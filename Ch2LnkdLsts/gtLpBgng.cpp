#include <iostream>
#include "LinkedList.h"

using namespace std;

Node* getLpBegng(Node* head){
	Node* result;

	Node* slow = head;
    Node* fast = head;
    
    while(fast!=NULL && fast->next!=NULL){
    	slow = slow->next;
    	fast = fast->next->next;
    	if(slow==fast){
    		break;
    	}   
    }

    if(fast==NULL){
    	result = NULL;
    }

    slow = head;

    while(slow!=fast){
    	slow = slow->next;
    	fast = fast->next;
    }

    result = fast;

	return result;
}


int main(){

	LinkedList* ll = new LinkedList();

	
	ll->addNode(25);
	ll->addNode(12);
	ll->addNode(32);
	ll->addNode(35);
	ll->addNode(73);
	ll->addNode(27);
	ll->addNode(15);
	ll->addNode(42);
	//create a looped linked list
	ll->createCycle();
	
	Node* n = getLpBegng(ll->head);

	if(n==NULL){
		cout<<"There's no loop"<<endl;
	}else{
		cout<<"The loop starts at the node: "<<n->data<<endl;
	}


	return 0;
}




