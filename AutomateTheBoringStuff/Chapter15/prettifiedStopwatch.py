'''
Expand the stopwatch project from this chapter so that it uses the rjust()
and ljust() string methods to “prettify” the output.

Next, use the pyperclip module introduced in Chapter 6 to copy the text output
to the clipboard so the user can quickly paste the output to a text
file or email.
'''

import time,pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
lstOutput = []

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print('Lap #%s: %s (%s)'%(str(lapNum).rjust(4),str(totalTime).rjust(6),str(lapTime).rjust(6)),end='')
        lstOutput.append('Lap #%s: %s (%s)'%(str(lapNum).rjust(4),str(totalTime).rjust(6),str(lapTime).rjust(6)))
        lapNum+=1
        lastTime = time.time()
except KeyboardInterrupt:
    #for some reason my compiler is not catching the keyboard interrupt correctly
    print('\nDone.')
    pyperclip.copy('\n'.join(item for item in lstOutput))
    print('Copied output to clipboard')
