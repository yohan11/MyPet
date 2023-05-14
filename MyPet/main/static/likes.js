function increaseLike(e) {
	id = e.classList[0];
	var likes_num = document.getElementById(id + "-likes-num");
	likes_num.textContent = parseInt(likes_num.textContent) + 1;
	console.log(likes_num.textContent);
}
