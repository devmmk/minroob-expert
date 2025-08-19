import random

class MinesweeperSolver:
    def __init__(self):
        self.board = []
        self.rows = 0
        self.cols = 0
        
    def parse_board(self, board_text):
        lines = board_text.strip().split('\n')
        self.board = []
        
        emoji_map = {
            '1⃣': 1,
            '2⃣': 2,
            '3⃣': 3,
            '4⃣': 4,
            '5⃣': 5,
            '6⃣': 6,
            '7⃣': 7,
            '8⃣': 8,
            '⬜️': 'unopened',
            '🔴': 'mine_flagged',
            '🔵️': 'mine_flagged',
            ' ': 0
        }
        
        for line_num, line in enumerate(lines):
            row = []
            i = 0
            while i < len(line):
                matched = False
                for length in [3, 2, 1]:
                    if i + length <= len(line):
                        substr = line[i:i+length]
                        if substr in emoji_map:
                            row.append(emoji_map[substr])
                            i += length
                            matched = True
                            break
                if not matched:
                    i += 1
            
            if row:
                self.board.append(row)
        
        if self.board:
            max_cols = max(len(row) for row in self.board)
            for row in self.board:
                while len(row) < max_cols:
                    row.append(0)
        
        self.rows = len(self.board)
        self.cols = len(self.board[0]) if self.rows > 0 else 0
    
    def get_neighbors(self, row, col):
        neighbors = []
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append([nr, nc])
        
        return neighbors
    
    def get_unopened_neighbors(self, row, col):
        neighbors = self.get_neighbors(row, col)
        unopened = []
        for nr, nc in neighbors:
            if self.board[nr][nc] == 'unopened':
                unopened.append([nr, nc])
        return unopened
    
    def get_flagged_neighbors(self, row, col):
        neighbors = self.get_neighbors(row, col)
        flagged = []
        for nr, nc in neighbors:
            if self.board[nr][nc] == 'mine_flagged':
                flagged.append([nr, nc])
        return flagged
    
    def is_number(self, cell):
        return isinstance(cell, int) and cell > 0
    
    def find_certain_mines(self):
        certain_mines = set()
        
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                
                if self.is_number(cell):
                    unopened = self.get_unopened_neighbors(row, col)
                    flagged = self.get_flagged_neighbors(row, col)
                    
                    mines_needed = cell - len(flagged)
                    
                    if mines_needed > 0 and mines_needed == len(unopened):
                        for ur, uc in unopened:
                            certain_mines.add((ur, uc))
        
        return list(certain_mines)
    
    def find_probable_mines(self):
        mine_probabilities = {}
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'unopened':
                    mine_probabilities[(row, col)] = 0.0
        
        constraint_count = {}
        for pos in mine_probabilities:
            constraint_count[pos] = 0
        
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                
                if self.is_number(cell):
                    unopened = self.get_unopened_neighbors(row, col)
                    flagged = self.get_flagged_neighbors(row, col)
                    
                    mines_needed = cell - len(flagged)
                    
                    if mines_needed > 0 and len(unopened) > 0:
                        prob = mines_needed / len(unopened)
                        
                        for ur, uc in unopened:
                            pos = (ur, uc)
                            mine_probabilities[pos] += prob
                            constraint_count[pos] += 1
        
        for pos in mine_probabilities:
            if constraint_count[pos] > 0:
                mine_probabilities[pos] /= constraint_count[pos]
        
        sorted_mines = sorted(mine_probabilities.items(), 
                            key=lambda x: x[1], reverse=True)
        
        return sorted_mines
    
    def get_best_mine_guess(self):
        certain_mines = self.find_certain_mines()
        if certain_mines:
            mine_row, mine_col = certain_mines[0]
            return {
                'row': mine_row,
                'col': mine_col,
                'confidence': 1.0,
                'reason': 'Certain mine based on constraints'
            }
        
        probable_mines = self.find_probable_mines()
        
        if probable_mines:
            (mine_row, mine_col), probability = probable_mines[0]
            if probability > 0:
                return {
                    'row': mine_row,
                    'col': mine_col,
                    'confidence': probability,
                    'reason': f'Most probable mine ({probability:.2%} chance)'
                }
        
        unopened_cells = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'unopened':
                    unopened_cells.append((row, col))
        
        if unopened_cells:
            mine_row, mine_col = random.choice(unopened_cells)
            return {
                'row': mine_row,
                'col': mine_col,
                'confidence': 0.1,
                'reason': 'Random guess - no constraints available'
            }
        
        return None
    
    def analyze_board(self):
        print("\n🔍 === BOARD ANALYSIS ===")
        
        # Count cell types
        unopened = flagged = numbers = empty = 0
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                if cell == 'unopened':
                    unopened += 1
                elif cell == 'mine_flagged':
                    flagged += 1
                elif self.is_number(cell):
                    numbers += 1
                elif cell == 0:
                    empty += 1
        
        print(f"📦 Unopened cells: {unopened}")
        print(f"🚩 Flagged mines: {flagged}")
        print(f"🔢 Numbered cells: {numbers}")
        print(f"🟦 Empty cells: {empty}")
        
        certain_mines = self.find_certain_mines()
        if certain_mines:
            print(f"\n💣 Certain mines found: {len(certain_mines)}")
            for row, col in certain_mines:
                print(f"  - ({row}, {col})")
        
        probable_mines = self.find_probable_mines()
        if probable_mines:
            print(f"\n🔮 Top 5 most probable mines:")
            for i, ((row, col), prob) in enumerate(probable_mines[:5]):
                if prob > 0:
                    print(f"  {i+1}. ({row}, {col}) - {prob:.2%} probability")
        
        return self.get_best_mine_guess()