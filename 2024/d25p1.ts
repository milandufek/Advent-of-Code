import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/25

function countChars(s: string, ch: string): number {
    return s.split(ch).length - 1;
}

function convertRowsToCols(rows: string[]): string[] {
    let cols: string[] = [];
    for (let i = 0; i < rows[0].length; i++) {
        cols.push(rows.map(row => row[i]).join(''));
    }
    return cols;
}

function solve(locksAndKeys: string[]): void {
    const MAX_HEIGHT = 7;
    let locks: number[][] = [];
    let keys: number[][] = [];
    for (let item of locksAndKeys) {
        let itemArray: string[] = item.split('\n');
        let converted: string[] = convertRowsToCols(itemArray);
        let code = converted.map(col => countChars(col, '#'));
        if (itemArray[0] == '#####') locks.push(code);
        else keys.push(code);
    }
    let matches: number = 0;
    for (let lock of locks) {
        matches += keys.filter(key => key.every((k, i) => lock[i] + k <= MAX_HEIGHT)).length;
    }
    console.log('Matches:', matches);
}

solve(readFileSync(determineInputFile(), 'utf-8').trim().split('\n\n'));
