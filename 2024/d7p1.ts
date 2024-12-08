import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/7

function canMakeIt(result: number, values: number[]): Boolean {
    if (values.length === 1) {
        return result === values[0];
    }
    const last = values[values.length - 1];
    const rest = values.slice(0, values.length - 1);
    if (result % last === 0 && canMakeIt(result / last, rest)) {
        return true;
    }
    if (result > last && canMakeIt(result - last, rest)) {
        return true;
    }
    return false;
}

// inefficient solution
function possibleValues(result: number, values: number[]): Set<number> {
    if (values.length === 1) {
        return new Set([values[0]]);
    }
    const last = values[values.length - 1];
    const rest = values.slice(0, values.length - 1);
    const subset = possibleValues(result, rest);
    const newSet = new Set<number>();
    subset.forEach(x => {
        newSet.add(x + last);
        newSet.add(x * last);
    });
    return newSet;
}

function solve(lines: string[]): void {
    let sum = 0;
    lines.forEach(line => {
        const [resultStr, valsStr] = line.split(':');
        const result = parseInt(resultStr.trim(), 10);
        const vals = valsStr.trim().split(' ').map(Number);
        // if (possibleValues(result, vals).has(result)) {
        //     sum += result;
        // }
        if (canMakeIt(result, vals)) {
            sum += result;
        }
    });
    console.log('Sum:', sum);
}

solve(readFileLines(determineInputFile()));
