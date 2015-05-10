Caesar Cipher
==============

.. automodule:: algopy.caesar
   :members:

That is how the cipher logic gets executed.   
   
.. code-block:: python
   :linenos:

	def __cipher_helper(message, key):
		cipher_text = ""
		for each_char in message.lower():
			char_pos = string.ascii_lowercase.find(each_char)
			if char_pos == -1:
				cipher_text += each_char
				continue
			else:
				char_pos = (char_pos + key) % 26
				cipher_text += string.ascii_lowercase[char_pos]
		return cipher_text