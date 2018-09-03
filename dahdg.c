#include <stdio.h>
 int main()
{
 int q, w, e;
 printf("Please Enter three different values\n");
scanf("%d %d %d", &q, &w, &e);
 if (q > w && q > e) 
{
printf("\n%d is Greater Than both %d and %d", q, w, e); 
}
else if (w > q && w > e) 
{
 printf("\n%d is Greater Than both %d and %d", w, q, e);
 }
else if (e> q && e > w) 
  {
   printf("\n%d is Greater Than both %d and %d", e, q, w);
  }
 else 
  {
   printf("\nEither any two values or all the three values are equal");
  } 
 return 0;
}
