import { readFileSync } from 'fs';

export function readFileLines(path: string): string[] {
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

function bfs(lines: string[]): number {
    const grid: string[][] = lines.map(line => line.split(''));
    const rows = grid.length;
    const cols = grid[0].length;
    const wall = '#';
    const start = [0, 0];
    const end = [rows - 1, cols - 1];
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let queue: number[][] = [[0, start[0], start[1]]];  // steps, row, col
    let visited = new Set<string>();
    visited.add(`${start[0]}:${start[1]}`);
    while (queue.length > 0) {
        let [steps, r, c] = queue.shift()!;
        if (r === end[0] && c === end[1]) return steps;
        for (const [dr, dc] of directions) {
            let nr = r + dr;
            let nc = c + dc;
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) continue;
            const cacheKey = `${nr}:${nc}`;
            if (visited.has(cacheKey)) continue;
            if (grid[nr][nc] === wall) continue;
            visited.add(cacheKey);
            queue.push([steps + 1, nr, nc]);
        }
    }
    return -1;
}
