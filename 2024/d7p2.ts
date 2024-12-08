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
    const sTarget = result.toString();
    const sLast = last.toString();
    if (sTarget.endsWith(sLast)) {
        const newTarget = parseInt(sTarget.slice(0, -sLast.length) || '0');
        if (canMakeIt(newTarget, rest)) {
            return true;
        }
    }
    return false;
}

function solve(lines: string[]): void {
    let sum = 0;
    lines.forEach(line => {
        const [resultStr, valsStr] = line.split(':');
        const result = parseInt(resultStr.trim(), 10);
        const vals = valsStr.trim().split(' ').map(Number);
        if (canMakeIt(result, vals)) {
            sum += result;
        }
    });
    console.log('Sum:', sum);
}

solve(readFileLines(determineInputFile()));
