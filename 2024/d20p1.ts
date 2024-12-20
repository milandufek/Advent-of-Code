import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/20

function getPosition(grid: string[][], char: string): number[] {
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            if (grid[r][c] === char) {
                return [r, c];
            }
        }
    }
    return [-1, -1];
}

function getMinimumSteps(grid: string[][]): number {
    const start = getPosition(grid, 'S');
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let queue: number[][] = [[0, start[0], start[1]]];
    let visited = new Set<string>();
    visited.add(`${start[0]}:${start[1]}`);
    while (queue.length > 0) {
        let [steps, r, c] = queue.shift()!;
        if (grid[r][c] === 'E') return steps;
        for (const [dr, dc] of directions) {
            let nr = r + dr;
            let nc = c + dc;
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) continue;
            if (visited.has(`${nr}:${nc}`)) continue;
            if (grid[nr][nc] === '#') continue;
            visited.add(`${nr}:${nc}`);
            queue.push([steps + 1, nr, nc]);
        }
    }
    return Infinity;
}

function findShortCuts(grid: string[][]): number[][] {
    let gridCopy: string[][] = grid.map(row => row.slice());
    const start = getPosition(gridCopy, 'S');
    gridCopy[start[0]][start[1]] = '.';
    const end = getPosition(gridCopy, 'E');
    gridCopy[end[0]][end[1]] = '.';

    const shortcuts: number[][] = [];
    for (let r = 1; r < gridCopy.length - 1; r++) {
        for (let c = 1; c < gridCopy[r].length - 1; c++) {
            if (gridCopy[r][c] === '#') {
                if (gridCopy[r - 1][c] === '.' && gridCopy[r + 1][c] === '.') {
                    shortcuts.push([r, c]);
                } else if (gridCopy[r][c - 1] === '.' && gridCopy[r][c + 1] === '.') {
                    shortcuts.push([r, c]);
                }
            }
        }
    }
    return shortcuts;
}

function solve(lines: string[]): void {
    let grid: string[][] = lines.map(line => line.split(''));
    let steps: number = getMinimumSteps(grid);
    let times: number[] = [];
    for (const [r, c] of findShortCuts(grid)) {
        grid[r][c] = '.';
        times.push(getMinimumSteps(grid));
        grid[r][c] = '#';
    }
    let cheaters = times.filter(t => t <= steps - 100);
    console.log('Cheaters:', cheaters.length);
}

solve(readFileLines(determineInputFile()));
