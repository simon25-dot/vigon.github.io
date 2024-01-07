document.addEventListener('DOMContentLoaded', function() {
          const Orders = [
            {
              WebsiteType: 'E-commerce',
              daystaken: '40days',
              status: 'Due',
              payment: 'Pending'
            },
            {
              WebsiteType: 'Business',
              daystaken: '55days',
              payment: 'Refunded',
              status: 'Declined'
            },
            {
              WebsiteType: 'Blog',
              daystaken: '3days',
              payment: 'Paid',
              status: 'Active'
            },
          ];
        
          Orders.forEach(order => {
            const tr = document.createElement('tr');
            const trContent = `
              <td>${order.WebsiteType}</td>
              <td>${order.daystaken}</td>
              <td>${order.payment}</td>
              <td class="${order.status === 'Declined' ? 'danger' : order.status === 'Pending' ? 'warning' : 'primary'}">${order.status}</td>
              <td class="primary">Details</td>
            `;
            tr.innerHTML = trContent;
            document.querySelector('table tbody').appendChild(tr);
          });
        });