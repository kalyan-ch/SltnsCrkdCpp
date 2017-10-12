#include <iostream>
#include "LinkedList.h"

using namespace std;

LinkedList* addNumbers(LinkedList* ll1, LinkedList* ll2){
	int len1 = ll1->listLength();
	int len2 = ll2->listLength();

	if(ll1->head==NULL || ll2->head==NULL){
		return NULL;
	}

	if(len1>len2){
		ll2->padList(len1-len2);
	}else{
		ll1->padList(len2-len1);
	}


	LinkedList* final = new LinkedList();

	int carry = 0;
	Node* n1 = ll1->head;
	Node* n2 = ll2->head;

	while(n1!=NULL || n2!=NULL){
		int num1 = n1->data;
		int num2 = n2->data;
		int num3 = num1 + num2 + carry;
		if(num3 > 9){
			num3 = num3%10;
			carry = 1;
		}else{
			carry = 0;
		}
		final->addNode(num3);

		n1 = n1->next;
		n2 = n2->next;
	}

	if(carry!=0){
		final->addNode(carry);
	}

	return final;

}


int main(){

	LinkedList* ll1 = new LinkedList();
	LinkedList* ll2 = new LinkedList();

	ll1->addNode(7);
	ll1->addNode(9);
	ll1->addNode(2);
	ll2->addNode(3);
	ll2->addNode(0);
	ll2->addNode(7);
	ll2->addNode(5);

	cout << "adding numbers" << "\n";

	LinkedList* sum = addNumbers(ll1,ll2);
	if(sum!=NULL){
		cout<< "the sum is" << "\n";
		sum->printList();
	}



	return 0;
}
