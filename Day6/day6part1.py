import pdb
teststring = 'rhghwwsmsgmgsmmmlzljllrddvsvhvhhnvvrcccwhhvgghchwhvwvcvrrrgtgrgdggfdgffshsllvvslsppglgvgwgswwcbcwbwrrbjbwjjtgjjdzdfdhfddrmmhqhpqhhqghhzssqzqccbwwffzvzffvtftddrbrtrrcjrrmmbmrrrlrppplmplmppfzpfpvpqvpqqdndpndnmnwmwjmwmwbbrhhmzmffwfqwfqwffppvfpvffnwwwwcbwbhbccvmmplmplmmlmplpprbpbllmhlhzhffngfnntrrsrprrvlllvjvmjvvppsrrfnrfnrfrfwrffrsfrflfltfllpfprrthhhnhqnnfwwcttvzzddqsddwpddnrnttvjttjjdjvdjvjnvnrvvchhschhlffjggtqgqnnvrnrsnrsnsvspsnncppvwvvtmmcqmcmscmsmwmvmpvvlqqmbqqlwwtgtztgttpjjbfjjzhzthhzssffwqqdmdcdlclrclrccbmmqjqmqcmmnnsvnntpphhdpdhhtbtdtffhzfhhpwhppwbppfspphdhggzqgzzffdsdfsszcscpscsqcssffhjhnhhlqqdbqqdmdsmddrfddndldgglvglvlggqlggjngjnnbffthhjbjpjnjmnmgmqqbjqjzjqzzzjffwttcnnzffmllcncmnnthnncttpgpnnjdjfftmmvqmqsqggfrfjjqbjbvvshvhphfhhljlfjjvcclzclctcmmfwfvwfvwwjvwvjjplpbpqqdvqqbhbdbnnsndssgffgsglssmfmjjfrjfrfttljldjdffjjdnjjlbbnrntrtfrttmhhndnsdsffgqqrpplvvfwvfvsfszzfzhfzzlttlctllrzrggvwvhhgnnlmnlmlpppdldqqdpdlplrpppjspspzzhphccgjjpmmwvwbwssnpssrzrwrhhmzhmhsmhmttrqrvqvcclggptpjpzpccltctppflfjffrtrjrhjhffhjfjbfjfqfqzffdtthwwjwzjzggsgzgqqjdqjddvgvsvnnqwqgwgtttfvfrfwrfwfwmwmqwmmmbzmzvzfvfrfvvgvtvptpbpwbwrbwrwffzzfgzfgfcfzcffjdjjvrvnnfmmtztffsggjcjzcjcssscnscnssmmwgwbbljlnjndnrrqwqjjjbnnmbmcmbcmbbvvmtvmmfcmcjcdcnnzfzfzqfzfvvmbvmmndnbnsnnlddqvvsnngvnnrttfbtbqqnwqqzfzfzccfmmgrrsbbhvvgjjhfhssjmmsjjzzbqblqlfqllwhlwwvvstvtfvttnncjjzcjcjrrsvrssmfsfczbrzrvscvmcmrjpzwhcqfrrzbljnmqlzbzqtmhrshlrjjpvhnsvtlhqggqwppsjpszmqwfqmlwbqzwcrggrvfbvztnflwvbrqcrqbcllswvsvhwjzpldgphwptfdnlgdlnbttjfzrdcfvpdhlssfsljvdjmwddbnrpqnnqlfdfdspbnjwqjwrgtnrftsqcfjpmqwgwhttggjwzvgbwlhmtmmjlwhssrgshzpbcnstzlqdshdhjfgqlsmqqhpwbscsjhfbhprvhmftqngjgdbcvfldqgqsjqjfdmcvsflwzflsjfssnjpbwffnsfcnrdsphbjpgghmcthgnzmpgppqjdvbztvhnwqzndntcpjdtwwhvsmgdcthpssszrqcbntgsznpghmbqddpqscntjprlwzhbzhjtwzbwwcldwdgsttzmtnstjnngzrgvhncdbgqnllfzbthldztsdwsngjzprbvrnbzrsghlgssbqfnbvhnhzwmmmtncvsdngdtwcbjlnnzbnlrnmrvnvsjnvzdqnggmsvljlvjznwdszcmblhrsjvczpnlhsmqjsmwhbjbplbtqsgqjdllhncwdgbvzwnmqvndcbfhnvtjnzmvjhwzvdldhgfwbqqzcnbflfnwntlhmqgdhmrgwqcpmsvfbmwhbtsbdlhcnbcbswvdfffgjvddrbpzpcwsrsjnfvmzhlvbdnwttnqrmzbnnntbfvptrlhjhwjcsbnhvtwtwzvgfnzjplthqjbsjjwzdtqqvblnbvgcmvrmnvmwfrhcqgvrcjlfzdlpbfvncbtfgvnsflbjzqqhczcmtbwqmrppmptfgzvfbmcslwlfrfpvvnvvnwfvvmmdzmmtjsgqdfhngtphtlfjqrtljgnthgnbbqfrnpfmpwhpzdvzmtswwdvcnpsdcqwjdwlvbsbmlwdsjbcbgcrfljshlvpngfmsrzlfhtfqgwbcctnzzhnqhdmqzdwthftwtmpbcmqvdcdtgvltbzmszzwwmhzlfvbdqnhjqgdmstsnhftcwzvvbmnhwvgqzscwcdjbdgfmvpjdzctwqwltbwjlgcblnnhpnmggbmvqpqtgqjzspgqzvcvsdbvjgjfzdzhfpbzjqljjcgldzgnlmtjcmfgdbqgglvjqrppwmhccvqzvsrjjvfhjprwdsqsnszfprznljtcsrtqhcrpljfrccflmbpvqtzgmzhjrlbnrmmsmmjbtzwpglqgdvvvjvnfzmplsmvlvcnjshvjwntclwgpznnzwhjssgdcjbzrmsgnfgcgphrhfvrfhzwdcvsplhbmqwhpmjvqlmschznbqblvhtqfgtdggmncndhhplnzjphccjmlmtdqnmnlnpnfqdstljqnsqbrjrtspvrwvdmwzlgdmsfvctzgtmgqhqqrzpbgplzcfdqnzhsqrbcvhsccshnnpvvrpvqzqsgzgmpzfvvrrcvhdtntnsqnjrbzlbzmpgwdqzbhtlrrhbwdqjlsfgdhmvgmgbqhwvljmmqfllqvvrznrlftgzjdcgtstjffqmgvffpvtctzpdqjfnmlcdzscntctmqhrtmhrlhbjzttrcvcnlhsrvtpbmdchhntnnpnzlvqqnsrjcmblcvphqgwshnjmplgvnbsmmdzgqcpqztjhhgjvtlbpdpdwlwmmfrdgcvzfbgvbgpbjnwsssvhszwplcgvpgjwdrwngbcdjwvlsfhqlrqzgrzpfgjstqfdbrpqdvrlgdwqcsrgvhctznjjlzsmzctsqtfnhhlpjgnltssglmlwshfbrgmjqbvsmqwvszdfsvhmtrfjgwjctpsmgzzjbpwsztnnvzrhwvvmhdpgdmwzsjprhlgzcdvhznlfgjqvcwqrplcfvzmthsdsnrtfvnlrmvwplmbdvdggmlvpgdgzhvzmvzwmptzsnfrcrjspccmqjpjmhjqgrjbdcdjbzjmphmcdvjqtmdshhjrqgjgsnpzfbfgpjpczwzvmclgzgztlvzmdbwgncnndjwhhhjnhtjdmcnrmnqbmjdrdcmtvcsmftqcfhsvhsfjmtzjpnwffggpfqlqmzlbhnnhbtgzfgnjvdzmvthqjrhzbwvhcjzcsmsvsctrqbltpcrpjjnsbjdbfjqfcbpcgcwtqsflmlwprjcwlmcjjgsfdpwcqvhjpsgvdgsfnscnbzsrmrbbvdrlltzplbvgqsdnplcvbhddbtmwnfmvqhqdlrtrmrmzmhlccgwgmbdppjqdjtwmvdzfsbsggrfstjwjpjnljffwffmqncfnthnhglwvsgvzmgbzhtdfpfmdwmcldthvsnqnptpmhqctblgfsszhcfbvcrggjdhthqvvvlldshvqwmvdtfslrhzvgdfwztrczdjgcfcgtmwnphqthlgpfnrqwcgpzwnlgdvsnvzftlnlfflfsmjzhrhqjctsbvtccwbfsdrnbhszzjhqndvwcsmffnstnfdfwpbgfztjmjngdczzlgpscjtshpmmmzlnqndsttbdgfjqcvbqlphwhlhgcvjbhjmtrfzlgpwdnvzrllndbhvhlngvhlszzdcrdgvrmjwcvhhtbhnjmdzgctqnpdlrnqjzbchjtcsggsczlgmvtqvzmsqvtrhtvdmzlcdddfnbvbsnrzvgzfqjtbhjqhdznrhbfbqwtnwvrfqsznbqfzfzfgmhvjjsgbbdbdtzswwlnfrq'
#teststring = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

test = True
ix = 0
while test:
    if len(set(teststring[ix:ix+14])) == 14:
        test = False
    else:
        ix += 1

print(ix+14)