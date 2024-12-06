import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/6

function solve(grid: string[]): void {
    const rows = grid.length;
    const cols = grid[0].length;
    let start: [number, number] = [-1, -1];
    outer: for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '^') {
                start = [r, c];
                break outer;
            }
        }
    }

    let [r, c] = start;
    let [dr, dc] = [-1, 0];
    const visited = new Set<string>();

    while (true) {
        visited.add(`${r},${c}`);
        if (r + dr < 0 || r + dr >= rows || c + dc < 0 || c + dc >= cols) break;
        if (grid[r + dr][c + dc] === '#') [dr, dc] = [dc, -dr];
        else {
            r += dr;
            c += dc;
        }
    }
    console.log('Visited:', visited.size);
}

solve(readFileLines(determineInputFile()));
