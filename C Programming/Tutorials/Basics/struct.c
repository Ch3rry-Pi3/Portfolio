#include <stdio.h>
#include <string.h> // For string handling

/*
 * This program demonstrates the use of structs in C.
 * Examples include:
 * - Defining a struct `Person` with attributes.
 * - Creating and modifying struct instances.
 * - Passing structs to functions (by value and by reference).
 */

// Step 1: Define a struct for a Person
struct Person {
    char name[50];
    int age;
    double salary;
};

// Function prototype to display a person's details
void displayPerson(struct Person p);

// Function prototype to update a person's salary (pass by reference)
void updateSalary(struct Person *p, double newSalary);

int main() {
    // Step 2: Creating struct instances
    printf("=== Creating Persons ===\n");
    struct Person person1 = {"Alice Johnson", 30, 50000.0};
    struct Person person2;
    
    // Assign values to person2
    strcpy(person2.name, "Bob Smith");
    person2.age = 45;
    person2.salary = 60000.0;

    // Step 3: Display details
    displayPerson(person1);
    displayPerson(person2);

    // Step 4: Updating salary using a function (pass by reference)
    printf("\n=== Updating Salary ===\n");
    updateSalary(&person1, 55000.0);
    updateSalary(&person2, 65000.0);

    // Step 5: Display updated details
    displayPerson(person1);
    displayPerson(person2);

    return 0; // Indicate successful execution
}

// Function to display a person's details
void displayPerson(struct Person p) {
    printf("\nPerson Details:\n");
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Salary: %.2f\n", p.salary);
}

// Function to update a person's salary (modifies original struct using pointers)
void updateSalary(struct Person *p, double newSalary) {
    p->salary = newSalary; // Use -> to access struct members via pointer
    printf("%s's salary updated to %.2f\n", p->name, p->salary);
}
