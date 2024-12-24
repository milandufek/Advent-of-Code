import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/24

function parseWires(wires: string): { [key: string]: number } {
    let map: { [key: string]: number } = {};
    for (const line of wires.split('\n')) {
        let [wire, val]: string[] = line.split(': ');
        map[wire] = parseInt(val);
    }
    return map;
}

function operate(a: number, b: number, op: string): number {
    switch (op) {
        case 'AND': return a & b;
        case 'OR':  return a | b;
        case 'XOR': return a ^ b;
    }
    return -1;
}

function solve(inputFile: string): void {
    let [wires, connections] = readFileSync(inputFile, 'utf-8').split('\n\n');
    let wireMap: { [key: string]: number } = parseWires(wires);
    while (true) {
        let updated: boolean = false;
        for (const conn of connections.split('\n')) {
            let [a, op, b, _, c] = conn.split(' ');
            if (wireMap[a] === undefined) continue;
            if (wireMap[b] === undefined) continue;
            if (wireMap[c] === undefined) {
                wireMap[c] = operate(wireMap[a], wireMap[b], op);
                updated = true;
            }
        }
        if (!updated) break;
    }
    const result = Object.keys(wireMap)
        .filter(key => key.startsWith('z'))
        .sort()
        .map(key => wireMap[key])
        .reverse()
        .join('');
    console.log(parseInt(result, 2));
}

solve(determineInputFile());
