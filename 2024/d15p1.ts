import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/15

function getStart(grid: string[][]): number[] {
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            if (grid[r][c] === '@') {
                return [r, c];
            }
        }
    }
    return [-1, -1];
}

function printGrids(grid: string[][], grid2: string[][]): void {
    for (let r = 0; r < grid.length; r++) {
        console.log(grid[r].join('') + '  ->  ' + (grid2[r] ? grid2[r].join('') : ''));
    }
}

function getScore(grid: string[][]): number {
    let score: number = 0;
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            if (grid[r][c] === 'O') {
                score += r * 100 + c;
            }
        }
    }
    return score;
}

function solve(): void {
    const grid: string[][] = rawGrid.split('\n').map(row => row.split(''));
    const originGrid: string[][] = grid.map(row => [...row]);
    let position: number[] = getStart(grid);
    let directionMap: { [key: string]: number[] } = {
        '^': [-1, 0],
        'v': [1, 0],
        '>': [0, 1],
        '<': [0, -1],
    };
    for (let move of moves) {
        let [r, c] = position;
        let [dr, dc] = directionMap[move];
        let nr = r + dr;
        let nc = c + dc;
        if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) continue;
        if (grid[nr][nc] === '.') {
            grid[nr][nc] = '@';
            grid[r][c] = '.';
            position = [nr, nc];
            continue;
        }
        if (grid[nr][nc] === 'O') {
            let tmpR = nr;
            let tmpC = nc;
            while (grid[tmpR] && grid[tmpR][tmpC] === 'O') {
                tmpR += dr;
                tmpC += dc;
            }
            if (grid[tmpR] && grid[tmpR][tmpC] === '.') {
                grid[tmpR][tmpC] = 'O';
                grid[nr][nc] = '@';
                grid[r][c] = '.';
                position = [nr, nc];
            }
        }
    }
    // printGrids(originGrid, grid);
    console.log('Score:', getScore(grid));
}

const [rawGrid, rawMoves] = readFileSync(determineInputFile(), 'utf-8').trim().split('\n\n');
const moves: string = rawMoves.split('\n').join('');
solve();
