import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/17

function combo(op: number): number {
    if (0 <= op && op <= 3) {
        return op;
    } else if (op === 4) {
        return a;
    } else if (op === 5) {
        return b;
    } else if (op === 6) {
        return c;
    } else {
        throw new Error('Invalid combo operand');
    }
}

function run(): void {
    let operand: number;
    const output: number[] = [];
    while (program.length > pointer) {
        instruction = program[pointer];
        operand = program[pointer + 1];
        if (instruction === 0) {         // adv
            a = a >> combo(operand);
        } else if (instruction === 1) {  // bxl
            b = b ^ operand;
        } else if (instruction === 2) {  // bst
            b = combo(operand) % 8;
        } else if (instruction === 3) {  // jnz
            if (a !== 0) {
                pointer = operand;
                continue;
            }
        } else if (instruction === 4) {  // bxc
            b = b ^ c;
        } else if (instruction === 5) {  // out
            output.push(combo(operand) % 8)
        } else if (instruction === 6) {  // bdv
            b = a >> combo(operand);
        } else if (instruction === 7) {  // cdv
            c = a >> combo(operand);
        }
        pointer += 2;
    }
    console.log(output.join(','));
}

let instruction: number = 0;
let pointer: number = 0;
const data: string = readFileSync(determineInputFile(), 'utf-8').trim();
let [a, b, c, ...program] = Array.from(data.matchAll(/\d+/g), m => parseInt(m[0]));
run();
