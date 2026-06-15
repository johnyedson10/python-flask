## Preciso cadastrar contas

data_venc --> 20-jun-2026
data_pag  --> 21-jun-2026
descricao --> conta de energia
valor     --> 200,00
status    --> select 1-Pago, 2-Pendente, 3-Vencido

## Exemplos

<input name="descricao" type="text"   required />
<input name="valor"     type="number" required />
<input name="data_venc" type="date"   required />
<input name="data_pag"  type="date"   required />

<select name="status"> 
    <option value="pago"> Pago </option>
    <option value="pendente"> Pendente </option>
    <option value="vencido"> Vencido </option>
</select>