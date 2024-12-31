import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/15

function parseInput(path: string): [string[], string] {
    const data = readFileSync(path, 'utf-8').trim().split('\n\n');
    const grid = data[0].split('\n');
    const moves = data[1].split('\n').join('');
    return [grid, moves];
}

function getStart(grid: string[][]): [number, number] {
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            if (grid[r][c] === '@') {
                return [r, c];
            }
        }
    }
    return [-1, -1];
}

function expandGrid(grid: string[][]): string[][] {
    const expandedChars: { [key: string]: string } = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    };
    const expandedGrid: string[][] = [];
    for (const row of grid) {
        const expandedRow: string[] = [];
        for (const char of row) {
            expandedRow.push(...expandedChars[char]);
        }
        expandedGrid.push(expandedRow);
    }
    return expandedGrid;
}

function printGrid(grid: string[][]): void {
    for (const row of grid) {
        console.log(row.join(''));
    }
}

function getScore(grid: string[][]): number {
    let score = 0;
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            if (grid[r][c] === '[') {
                score += r * 100 + c;
            }
        }
    }
    return score;
}

function solve(): void {
    let grid: string[][] = expandGrid(originGrid.map(row => row.split('')));
    let position: [number, number] = getStart(grid);
    const directionMap: { [key: string]: [number, number] } = {
        '^': [-1, 0],
        'v': [1, 0],
        '>': [0, 1],
        '<': [0, -1],
    };

    function swap(tileA: [number, number], tileB: [number, number]): void {
        const [r1, c1] = tileA;
        const [r2, c2] = tileB;
        [grid[r1][c1], grid[r2][c2]] = [grid[r2][c2], grid[r1][c1]];
    }

    for (const move of moves) {
        const [dr, dc] = directionMap[move];
        const movable: [number, number][] = [position];
        let canMove = true;
        for (const [r, c] of movable) {
            const nr = r + dr, nc = c + dc;
            if (movable.some(([mr, mc]) => mr === nr && mc === nc)) {
                continue;
            }
            const tile = grid[nr][nc];
            if (tile === '#') {
                canMove = false;
                break;
            }
            if (tile === '[') {
                movable.push([nr, nc], [nr, nc + 1]);
            } else if (tile === ']') {
                movable.push([nr, nc], [nr, nc - 1]);
            }
        }

        if (canMove) {
            const key = (x: [number, number]) => (dr + dc === 1 ? -1 : 1) * x[Math.abs(dc)];
            movable.sort((a, b) => key(a) - key(b));
            for (const [r, c] of movable) {
                swap([r + dr, c + dc], [r, c]);
            }
            position = [position[0] + dr, position[1] + dc];
        }
    }

    console.log(getScore(grid));
}

let [originGrid, moves] = parseInput(determineInputFile());
solve();
