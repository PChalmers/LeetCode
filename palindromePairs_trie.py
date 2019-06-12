from collections import defaultdict
import datetime

class NodeForTrieTree:
    def __init__(self): 
        self.childNodes = defaultdict(NodeForTrieTree)
        self.indexOfEndingWord = -1
        self.indexMarkingStartOfpalindromes = []

class TrieTree : 
    def __init__ (self) :
        self.rootNode = NodeForTrieTree()

    def addWordToTrie(self, wordToAdd, indexOfWord):
        def isAPalindrome(word):
            return word == word[::-1]        
        
        currentNode = self.rootNode
        for indexOfChar, char in enumerate(reversed(wordToAdd)):
            temp = wordToAdd[0:len(wordToAdd)-indexOfChar]
            if isAPalindrome(temp): 
                  currentNode.indexMarkingStartOfpalindromes.append(indexOfWord)
            currentNode = currentNode.childNodes[char]
        currentNode.indexOfEndingWord = indexOfWord


class Solution:
    def makeTrie(self, listOfWords):
        self.trieTree = TrieTree()
        for indexOfWord, word in enumerate(listOfWords): 
            self.trieTree.addWordToTrie(word, indexOfWord)
        return self.trieTree
    
    # Takes the trie, a word, and its index in the word array 
    # and returns the index of every word that could be appended
    # to it to form a palindrome.
    def getPalindromesForWord(self, trie, word, index):
         # Walk trie. Every time we find a word ending,
         # we need to check if we could make a palindrome.
         # Once we get to the end of the word, we must check
         # all endings below for palindromes (they are already
         # stored in 'palindromesBelow').
        pairsOfWordsToReturn = []
        
        def isAPalindrome(word):
            return word == word[::-1]
    
        while(word != None):
            if(trie.indexOfEndingWord >= 0): 
                if(isAPalindrome(word)): 
                    pairsOfWordsToReturn.append(trie.indexOfEndingWord)
            if(word[0] not in trie.childNodes): 
                return pairsOfWordsToReturn
            trie = trie.childNodes[word[0]]
            word = word[1:]
        
        # word has ended. There can be more in Trie
        if trie: 
            if(trie.wordEndIndex >= 0): 
                pairsOfWordsToReturn.append(trie.indexOfEndingWord)
            pairsOfWordsToReturn.extend(trie.indexMarkingStartOfpalindromes)
        return pairsOfWordsToReturn

    def palindromePairs(self, words):
        trie = self.makeTrie(words)
        output = []
        for i, word in enumerate(words):
            t = trie.rootNode
            candidates = self.getPalindromesForWord(t, word, i)
            output.extend([[i,j] for j in candidates if j != i])
        return output

s = Solution()
# print(s.palindromePairs(["a","abc","aba",""]))

start = datetime.datetime.now()
print(s.palindromePairs(["gbagiejccfefdja","ecghjehhabihjjdg","ij","diecfdcggfbih","a","bbaggbheggidcjaffdeg","ffeegjf","hicghibjhdggegac","ibfeggda","fjdgdhfie","hadefcabdfgcaagb","hjadfehbahcfbhjjieca","gihhcgdgedhffe","bbcjfccjceejajj","djdj","eebbeafci","icgeahffcedef","ichbc","dffbjhihegghgbff","gdajicijabibcggacch","fecidebdechdaf","ha","ebj","dheeaiihhg","bb","cc","eiehdebiaicedibji","hjeij","c","bi","fdb","aeigac","adgibhegfffdjacfdc","geiieheddbahjdga","hgjjibafjc","fdjbd","ecaigajddbcfhif","dhcdcdhfgbfidfabacei","edegdfcahbhidgchf","aiecebg","dihdebafjhgbagbjdh","dcighgdajdagbb","gaiaag","idghfcfcffehbggdaeb","bdi","dbifhgj","cedeiaiidcdjjjbgeh","bhfhbbbe","ecacidgddggifajidfa","jd","hhbgbcddehbdc","gbgeieb","hgcdfbbfbdbcgb","ijfifbe","bjjhgehihdhahd","dacjcgdabba","ebcdeaediahjifdbgee","degbiice","chjbdbgjjhgiidcehehe","iegdjdgihhhccafdedi","bjj","gcdee","dbcaeiaceaedjbcehjea","fdbjfjdedaceajjjbhf","j","gdcbjhdbiehejidc","ajgib","jheheccjadiedcib","eagejbehjahaj","jgdji","bh","g","abchcebhdhjfjgcc","djihjbfjadjibfjbgcfa","egcjibgjb","bfebabjahgaii","hjecacdd","ahacejicaggccaaaeb","cfggdc","gagheffcghicgia","aggghigfhbgfeh","head","cbggaidah","dgbajfhihediajjb","cihhhgdjij","cdadhjeehiejch","gfdae","ajhcheibijabagej","becdggd","idagidgffic","fdibaaeihaefeagbid","chjiaec","hcjbfdbhbajbcai","egbjhbegjigdicgdjdab","igecajb","ajafhd","efbhghaaieae","dfiacgijif","efdjf","cgfiehjiggafhd","ajahigiijd","eddfechgceifjc","hig","ijcgfbbefcabefbbheca","ahgdhaefaihgbiaf","aicacifajigfhidgfac","ibghfihjbgcd","ecdacaiid","jifihdjehcdedhaebjig","dfgch","ddfdadjddgejjcfefd","aciieececcdf","fgcdjjcigb","hgc","dhcidegafifjgje","ebhbfecfdihbba","bc","fhibbhbhji","gfbh","jhji","dbhgfibgdh","iffgdddefc","jigegibbjiga","iicfiiiiiifcdj","ihdaaf","eggijdb","ggcidccbcgcdjdjhbj","aib","chbiaeaacgehddia","hadehejfgach","icghjhjagheeecafee","ibifdihbjccjac","jjjihbjb","hhhffi","geccedfbghcg","ae","hcgf","acbfcghchahcbjaii","bcgcdifbigcfhfefga","cecihdghfffddjcecidd","hhiicchdbi","fdahfdjbdhceabac","eidihihaddbcc","hcaahghgijdgfcbibhc","eiggdcdch","fifgejbihgcajdffh","bhjjib","fgcejhaehbdbhdgdhib","bgjfhccidbibabf","ijeeaeeeebcfceeif","gahidiehdfgdi","fgigdfgjbhahehaed","iafffcdb","d","cdgh","cchafjghfdaecdffdcgf","aecacedfeigcfghcfdef","jbeidacgh","eacecd","afhbihecce","acfbahfjdgdchijcaai","biig","ehdbhifaiaagi","jdecb","hdjfhggjgcfjdjcd","icahcjbad","e","bifjbifbghdciaidg","jjcbdichegeiejaga","aehhb","caabaejjcfjdhafba","ehfiec","gcjbjfeacccbegedefa","fchggc","jbefahijhhgagcjgdcfe","ifacehcjiaacba","gfae","gjbbagdgbhhddibe","cfjfdga","iafagghbjda","bjeb","gbijeecedf","bgbcfhi","jicac","gded","efgedfbb","idbdajdfcfeijf","gfeiafhae","digbajejb","ihjib","biefdigdidgh","fedecff","iebjigi","ebaijieebhiigbd","hjaciabbhfc","edgbh","gaejdc","gd","aebbcbfehgdc","cbjjigjgia","dchjjicjghdfagdha","aghaggebjbbdj","afhdhj","ecajjbigfgeiejdfgjf","bfcfjhje","ejd","becbccdffhjiha","ahcd","hjgfedcda","acdd","chfiec","fajhfdfhcgj","ac","i","jcbeghfbgjiib","jechhf","idcgadh","dijgdgejigjgjbife","bajcdfjgifcf","ehcccbifhbbci","gggbdfafcjaa","fiijfiffbeeafhidgdh","fjhijj","bifghffcha","cfjd","ibhgf","ifiggeedafjcgbdfbe","bjhagccefjahchdjidh","gchdjdacih","jcgdad","ecegiahjb","dgf","hhejeejjfgd","igiedc","faffaae","hhhdagegjjhadcfdb","djdedaibedhhhad","agjcdbgciadghfg","jhgiachghef","ib","jhaaidgiajbfc","jegcdbhecb","eiabgbieiahegjfdfcha","dgcae","jgdcaehgeffjdhdhd","gjjc","jbbgagji","cdfgbjeeihhejcabih","ahdhahadadje","eeegecddajiiadahbhe","baffhiihfgifhca","cbjgfbbbe","bihgfhfadjgfde","jahhbfdijbfffh","igcgj","cghdcabgehjcie","cghgaiajdj","if","fjbdgidbibhdif","hhbcaa","aabfgeic","ahd","ggfhahfgbjbhhii","abaiiegibg","abajjhadbfgg","fibcgafjibacaegfbhaa","jaagdjaciefgjjdfje","bgeah","diei","gifcfffedcejdhgid","dbi","ahbicbaded","iegdccicigfeajagibj","afg","dgh","cjijdcccaebici","afge","eciih","bfgcdjdfegac","cbfhcbhfbcfiajd","feibbfceedecadaiabb","ccafdfcag","bbbei","jbbhff","fhg","cibcfhejhbhhjhfhbadh","jgadaibddggajjegh","ghahacag","jbjcbbigdjh","dfihbj","cieieciffbdgef","adcgifdcjdejbebi","ccichece","hhaej","ijidfjajjgaeigiea","fd","df","jjfebghacicgadeec","chjdj","jdabejje","cadadjchbbehgfgiecaa","hcddhecbeb","ijjbhai","ggjfdijhfh","ageggjfibgeda","bcgdceggbebbfd","bjbbcbihfj","eeaf","iaic","hhiibebjdbgheihaigff","eeiedaibajgjcfga","gchgfdjiaedfgacdjgad","hjhbiehiig","b","geajijdebcajgfe","ei","idjaefi","id","bhdfdbcd","hggd","ghiigj","aihfdggfadaeiihbb","jbegid","cfigdibdgidg","bajfgbjadadhefgbjh","afac","ff","aideabecjcchbcfhhc","bdcafbaehafhahfde","cgfiheejaidj","bigeejbjgec","dag","giifhbgdgjbhcaaeiife","ijgfcffgadechijj","ieigcdc","egagfdfabihe","fiifbcd","jcccjjfciea","dge","dgeff","dfecjhciahh","cjbdjiegjfcbcfhbfhg","dcecedaeeebegf","hjbhgecb","cjbdefegfebchgc","jeiaefjbicgbdihi","hhcfbiefbbcj","eg","igeghceahe","hh","iighhghicbigaji","ihcadidcbcfgaajahj","igdjd","iebijhjdieffd","cfjdiiaaeichciie","bidigjaebbcacigh","eeahciab","edhjchcdc","gieifhhjejgdajgdigcd","ibehahbigijgcbbehcaj","gde","cccijcadiadbcfccj","hdfbejfefcaeigdehdhj","hbchgdjjd","ihhba","ffjbjeajcfha","adbadbediddah","gcfadicdjdfjddhgjd","chjjajcgfjefh","egchcdeffbbjjhbfgjgj","aahfjd","hdhjaieeidj","iechgceeiah","bichjfbigeha","jjibfgfcejfhjef","hhajabbihdif","fjcbjbbhja","cjejddjbdjfffdga","biaeiehc","edihagfihjdbefhihg","afj","bdhhjjhfjjbdd","bighfgcig","fhbjfaadgdhfibcahi","fidhdiicigchdgcajbc","ibccefcfbccdbebaifb","cdii","feibajadhijfheifbaj","babjhchg","ibhjajjgh","ajfbh","bachehagcgadbichcic","bjgiedhcahaifg","ijahacfe","jcghdcgdjjh","bfhagjcidehgahehbd","egegajidchfdjdgdfcc","f","cd","hijd","eideajaaecb","hjiaefdaeabiehdjede","jdgfcbehibieehdc","jfb","aeiiaifhedgccegbabg","ijihcejf","aejadfbedae","fdjfbcfafjcbf","bejjjcfd","aicabca","fa","ihbef","hjej","gfihebacjfdaei","dcbjcighgjgh","fefhhihcb","dbfgjcabfa","cadhjhhgiffghffgajd","dibhdbbcbah","cidhgegcabfbdibjhef","gb","bificfaeghfcjfg","faadefidbdjcebhg","behfe","ghgdhgjeid","ghjhihdcadffaege","acigfegdcjhgj","dfajaecjdajiihjdc","ajefgebgefahbjbffej","fceia","jihifjchehec","ifcghhhhchcfdad","eegagcjbdhc","jfdijjahefdcihfaf","chdbbfaedhh","cg","cfijhhcbijaacdbi","hc","ceddhbg","ahehcdehdbbciee","geeiaeibfjceajh","jhbefdjgj","cbgb","bgd","bd","bjaafbacedf","jfjcbg","ihjaedfcadbi","ghhaidbghhba","aegdgcj","afeccafcfcaifcf","icheehijijc","cadabegjjj","ddfciaajcabefda","cb","ihgeeh","ajiadfhcacjfdifcib","dchahahcdegcc","hi","aihjfddibcihdh","gdacjbfgde","cfeeidaf","ejehdic","bbcfgighcb","giieiicfcfaa","aai","fgahai","efjiiaiehbjhjafhdhb","edghhjiddecieec","ej","he","hb","ead","hidjghcijb","ibcbf","ifdehfhcajfiebbaj","ace","gbhf","bbihdhhc","hbbafdhcbef","jfcbe","cjebbhaifdbbib","ieeeejjacicjhddcch","chihgddjfga","hfhii","ce","bhi","aidejahh","jahfdehgbagddfjc","ijicebfeeeja","gfffadhedihdaecfbde","efffibiifhbffh","agchjcghjffjceaa","eehafabifjicfb","dgfigibd","bjibgdhiedhgdbgjhce","eijacdjadaigchchfeee","gfdhfchgiedcadcjajih","gjiej","iaibcaebeabddaciba","dbibcegdggihfhfcef","jiffdecbdjejjcgh","cffdbjceabbgfi","gifha","ghiieajjai","cghijdicbjed","adddggafj","iiafejjcggdeeef","beicaaicdhfdhbjj","dccjfaaiiefhh","heihghdgaafhjfac","behidid","jjbhbdeabbagdfcb","ebgaiggafciebaea","bagj","hhdefjdaiiigieaed","dhebhefbhciciecihee","dg","bcbcgagjaijbbdb","ahdajhhcedb","ii","fjgbhjhccjgecjgh","cgdjehhedec","hjdfaaadfbaggd","dfd","cfaeeegiihi","jahegibjabf","icbii","iibj","hdjfbgd","hfaichbdfjhcbfjabc","ibaghgciec","abgjcafbbbg","idjehihcbfhihbdgbi","begachciadfdadbhb","biiaghdigaab","egjfg","bdji","bfdebfba","jdfhfcdjjgdfjahefgij","hfbiedicieccbdjhjdj",
"jeecejjiijgjdcifd","gibbhicheadcg","bfhjhhfcdcgbhjhbhgef","hadfbgdih","eehhcdej","hchae","eggd","dicg","aafgfhffdedghjajfdh","gcfjhgfcdhgieiibff","hjchbbdgdedfechebge","jceii","bdggccdhhdb","cfehhdcbj","hcbfdfcbdiiaah","bjhgeeccjib","hdaiedigd","eahjifhjd","fcgega","jcbcehcgeebe","ggbgaebfibdejafbaeeb","fcigbhdddbg","eecfhghc","jdbehehjfdijejahbfdf","cja","eiaaagcbjec","cbhcch","jhhagfjji","hgcbbhfgedfaiehgj","hceigehdejdd","cgdhdbiejihic","cgbihcdhgecjjaec","fdahfa","h","ijagaceheie","hbeifcfibffcgj","edfddjb","aaffahhajdeaafajed","jfdfbjiifjeabcjbhj","egcaba","ijie","giaaibag","iabhh","cjeheeafg","fccijfdgdcfhdc","hhhj","bccbhdgejhaggfhgccce","gbj","giffhifehhj","afacd","gchgbidjb","fbjbfdicha","jgh","ibiihciggjd","aaijjgfajifgadbd","cje","jhggafbhehbdhfedia","gcjijhfgfigjhc","igihhdificbj","ef","aeaighghbafjei","jbbehagfcc","jdgbhgbag","jhj","fhibchdcgijfbhabejcc","eiaghab","hggcbechfii","gcjfjfddgehjhehe","efbcaiidaejgccbij","fdecchgedgf","ebhdeifbedffaib","fadeiddecchhejibfhje","gjhfc","cdijhcab","geedadifhchhdibgbech","jjjchdi","hbgecedhjcecic","difffebbhiihihedj","cjgfbjchhceddbbgd","eacgf","gcafbdbibbchbhijcbi","iagjiigdfibccjg","gcaffeeejcbiefjaga","dfjcg","jcaf","cjgce","jj","abegabdeffbj","badfj","jggijgicidbbddhd","adc","bgeajdjbaeja","cabi","ehbagjgebjhhehhjbf","jaabgcbfei","acgehebbc","bgjagc","hjahgeedhieehdjbcjd","ijeabhici","ehgiejdefhdehi","gdedeegfdhdbd","cjjceib","gajfdaigdjdgi","bfdaegbeaehadefg","digaai","jgicbadgebdjifjghg","heaadfghjjadce","bahbedgbjifcechc","hfgag","eeaegca","bacechahejggagfibcia","gdiif","dbhhe","dfehgeaiafbf","dhahcc","chh","ejfbeiggdcaigidhdbdb","agfjcfbeejgibefeaeh","jgghgedceegcbhfagh","efdjdffaiehijfbi","cafggjaedcf","adbihiggjjeeebg","fajicbf","hjjahdbjfggdf","gfdgabhficb","bgejhidib","dihc","ghagdddjbdaegdbihcf","efg","gedfhcgcafcfhajei","dfdchhgfebfjcbdi","fehajg","ajafecgea","gifdfia","ad","ceficegbgaabd","dbbgdjhjdjehae","djbhjiaejbdgaadcbjgi","ifjacjgdedheeb","afcdagacg","gjfbdjbgeaejj","jjdeaca","cgccafhgiegag","edhgbjjffcadhjhc","hfcgeaibabaeedc","bhjaheageef","ggcadhdjbceicji","gbebic","fdjcadcei","eadcc","jgefihheiajfjegebcb","bfijdaeijiebiihj","bgfbfggaebghidbaeij","hbfijfcechdib","jcacf","fbecigeedcbehib","hdeeaafahj","eciiehedaffajeeehgcc","bidiafidhhiehejfg","djadbeaciigehgahachc","gbh","feiegfc","habfaeaibhdbf","hbcgfaecde","faabcidhegi","giafjfbahjca","fefifjcadfji","gaicb","fhcgabjidj","hcdibbdcgfhggi","dfjghdffjejfehccddc","hhhgfaibbj","ediejhggcgadfbifbce","gdbgjhdhdbeggc","gj","jddjadfhh","jhigbbdiej","ageddiiic","jchidcbijcaiaa","biaaijffgdfhhfdcfgb","ejhgb","eabfhbb","jggcacagaafcd","iaedgbgbfccjejhe","gggcj","baahcfbfgcbadecci","acdehbehgdiahecbigjg","cjcdabedjajc","jbfgi","eedejcf","ejciaaib","ifidhaac","habgebdefibhfi","daacbgieijajefaafbh","ffffaeac","cjhdbfghfhefecichac","iiegeghedejbifbbjbaj","cijaajbfff","eb"]))
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)