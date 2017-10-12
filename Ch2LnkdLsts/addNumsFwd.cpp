#include <iostream>
#include "LinkedList.h"

using namespace std;

LinkedList* addNumbers(Node* head1, Node* head2){

	LinkedList* final = new LinkedList();

	int carry = 0;
	Node* n1 = head1;
	Node* n2 = head2;

	while(n1!=NULL || n2!=NULL){
		int num1 = n1->data;
		int num2 = n2->data;
		int num3 = num1 + num2 + carry;
		if(num3 > 9){
			int temp = num3%10;
			carry = (num3-temp)/10;
			num3 = temp;
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
	ll1->addNode(1);
	ll1->addNode(6);
	ll2->addNode(2);
	ll2->addNode(9);
	ll2->addNode(3);

	cout << "adding numbers" << "\n";

	LinkedList* sum = addNumbers(ll1->head,ll2->head);

	cout<< "the sum is" << "\n";

	sum->printList();


	return 0;
}