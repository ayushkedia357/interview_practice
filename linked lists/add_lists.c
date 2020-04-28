#include<stdio.h>
#include<stdlib.h>
typedef struct node{//defining node
	int val;
	struct node* next;
}node;
void insert(node** head,int a,int pos){
	//printf("poiuy");
	node* temp=(node*)malloc(sizeof(node));
	node* temp1=*head;
	temp->val=a;
	temp->next=NULL;
	if(*head==NULL){
		//printf("poiuy");
		*head=temp;
	}
	else if(pos==1 && *head!=NULL){
		temp->next=temp1;
		*head=temp;
		return;
	}
	else{
		int t=1;
		while(t<pos-1){
			temp1=temp1->next;
			t++;
		}
		temp->next=temp1->next;
		temp1->next=temp;
	}
	return;
}
void print_list(node *head){
	//printf("%d",head->val);
	node* temp=head;
	while(temp!=NULL){
		printf("%d ",temp->val);
		temp=temp->next;
	}
	return;
}
void add(node** head,node **head1){
	node* temp1=*head;
	node* temp2=*head1;
	node* head2=NULL;
	int carry=0,i=1,sum=0;
	while(temp1!=NULL && temp2!=NULL){
		sum=carry+temp1->val+temp2->val;
		//printf("%d ",sum);
		insert(&head2,sum%10,i);
		carry=sum/10;
		i++;
		sum=0;
		temp1=temp1->next;
		temp2=temp2->next;
	}
	while(temp1!=NULL){
		sum=carry+temp1->val;
		insert(&head2,sum%10,i);
		carry=sum/10;
		i++;
		sum=0;
		temp1=temp1->next;
	}
	while(temp2!=NULL){
		sum=carry+temp2->val;
		insert(&head2,sum%10,i);
		carry=sum/10;
		i++;
		sum=0;
		temp2=temp2->next;
	}
	if(carry){
		insert(&head2,carry,i);
	}
	print_list(head2);
	return;
}
int main(){
	node* head=NULL;
	node* head1=NULL;
	int a,l=0,pos,ll=0;
	//printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
	int choice;
	while(1){
		printf("enter 1=>insert	2=>For 2nd list  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
		printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>l){
			printf("invalid input");
			continue;
		}
		insert(&head,a,pos);
		l++;
	}
	print_list(head);
	while(1){
		printf("enter 1=>insert	2=>for adding the lists  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
		printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>ll){
			printf("invalid input");
			continue;
		}
		insert(&head1,a,pos);
		ll++;
	}
	print_list(head);
	print_list(head1);
	add(&head,&head1);
	return 0;
}
