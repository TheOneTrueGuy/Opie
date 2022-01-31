import openai
#import ipywidgets as widgets
import json
import  argparse
parser = argparse.ArgumentParser(description='Rounder')
parser.add_argument('--api_key', type=str, default='', help='OpenAI API key')
parser.add_argument('-o', '--output', type=str, default='test.txt', help='Output file')
parser.add_argument('-i', '--input', type=str, default='input.txt', help='Input file')
parser.add_argument('-t', '--type', type=str, default='slidingWindow', help='Type of input')
parser.add_argument('-p', '--prompt', type=str, default='the secret to time travel is', help='Prompt')
parser.add_argument('-s', '--seglen', type=int, default=3, help='Segment length')
args=parser.parse_args()
out=args.output
type=args.type
input_file_name=args.input
prompty=args.prompt
seglen=args.seglen
myTokens = 600
myEngine = "davinci"
myTemp = 1.18
myTop_p = 2
myN=4
myStream = None
myLogProbs = None
myStop = "Human:"



openai.api_key = "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"
#ynput=input("Enter your prompt: ") #"Time crystals can be made by" #
#make new list from ynput split on commas,
#lyst=ynput.split(",")
#print(lyst)
#myPrompt=lyst[0]
#print(myPrompt)

#myTokens = int(lyst[1])
#myEngine = "davinci"
#myTemp = float(lyst[2])
#myTop_p = int(lyst[3])
#myN=int(lyst[4])
#myStream = None
#myLogProbs = None
#myStop = "Human:"

dontstop=True
#function to get text: object string from json formatted string/object
def stringfromjson(jsonstr):
    return json.loads(jsonstr)["text"]

#response = openai.Completion.create(engine="davinci", prompt= myPrompt, max_tokens=48)
#z=response.choices[0]
#y = json.loads(str(z))
#text=y["text"]

def loopJam1(myp):
    myPrompt=myp
    dontstop=True
    while dontstop:
        response = openai.Completion.create(engine="davinci", prompt= myPrompt, max_tokens=48)
        z=response.choices[0]
        y = json.loads(str(z))
        reply=y["text"]
        with open(out,'a') as f:
            f.write(myPrompt)
            f.write('\n')
            f.write(reply)
        print(reply)
        ynput=input("Enter your prompt: ") #"Time crystals can be made by" #
        #make new list from ynput split on commas,
        lyst=ynput.split(",")
        print(lyst)
        myPrompt=lyst[0]
        print(myPrompt)

        myTokens = int(lyst[1])
        myEngine = "davinci"
        myTemp = float(lyst[2])
        myTop_p = int(lyst[3])
        myN=int(lyst[4])

        if myPrompt=="stop":
            dontstop=False

        
#loopJam1()

# function to open text file, read it in close the file and return a string
def readFile(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text




def slidingWindowParaphrase(fyl, seglen):
    phrase=readFile(fyl)
    #break phrase up into a list of words
    words=phrase.split()
    # a for loop to iterate through the number of words minus 3
    para=""
    for i in range(len(words)-seglen): #range(120):#
        
        #get three words from the list starting at i
        threeWords=words[i:i+seglen]
        #join the three words together
        threeWords=" ".join(threeWords)
        response = openai.Completion.create(engine="davinci", prompt= threeWords , max_tokens=4)
        z=response.choices[0]
        y = json.loads(str(z))
        reply=y["text"]
        print(reply)
        #concatenate reply to para
        para=para+reply+" "


        
    return para


# main function, if main, run either sliding window paraphrase or loopJam1
if __name__ == "__main__":
    if type=="slidingWindow":
        para=slidingWindowParaphrase(input_file_name, seglen)
        print(para)
        #save para to output file
        with open(out,'a', encoding="utf-8") as f:
            f.write(para)
    else:
        loopJam1(prompty)

        
    

#with open('backnforth.txt','ab') as f:
#        f.write('koko')