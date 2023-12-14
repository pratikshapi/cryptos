

 ________  ___  ___  ________  ________  ________  ________  ___  ________
|\   __  \|\  \|\  \|\_____  \|\_____  \|\   ____\|\   __  \|\  \|\   ___  \
\ \  \|\ /\ \  \\\  \\|___/  /|\|___/  /\ \  \___|\ \  \|\  \ \  \ \  \\ \  \
 \ \   __  \ \  \\\  \   /  / /    /  / /\ \  \    \ \  \\\  \ \  \ \  \\ \  \
  \ \  \|\  \ \  \\\  \ /  /_/__  /  /_/__\ \  \____\ \  \\\  \ \  \ \  \\ \  \
   \ \_______\ \_______\\________\\________\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|\|__| \|__|


We have made our own cryptocurrency called buzzcoin, and deployed a contract at
a specified address. The contract contains five functions, which will pay you
some buzzcoin. Your job is to make every function pay you. The number of
buzzcoin you can get is your grade.

Before you do anything. Take a good long look at the contract provided. Make
sure you understand (or even test with truffle since you should know how by
now) what each question does before you attempt. Compile the contract and make
sure that the abi matches. I compiled it with version 0.5.16

When you are ready, here are instructions to run on our blockchain:


1) Install metamask. This is a firefox/chrome extension. Follow through the
setup. Make sure not to also use real crypto with this!

2) Import the key we sent you over canvas messages. Go to import account,
select json, and choose the key. The password for everyone is "buzz". Don't
share your key with other students!

3) Go to expanded view, settings, add custom network, and provide it with the
following:

Network Name: Buzzcoin
RPC URL: http://143.215.130.235:8545
Chain ID: 9090
Currency Symbol: Buzz

4) If everything goes well, metamask will query our blockchain for your
balance, and it should say 1 BUZZ! If is does not say that, then you did
something wrong

5) Now to interact with the contract, you will need the address I deployed it
at, plus the "abi", which is just an interface to functions and definitions

6) Go to eth95.dev, connect to MetaMask at the top left. It will
connect to metamask. You can use this interface to interact with the Buzzcoin contract (also can use Web3.py if you prefer).
You can now find a contract (see 'Add Contract' at the bottom left and use the abi we provided). Before interacting with the contract, also remember to add the contract Address, which we also provided.

7) From here choose which function to run (in the middle/bottom of the screen: 'Functions'). You can also also fill in BUZZ to send on the right ('ETH to send') and click submit to complete the transaction.

You can find a list of all transactions at the following url:

http://cryptolab.gtisc.gatech.edu/buzzcoin

It updates probably every 10 minutes, or longer.

There is an easter egg somwhere. If you are the first to find it, you get 30
BUZZ. If you are the second, you get 15. The third gets 1. Send an email or a
private piazza post to claim your reward.

This is more important for the second part of the project (deployed later) where
whoever has the highest amount of buzzcoin by the end of the semester gets a
full letter grade bonus.

You dont need to know web3, but itll be easier if you do. See examples here:

https://web3py.readthedocs.io/en/stable/examples.html

Our node will respond to any RPC request. See examples here:

https://eth.wiki/json-rpc/API

Finally. one of the questions becomes.... more difficult the more students who
submit it. The first few people who submit the question basically get it for
free. The last person has to do some serious serious work. Hope you read this
and start early ;)

If you want hints on any questions besides on setup, or problem1, you must pay
the tax of one buzzcoin per hint. It may be worth it if my hint helps you get
twenty buzz, and I promise they will be good hints :) Send 1 buzz to

0x1421350ab6660421d2EA4e423a52030c9A19010E

And in your piazza post, send tx info of you paying me >:)

You are not allowed to try to connect to our node, mine, dos, or steal coins
from other students. If you find an unlimited money glitch, let me know before
hand and we will give some bonus, instead of leaving no coins for other
students.

Your deliverables are a list of all your transactions, your final balance (send a screenshot), and
a small writeup of how you solved each question. Enough for us to know you did
it

have fun!
