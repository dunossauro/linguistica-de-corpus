<html>
{% include 'main_view.tpl' %}
   <body>
     <h1>{{ name }}</h1>
     <table>
        <tr><th>Word 1 </th><th>Word 2 </th><th>Count</th></tr>
        {% for row in rows %}
        {% set x = row.split() %}
        <tr>
            <td>{{ x[0] }}</td>
            <td>{{ x[1] }}</td>
            <td>{{ x[-1] }}</td>
         </tr>
        {% endfor %}
     </table>
</body>
