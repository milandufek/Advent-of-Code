import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/4

function searchXmasInGrid(grid: string[][]): number {
    let count = 0;

    for (let x = 1; x < grid.length - 1; x++) {
        for (let y = 1; y < grid[0].length - 1; y++) {
            if (grid[x][y] !== 'A') {
                continue;
            }
            const corners: string[] = [
                grid[x - 1][y - 1], grid[x - 1][y + 1],
                grid[x + 1][y + 1], grid[x + 1][y - 1]
            ];
            if (['MMSS', 'MSSM', 'SSMM', 'SMMS'].includes(corners.join(''))) {
                count++;
            }
        }
    }

    return count;
}

function solve(lines: string[]): void {
    const grid = lines.map(line => line.split(''));
    const occurrences = searchXmasInGrid(grid);
    console.log('Total occurrences of X-MAS:', occurrences);
}

solve(readFileLines(determineInputFile()));
