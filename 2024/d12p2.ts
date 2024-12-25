import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/12

function countCornerCells(region: number[][]): number {
    let corners = 0;
    for (const [i, j] of region) {
        const T = region.some(([x, y]) => x === i - 1 && y === j);
        const R = region.some(([x, y]) => x === i && y === j + 1);
        const B = region.some(([x, y]) => x === i + 1 && y === j);
        const L = region.some(([x, y]) => x === i && y === j - 1);
        const TR = region.some(([x, y]) => x === i - 1 && y === j + 1);
        const BR = region.some(([x, y]) => x === i + 1 && y === j + 1);
        const BL = region.some(([x, y]) => x === i + 1 && y === j - 1);
        const TL = region.some(([x, y]) => x === i - 1 && y === j - 1);
        // is single cell   => 4 corners
        if (!T && !R && !B && !L) corners += 4;
        // has neighbor     => 2 corners
        if (T && !R && !B && !L) corners += 2;
        if (R && !B && !L && !T) corners += 2;
        if (B && !L && !T && !R) corners += 2;
        if (L && !T && !R && !B) corners += 2;
        // is outer corner  => 1 corner
        if (T && R && !B && !L) corners += 1;
        if (T && L && !B && !R) corners += 1;
        if (B && R && !T && !L) corners += 1;
        if (B && L && !T && !R) corners += 1;
        // is inner corner  => 1 corner
        if (R && T && !TR) corners += 1;
        if (R && B && !BR) corners += 1;
        if (L && T && !TL) corners += 1;
        if (L && B && !BL) corners += 1;
    }
    return corners;
}

function calculateConnectedCells(x: number, y: number): number {
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const seen: Set<string> = new Set();
    const queue: number[][] = [[x, y]];
    const region: number[][] = [];
    const key = `${x},${y}`;
    seen.add(key);
    checked.add(key);
    while (queue.length > 0) {
        const [x, y] = queue.shift()!;
        region.push([x, y]);
        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;
            const key = `${nx},${ny}`;
            if (seen.has(key)) continue;
            seen.add(key);
            if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) continue;
            if (grid[nx][ny] === grid[x][y]) {
                queue.push([nx, ny]);
                checked.add(key);
            }
        }
    }

    let sides: number = countCornerCells(region);

    return region.length * sides;
}

function solve(): void {
    let score: number = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (checked.has(`${r},${c}`)) continue;
            score += calculateConnectedCells(r, c);
        }
    }
    console.log(score);
}

const lines: string[] = readFileLines(determineInputFile());
const grid: string[][] = lines.map(line => line.split(''));
const rows: number = grid.length;
const cols: number = grid[0].length;
const checked: Set<string> = new Set();
solve();
