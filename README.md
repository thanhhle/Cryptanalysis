# Cryptanalysis
An application written in Python



## Description:
This assignment is designed to allow you to get some practice with cryptanalysis of substitution ciphers. Write a program that decrypts the following encrypted quotations. You may use any programming language that you like for your submission, but I recommend using something that makes text manipulation easy, like Python.
  1. fqjcb  rwjwj  vnjax  bnkhj  whxcq  nawjv  nfxdu  mbvnu  ujbbf  nnc
  2. oczmz  vmzor  jocdi  bnojv  dhvod  igdaz  admno  ojbzo  rcvot  jprvi  oviyvaozmo  cvooj  ziejt  dojig  toczr  dnzno  jahvi  fdiyv  xcdzq  zoczn  zxjiy
  3. ejitp  spawa  qleji  taiul  rtwll  rflrl  laoat  wsqqj  atgac  kthls  iraoatwlpl  qjatw  jufrh  lhuts  qataq  itats  aittk  stqfj  cae
  4. iyhqz  ewqin  azqej  shayz  niqbe  aheum  hnmnj  jaqii  yuexq  ayqkn  jbeuqiihed  yzhni  ifnun  sayiz  yudhe  sqshu  qesqa  iluym  qkque  aqaqm  oejjs hqzyu  jdzqa  diesh  niznj  jayzy  uiqhq  vayzq  shsnj  jejjz  nshna  hnmyt isnae  sqfun  dqzew  qiead  zevqi  zhnjq  shqze  udqai  jrmtq  uishq  ifnun siiqa  suoij  qqfni  syyle  iszhn  bhmei  squih  nimnx  hsead  shqmr  udquq uaqeu  iisqe  jshnj  oihyy  snaxs  hqihe  lsilu  ymhni  tyz

Additionally, you must write a second program that takes the following phrases and encrypts them using a substitution cipher. Your second program should ask for a key and a phrase and then proceed to encryptthat phrase using the given shared key. Make sure that you give me the key for the cipher that you use andthe output of encrypted phrases.
  1. He who  fights  with  monsters  should  look to it that he  himself  does  not become a monster. And if you  gaze  long  into an abyss , the  abyss  also gazes  into  you.3.  Whenever I find  myself  growing  grim  about  the  mouth; whenever  it is adamp , drizzly  November  in my soul; whenever I find  myselfinvoluntarily  pausing  before  coffin  warehouses , and  bringing  up therear of every  funeral I meet; and  especially  whenever  my hypos  getsuch an upper  hand of me , that it  requires a strong  moral  principle  toprevent  me from  deliberately  stepping  into  the street , andmethodically  knocking  people ’s hats  off - then , I account  it high  timeto get to sea as soon as I can.
  2. There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.
  3. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can.

## Result:
#### Decrypting Ciphertext to Plaintext:
    Ciphertext: 
    fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc

    Plaintext: 
    whatsinanamearosebyanyothernamewouldsmellassweet
  -----------------------------------------------------------------------
   
    Ciphertext: 
    oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy

    Plaintext: therearetwothingstoaimatinlifefirsttogetwhatyouwantandafterthattoenjoyitonlythewisestofmankindachievethesecond
  -----------------------------------------------------------------------
  
    Ciphertext:
    ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae

    Plaintext: contrariwisecontinuedtweedledeeifitwassoitmightbeandifitweresoitwouldbebutasitisntitaintthatslogic
  -----------------------------------------------------------------------
  
    Ciphertext:
    iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz

    Plaintext: sohewaxesinwealthnowisecanharmhimillnessoragenoevilcaresshadowhisspiritnoswordhatethreatensfromeveranenemyalltheworldwendsathiswillnoworseheknowethtillallwithinhimobstinatepridewaxesandwakeswhilethewardenslumbersthespiritssentrysleepistoofastwhichmastershismightandthemurderernearsstealthilyshootingtheshaftsfromhisbow
    
#### Encrypting Plaintext to Ciphertext:
    Key: tkrqcujmhebdpnlwvifsyaxzgo
  -----------------------------------------------------------------------
    Plaintext: 
    He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you.

    Ciphertext: mcxmluhjmsfxhsmplnfsciffmlydqdllbslhssmtsmcmhpfcduqlcfnlskcrlpctplnfscitnqhuglyjtocdlnjhnsltntkgffsmctkgfftdfljtocfhnslgly
  -----------------------------------------------------------------------
    Plaintext: 
    There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.

    Ciphertext: smcichftsmcligxmhrmfstscfsmtshucacitngklqgqhfrlacifcztrsdgxmtssmcynhacifchfulitnqxmghshfmcichsxhddhnfstnsdgqhftwwctitnqkcicwdtrcqkgflpcsmhnjcacnplickhotiictnqhnczwdhrtkdcsmcichftnlsmcismcligxmhrmfstscfsmtssmhfmtftdictqgmtwwcncq
  -----------------------------------------------------------------------
    Plaintext: 
    Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can.

    Ciphertext: xmcncacihuhnqpgfcdujilxhnjjihptklyssmcplysmxmcncacihshftqtpwqihoodgnlacpkcihnpgflydxmcncacihuhnqpgfcduhnaldynstihdgwtyfhnjkculicrluuhnxticmlyfcftnqkihnjhnjywsmcictilucaciguyncitdhpccstnqcfwcrhtddgxmcncacipgmgwlfjcsfyrmtnywwcimtnqlupcsmtshsicvyhicftfsilnjplitdwihnrhwdcslwicacnspcuilpqcdhkcitscdgfscwwhnjhnslsmcfsiccstnqpcsmlqhrtddgbnlrbhnjwclwdcfmtsfluusmcnhtrrlynshsmhjmshpcsljcsslfcttffllntfhrtn
