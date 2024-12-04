import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/4

function searchWordInGrid(grid: string[][], word: string): number {
    const rows: number = grid.length;
    const cols: number = grid[0].length;
    let count: number = 0;

    function searchDirection(x: number, y: number, dx: number, dy: number): boolean {
        for (let i = 0; i < word.length; i++) {
            const nx = x + i * dx;
            const ny = y + i * dy;
            if (nx < 0 || ny < 0 || nx >= rows || ny >= cols || grid[nx][ny] !== word[i]) {
                return false;
            }
        }
        return true;
    }

    const directions = [
        [0, 1], [1, 0], [1, 1], [1, -1],
        [0, -1], [-1, 0], [-1, -1], [-1, 1]
    ];

    for (let x = 0; x < rows; x++) {
        for (let y = 0; y < cols; y++) {
            for (const [dx, dy] of directions) {
                if (searchDirection(x, y, dx, dy)) {
                    count++;
                }
            }
        }
    }

    return count;
}

function solve(lines: string[]): void {
    const grid = lines.map(line => line.split(''));
    const word = 'XMAS';
    const occurrences = searchWordInGrid(grid, word);
    console.log(`Total occurrences of '${word}':`, occurrences);
}

solve(readFileLines(determineInputFile()));
