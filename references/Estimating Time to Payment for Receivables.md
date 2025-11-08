`Estimating Time to Payment for Receivables`

## **`Context`**

`At Credix, we operate Credipay, a platform that enables Sellers to finance their Buyers (other companies) invoices and anticipate those receivables. We underwrite those receivables and assume credit and liquidity risk on behalf of our clients.`

`Understanding when a receivable will be paid is critical to multiple functions - from collections and credit risk to treasury and asset valuation. Today, most underwriting and monitoring focuses on whether a receivable will be paid, but far fewer tools help us anticipate when that cash will actually land.`

`Yet this time dimension has first-order implications:`

* `It directly affects capital efficiency and liquidity planning;`  
* `It alters how we prioritize collections and monitor portfolios;`  
* `It reframes how we discount and value assets.`

`You are asked to explore how we can predict and understand time to payment using internal asset and company-level data.`

---

## **`Your Task`**

1. **`Estimate time to payment`** `for receivables - given a set of features known at origination. It should be able to estimate time to payment for new unseen receivables.`  
   1. `Feel free to choose the best option given the problem/data, combining ML algorithms and/or business rules if needed.`  
   2. `You should select yourself the appropriate evaluation metric(s) and evaluate your solution. Justifying the reason for choosing it and the evaluation framework used.`  
2. **`Implement`** `the model/business logic in such a way that it can predict the time to payment for new receivables.`  
   1. `The implementation doesn't need to be hosted online, however should be as close as possible to a production environment, with the technology of your choice.`  
3. **`Deliver a concise, decision-oriented summary`** `with the proposed solution, alongside evaluation metrics and business impact.`

`We’re less interested in black-box performance than in clarity of reasoning, signal extraction, and business framing.`

`Feel free to make any necessary assumptions in order to complete the task, clearly stating what those were and the justification for it within your final document/code.`

---

## **`Available Resources`**

[`Google Drive link`](https://drive.google.com/drive/folders/1NVXcmlrsMpW0nGSpj2EJzVSXvTfCMSnl?usp=sharing)

* **`df_assets.parquet`**`: Asset-level data including payment, due dates and face value.`  
  * `Each asset represents a installment or payment to be paid, which is linked to a invoice/order.`  
* **`df_company_data.parquet`**`: Company basic characteristics.`  
* **`df_quod.parquet`**`: Bureau Credit signals (periodically refreshed).`  
* **`glossary.xlsx`**`: Dictionary containing the descriptions of each column in the above datasets.`

`All sensitive fields are anonymised, but keys are consistent across tables.`

---

## **`Deliverables`**

* `All code created to complete the assignment - including data cleaning, modeling, evaluation and implementation. Github preferred.`  
* `A CSV or dataframe of receivables with predicted time to payment.`  
* `A short business summary: what you learned, methodology and business impact.`

---

# **`Timeline`**

| `Time limit` | `9th of November EoD BRT time` |
| ----- | ----- |
| `Send your submission to` | `joao@credix.finance, alexandre@credix.finance, HR@credix.finance` |

