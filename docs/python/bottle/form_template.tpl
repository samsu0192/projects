<!DOCTYPE html>
<title>Break up sentence</title>
%if show_form:
<form action:"/" method="post">
	<label for ="sentence">Input a sentence to break up</label>
	<input type="text" name="sentence" />
</form>
%else:
Sentence parts:<ol>
%for part in parts:
	<li>{{part}}
%end
</ol>
%end
