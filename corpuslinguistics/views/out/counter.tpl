<html>
{% include 'main_view.tpl' %}
   <body>
     <h1>{{ name }}</h1>
   </br>
     <table>
        <tr>
          <th>Word&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>Count</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>

            <td>{{ rows[row]}}</td>
         </tr>
         {% endfor %}
     </table>
</body>
