# Stock_News_Alert
## Introduction:-
The objective of this project is to get the latest news of the specified company, which affect the stock 
price. Stock price of any company is heavily affected by news in short term. If stock price is fluctuated 
more than our specified parameters than we get an sms that “why the stock price is fluctuated so 
much”.
## Example:–
On 6 July Tata Motors share price fall by more than 10% between 1 p.m. to 3 p.m.. “The stock suddenly 
came under pressure after the company highlighted that its Jaguar Land Rover (JLR) division will see 
negative earnings before interest and taxes (EBIT) margins in the September quarter (Q2FY21). The 
company has lowered its expectation for JLR due to the global chip shortage issue. The company said 
that chip shortage will be greater in the second quarter in comparison to the first quarter of FY22.” If 
trader can get sms after falling just 1% in 15 min than he can save his profit or can prevent major loss.
## Implementation details:-
In this project, we use three api –
1. Alpha Vantage api – To get stock prices for specified time and company.
2. News api – To get the latest news of specified company
3. Twilio – To get sms on our verified number

To make this project, we firstly make a necessary parameters file. In which we have our company name, 
company symbol, Interval, price difference api related private information. Then we make two files, one 
for Intraday and one for daily. (For security, I hide api key's and mobile numbers by xxxx.)

In our Intraday and daily files,
1. we first import required module and then specify required stock parameters. 
2. Then make a data_list and store the closing price of stock using alpha vantage api.
3. Then we get the absolute difference and % difference between last two closing price for 
specified time period.
4. Then we specify our condition. And store first 3 articles using news api.
5. Lastly we send each article on sms using twilio account.
## Conclusion:-
Using this project, we can track any unexpected news that affect stock price. For example if we use this 
project on Microsoft stock on 14 July and make % difference to 1 then we get following sms –
https://github.com/rajeshkasaniya/Stock_News_Alert/blob/master/Example.jpeg
