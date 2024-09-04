/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    // Initially start it off as the first customer's bank account's value.
    let maxWealth = accounts[0][0]

    // Go through all of the customers and for each customer add all of their bank accounts wealth together. Then, check if the total wealth of all of their bank accounts added together is GREATER than the "maxWealth". If it's greater than the "maxWealth", then set the "maxWealth" to that. If it's not, keep it moving and go to the next customer.

    // [[1,5],[7,3],[3,5]]
    for (let i = 0; i < accounts.length; i++) {
        const customersBankAccounts = accounts[i]
        let customersTotalWealth = 0
        
        for (let j = 0; j < customersBankAccounts.length; j++) {
            const bankAccountValue = customersBankAccounts[j]
            customersTotalWealth += bankAccountValue
        }

        if (customersTotalWealth > maxWealth) {
            maxWealth = customersTotalWealth
        }
    }

    return maxWealth
};