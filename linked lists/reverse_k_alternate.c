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
void reverse(node** head1,int l,int ll){
	node* temp=*head1;
	node* temp2=*head1;
	int j=0,m=ll,k=ll;
	while(j<=l/ll){
		if(j%2!=0){
			j++;
			while(temp2!=NULL && m>0){
				temp2=temp2->next;
				m--;
			}
			m=ll;
			continue;
		}
		if(m%2!=0){
			m--;
		}
		while(temp2!=NULL && m>ll/2){
			temp=temp2;
			int i=1;
			while(temp->next!=NULL && i!=k){
				temp=temp->next;
				i++;
			}
			int temp1=temp2->val;
			temp2->val=temp->val;
			temp->val=temp1;
			temp2=temp2->next;
			m--;
			k-=2;			
		}
		while(temp2!=NULL && m>0){
			printf("ghgh");
			temp2=temp2->next;
			m--;
		}
		j++;
		m=ll;
		k=ll;
	}
	return;
}
int main(){
	node* head=NULL;
	int a,l=0,pos;
	//printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
	int choice;
	while(1){
		printf("enter 1=>insert	2=>to reverse k alternate elements  \n");
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
	node* head1=head;
	print_list(head);
	printf("\n");
	int k;
	printf("enter value for k:  ");
	scanf("%d",&k);
	int ll=k;
	reverse(&head1,l,ll);
	print_list(head);
	return 0;
}
