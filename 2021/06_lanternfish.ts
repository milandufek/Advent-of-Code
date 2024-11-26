import * as fs from 'fs';

function parseInput(filePath: string): number[] {
    const data = fs.readFileSync(filePath, 'utf8');
    return data.split('\n').filter(line => line.trim() !== '')[0].split(',').map(Number);
}

function reborn(fishes: number[], days: number): void {
    let q = Array(9).fill(0);
    fishes.forEach(fish => q[fish]++);
    for (let i = 0; i < days; i++) {
        let newFish = q.shift();
        q[6] += newFish;
        q.push(newFish);
    }
    console.log(`Sum (${days} days): ${q.reduce((a, b) => a + b, 0)}`);
}

reborn(parseInput('inputs/06.in'), 80);
