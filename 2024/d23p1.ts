import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/23

function solve(lines: string[]): void {
    let connections: { [key: string]: Set<string> } = {};
    for (const line of lines) {
        let [left, right] = line.split('-');
        if (!(left in connections)) {
            connections[left] = new Set();
        }
        if (!(right in connections)) {
            connections[right] = new Set();
        }
        connections[left].add(right);
        connections[right].add(left);
    };

    let sets: Set<string> = new Set();
    for (let a in connections) {
        for (let b of connections[a]) {
            for (let c of connections[b]) {
                if (a !== c && connections[c].has(a)) {
                    sets.add(',' + [a, b, c].sort().join(','));
                }
            }
        }
    }
    let count: number = Array.from(sets).filter(s => s.includes(',t')).length;
    console.log('Count:', count);
}

solve(readFileLines(determineInputFile()));
