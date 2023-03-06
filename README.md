## ERPNext Loyalty Enhancements

#### Installation

Pull the app to your private server

```bench get-app https://github.com/the-bantoo/loyalty_enhancements.git```


Install the app to your site (replace `site-name` with your actual site's name)

`bench --site site-name install-app loyalty_enhancements`

#### Usage

Simply install and process Sales Invoices as usual. 

The app will add a new field `Loyalty Balance` and update the value with the same value found in the Customer profile.

#### Features
- [x] Add loyalty balance to invoices
- [ ] Add balances to any other doctype (request if needed by creating an new issue)

#### License

MIT
