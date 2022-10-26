#!/usr/bin/env python
# coding: utf-8
def gc_filtering(read, gc_bounds=(0, 100)):
    gc_num = len([GC for GC in read[1] if GC == "G" or GC == "C"])
    read_len = len(read[1])
    gc_content = 100 * gc_num / read_len
    if gc_bounds[0] <= gc_content <= gc_bounds[1]:
        return "passed"
    else:
        return "rejected"


def length_filtering(read, length_bounds=(0, 2 ** 32)):
    read_len = len(read[1])
    if length_bounds[0] <= read_len <= length_bounds[1]:
        return "passed"
    else:
        return "rejected"


def quality_filtering(read, quality_threshold=0):
    if sum([ord(i) - 33 for i in read[3]]) / len(read[3]) > quality_threshold:
        return "passed"
    else:
        return "rejected"


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0,
         save_filtered=False):
    with open(input_fastq, 'r') as file:
        count = len(file.readlines()) / 4
        file.seek(0)
        while count != 0:
            read = [file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip()]
            if save_filtered is True and (
                    gc_filtering(read=read, gc_bounds=gc_bounds) == "rejected" or
                    length_filtering(read=read, length_bounds=length_bounds) == "rejected" or
                    quality_filtering(read=read, quality_threshold=quality_threshold) == "rejected"):
                with open(f"{output_file_prefix}_failed.fastq", "a+") as failed_file:
                    for line in read:
                        failed_file.write(line + '\n')
            else:
                with open(f"{output_file_prefix}_passed.fastq", "a+") as passed_file:
                    for line in read:
                        passed_file.write(line + '\n')
            count -= 1
