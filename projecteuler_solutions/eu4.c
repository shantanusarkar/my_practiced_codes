//Q. A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//   Find the largest palindrome made from the product of two 3-digit numbers.
//Date: Mar 8, 2013
//Author: Shantanu Sarkar

#include<stdio.h>
int ispalindrome(int a)
{
	int w,x,y,z,b,c,d,e;
	w=a;
	x=w%10;
	w=w/10;
	y=w%10;
	w=w/10;
	z=w%10;
	w=w/10;
	b=w%10;
	w=w/10;
	c=w%10;
	w=w/10;
	e=w%10;
	w=w/10;
	d=(x*100000)+(y*10000)+(z*1000)+(b*100)+(c*10)+e;
	if(d==a)
		return(0);
	else
		return(1);
}
void main()
{
	int i,j,result=0,prod,x;
	for(i=100;i<1000;i++)
	{
		for(j=100;j<1000;j++)
		{
			prod=i*j;
			x=ispalindrome(prod);
			if(x==0&&result<prod)
				result=prod;
		}
	}
	printf("The highest three digit palindrome is %d",result);
}
