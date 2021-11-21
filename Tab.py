import math

class Tab:
    # syntax: https://www.guitartricks.com/helptab.php

    # TODO: import/export
    # TODO: write to latex
    # TODO: insert_time (beat, snap, num_snaps) -> adds num_snaps time at (beat, snap)
    # TODO: delete(beat, snap, num_snaps) -> removes num_snaps snaps beginning in (beat, snap)
    # TODO: play tab: https://realpython.com/playing-and-recording-sound-python/
    # TODO: allow to insert multiple fret at the same time (in different chords, for the same beat)

    def __init__(
        self,
        strings = ["e", "B", "G", "D", "A", "E"],
        beats_per_bar = 4,
        snaps_per_beat = 4
        ):
        self.__max_len = 150

        # here string denotes a guitar string
        self.__strings = strings
        self.__max_string_len = max([len(i) for i in self.__strings])
        self.__string_sep = "|"

        # a bar is a set of beats in a specific tempo
        self.__bar_sep = "|"
        
        # a beat is the basic rhythmic unit of measure
        self.__beats_per_bar = beats_per_bar
        self.__beat_marker = "*"

        # a snap is a subdivision of beats
        self.__snaps_per_beat = snaps_per_beat
        self.__snap_char = "-"
        self.__snap_len = 2
        self.__snap_marker = "."

        self.__set_bars_per_line()

        # { beat: { snap: { string: fret } } }
        self.__music = {}


    # calculate ideal bars_per_line based on max line length, beat_snap, etc
    # if snap_len is increased by some fret, it adjusts the lines per bar
    def __set_bars_per_line(self):
        bar_len = self.__snap_len * self.__snaps_per_beat * self.__beats_per_bar
        self.__bars_per_line = (self.__max_len - self.__max_string_len - len(self.__string_sep)) // bar_len
        if self.__bars_per_line == 0:
            self.__bars_per_line = 2


    # basic add operation: adds a fret in string, in a snap of a beat
    def add(self, string, fret, beat=False, snap=False):
        if string not in self.__strings:
            raise ValueError(f"Tab.add - Invalid argument: string must be one of {self.__strings}")
        
        if type(fret) is not str:
            raise ValueError(f"Tab.add - Invalid argument: fret must be a string")

        if (beat == False and snap != False) or (beat != False and snap == False):
            raise ValueError("Tab.add - Invalid argument: cannot specify a snap without specifying a beat or vice versa")

        if beat != False and (type(beat) is not int or beat < 1):
            raise ValueError("Tab.add - Invalid argument: beat must be a positive integer")
        
        if snap != False and (type(snap) is not int or not (1 <= snap <= self.__snaps_per_beat)):
            raise ValueError(f"Tab.add - Invalid argument: snap must be an integer in range [1, {self.__snaps_per_beat}]")

        # Need to find next beat/snap
        if beat == False:
            beats = self.__music.keys()
            if len(beats) == 0:
                beat = 1
                snap = 1
            else:
                max_beat = max(self.__music.keys())
                max_snap = max(self.__music[max_beat].keys())

                if max_snap == self.__snaps_per_beat:
                    beat = max_beat + 1
                    snap = 1
                else:
                    beat = max_beat
                    snap = max_snap + 1            


        if beat not in self.__music:
            self.__music[beat] = {}
        
        if snap not in self.__music[beat]:
            self.__music[beat][snap] = {}
        
        self.__music[beat][snap][string] = fret

        # adjust output snap length if necessary
        if len(fret) >= self.__snap_len:
            self.__snap_len = len(fret) + 1
            # do not forget to update bars per line
            self.__set_bars_per_line()

    # This funcion returns the item that is stored for that beat, snap and string
    def get(self, beat, snap, string):
        # TODO: check argument validity
        if beat not in self.__music or snap not in self.__music[beat] or string not in self.__music[beat][snap]:
            return self.__snap_char * self.__snap_len
        
        item = self.__music[beat][snap][string]
        return f'{item}{self.__snap_char * (self.__snap_len - len(item))}'


    def __repr__(self):
        res = ""

        n_bars = math.ceil(max(self.__music.keys()) / self.__beats_per_bar)
        n_lines = math.ceil(n_bars / self.__bars_per_line)

        line_beat = 1
        
        for line in range(n_lines):

            # represent snap/beat division in each line
            snap_beat_marker = " " * (self.__max_string_len + 1) # account for space
            snap_beat_marker += self.__string_sep
            for _ in range(self.__bars_per_line):
                for _ in range(self.__beats_per_bar):
                    snap_beat_marker += self.__beat_marker + " " * (self.__snap_len - 1)
                    for _ in range(self.__snaps_per_beat - 1):
                        snap_beat_marker += self.__snap_marker + " " * (self.__snap_len - 1)
                snap_beat_marker += self.__bar_sep

            res += snap_beat_marker + "\n"

            # represent frets for each string
            for string in self.__strings:
                cur_beat = line_beat
                res += f'{" " * (self.__max_string_len - len(string))}{string} {self.__string_sep}'
                for bar in range(self.__bars_per_line):
                    for beat in range(self.__beats_per_bar):
                        for snap in range(self.__snaps_per_beat):
                            res += self.get(cur_beat, snap + 1, string)

                        cur_beat += 1
                    res += self.__bar_sep
                res += '\n'
            
            line_beat = cur_beat
            
            res += '\n'
        
        return res

