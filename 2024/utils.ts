import { readFileSync } from 'fs';

export function readFile(path: string): string[] {
    const data: string = readFileSync(path, 'utf-8');
    return data.trim().split('\n').map(s => s.trim());
}

export function determineInputFile(): string {
    let input: string = process.argv[2];
    if (['-t', '--test', 'test'].includes(input)) {
        input = `inputs/test.txt`;
    } else {
        const match = String(process.argv[1]).match(/d(\d+)p/);
        let input_file: string = match ? match[1] : 'test';
        input = `inputs/${input_file}.txt`;
    }
    console.debug('Input file:', input);
    return input;
}

export function zip<T, U>(arr1: T[], arr2: U[]): [T, U][] {
    const length = Math.min(arr1.length, arr2.length);
    const result: [T, U][] = [];
    for (let i = 0; i < length; i++) {
        result.push([arr1[i], arr2[i]]);
    }
    return result;
}

export function pairwise<T>(arr: T[]): [T, T][] {
    let pairs: [T, T][] = [];
    for (let i = 0; i < arr.length - 1; i++) {
        pairs.push([arr[i], arr[i + 1]]);
    }
    return pairs;
}
