#include <stdio.h>

int main()
{
	
	int dep, with;
   	int tposo=0;
    int choise, quit = -1;
	while(choise != -1){
	
	printf("WELCOME!");
	printf("how can we help you: \n");
	printf("1)deposit: \n ");
	printf("2)withdraw: \n");
	printf("3)view my remaining balance: \n");
	printf("or give -1  to quit\n ");
	printf("press 1 for deposit\n ");
	printf("press 2 for withdrawal\n ");
	printf("press 3 for remaining balance \n");
	scanf("%d", &choise);
		
	
	    switch(choise)
		{
			case 1:   
		        printf("give your amount of deposit: \n");
				scanf("%d",&dep);	
		     if(dep>5)
				{
					
		              tposo += +dep;
		              tposo++;
		              printf("deposit completed!\n");
		              printf("your new balance is: %d\n", tposo);
		              printf("press -1 if you want to quit");
		              scanf("%d",&quit);
		              break;
		               } 
		       case 2:
		    	       printf("give the amount of your withdraw: \n");
		    	       scanf("%d",&with);
		       if(with<20)
		               {
		    	        printf("your remaining balance is: %d", tposo);
		    	        printf("you cant withdraw!\n");
		    	        break;
		    	       }
		       else if(with>=20)
			       {
				tposo=dep-with;
				printf("your remaining balance is: %d\n", tposo);
				printf("press -1 if you want to quit");
		                scanf("%d",&quit);
				break;
			       }
		        case 3:
			        printf("your remainng balance is: %d\n", tposo);
				break;
			    
	      }
       }   
return 0;	   
}
		
	


/*for some reason the final balance after the deposit is the amount of deposit +1 */	

/*thelw na valw parapanw epilogesvopws na mporei na epilegei o xrhsths thn
analhpsh thn katathesh kai thn provolh ypoloipou epishs kai thn epilogh eksodou 
apo to programma*/
