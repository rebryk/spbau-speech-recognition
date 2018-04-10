
if __name__ == '__main__':
	with open('train.csv', 'w') as f:
		for i in range(1, 451):
			f.write(f'/workspace/data/VCTK-Corpus/wav48/p239/p239_{i:03d}.wav,/workspace/data/VCTK-Corpus/txt/p239/p239_{i:03d}.txt\n')

	with open('val.csv', 'w') as f:
		for i in range(451, 476):
			f.write(f'/workspace/data/VCTK-Corpus/wav48/p239/p239_{i:03d}.wav,/workspace/data/VCTK-Corpus/txt/p239/p239_{i:03d}.txt\n')

	with open('test.csv', 'w') as f:
		for i in range(476, 504):
			f.write(f'/workspace/data/VCTK-Corpus/wav48/p239/p239_{i:03d}.wav,/workspace/data/VCTK-Corpus/txt/p239/p239_{i:03d}.txt\n')
