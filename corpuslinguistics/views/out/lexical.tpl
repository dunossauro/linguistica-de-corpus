<html>
{% include 'main_view.tpl' %}
   <body>
     <h1>{{ name }}</h1>
     <table>
        <tr><th>Word</th><th>Count</th></tr>
        {% for row in rows %}
        {% set x = row.split() %}
        <tr>
            <td>{{ " ".join(x[0:2]) }}</td>

            <td>{{ x[-1]}}</td>
         </tr>
        {% endfor %}
     </table>
</body>
