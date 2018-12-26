#include<stdio.h>
 
int main()
{
   int n, a = 0, b = 1, c, d;
   scanf("%d",&n);
 for ( d = 0 ; d < n ; d++ )
   {
      if ( d <= 1 )
         c = d;
      else
      {
        c = a + b;
         a = b;
         b = c;
      }
      printf("%d\n",c);
   }
 
   return 0;
}
