from my_utils import get_data


# https://adventofcode.com/2022/day/13

class SignalDecoder:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.compare_counter = 0
        self.valid_sum = 0
        self.valid_list = []
        self.i_divider_packet_1 = 1
        self.divider_packet_1 = [[2]]
        self.i_divider_packet_2 = 2  # because of first one...
        self.divider_packet_2 = [[6]]
        self.decoder_key = 0

    def decode_signals(self) -> None:
        pair = []
        counter = 0
        packets = get_data(self.input_file)

        for p in packets:

            if p == '':
                pair.clear()
                continue

            pair.append(p)

            # part 1
            if len(pair) == 2:
                counter += 1
                if self.compare_packets(eval(pair[0]), eval(pair[1])) < 0:
                   self.valid_sum += counter
                   self.valid_list.append(pair)

            # part 2
            if self.compare_packets(eval(p), self.divider_packet_1) < 0:
                self.i_divider_packet_1 += 1
            if self.compare_packets(eval(p), self.divider_packet_2) < 0:
                self.i_divider_packet_2 += 1

        self.decoder_key = self.i_divider_packet_1 * self.i_divider_packet_2

    def compare_packets(self, left, right, debug: bool = False) -> int:
        status: int = 0
        self.compare_counter += 1

        if debug:
            print(f'#{self.compare_counter}\n'
                f'  Left: {left} ({type(left)})\n'
                f'  Right: {right} ({type(right)})')

        if isinstance(left, int):
            if isinstance(right, int):
                return left - right
            else:
                return self.compare_packets([left], right)
        elif isinstance(right, int):
                return self.compare_packets(left, [right])

        for z_left, z_right in zip(left, right):
            status = self.compare_packets(z_left, z_right)

            if status:  # false if 0 else true!
                return status

        return len(left) - len(right)

    def show_results(self) -> None:
        print(f'Valid signals ({self.input_file}): {self.valid_sum}')
        print(f'Decoder key ({self.input_file}): {self.decoder_key}')



if __name__ == '__main__':
    # s = SignalDecoder('inputs/13_example.in')  # 13, 140
    s = SignalDecoder('inputs/13.in')
    s.decode_signals()
    s.show_results()
