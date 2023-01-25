const requestLike = new XMLHttpRequest();

const postLike = (id, request_user_id) => {
  console.log(request_user_id);
  const url = "/post_like_ajax/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(
    JSON.stringify({
      id: id,
      request_user_id: request_user_id,
    })
  );
};

// 좋아요 누르기
const likeHandleResponse = () => {
  if (requestLike.status < 400) {
    const { id, request_user_id } = JSON.parse(requestLike.response);
    console.log(id, request_user_id);

    const element = document.querySelector(`.post-id-${id} svg`);
    const button_element = document.querySelector(`.post-id-${id}`);
    const count_like_element = document.querySelector(`p.post-id-${id} span`);

    var content = element.getAttribute("data-prefix");

    var count_like = count_like_element.innerHTML;
    console.log(count_like);
    console.log(content);

    if (content === "fas") {
      button_element.innerHTML = '<i class="far fa-heart"></i>';
      count_like--;
    } else {
      button_element.innerHTML = '<i class="fas fa-heart"></i>';
      count_like++;
    }
    count_like_element.innerHTML = count_like;
  }
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    likeHandleResponse();
  }
};

// 댓글 달기
const requestcommentAdd = new XMLHttpRequest();
const commentInput = document.querySelector("input#comment-input");
const commentSubmitBtn = document.querySelector("button.comment-submit-btn");

const commentAdd = (id, user_id) => {
  const text = commentInput.value;
  console.log(text);
  if (text == "") {
    alert("빈 댓글은 만들 수 없어요!");
    return;
  }

  const url = "/comment_add_ajax/";
  requestcommentAdd.open("POST", url, true);
  requestcommentAdd.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestcommentAdd.send(
    JSON.stringify({
      id: id,
      request_user_id: user_id,
      text: text,
    })
  );
};

const commentAddHandleResponse = () => {
  if (requestcommentAdd.status < 400) {
    const { id, request_user_name, text, comment_id } = JSON.parse(
      requestcommentAdd.response
    );

    const newDiv = document.createElement("div");

    const writerP = document.createElement("p");
    writerP.innerHTML = request_user_name;

    const contentP = document.createElement("p");
    contentP.innerHTML = text;

    const deleteBtn = document.createElement("button");
    deleteBtn.innerHTML = "댓글 삭제";
    deleteBtn.setAttribute("class", "post-id-{{post.id}} delete_button");
    deleteBtn.setAttribute("onclick", `commentDelete(${comment_id})`);

    const recommentBtn = document.createElement("button");
    recommentBtn.innerHTML = "답글 달기";

    newDiv.appendChild(writerP);
    newDiv.appendChild(contentP);
    newDiv.appendChild(deleteBtn);
    newDiv.appendChild(recommentBtn);

    comments_container = document.querySelector(".comments__container");
    comments_container.appendChild(newDiv);
  }
};

requestcommentAdd.onreadystatechange = () => {
  if (requestcommentAdd.readyState === XMLHttpRequest.DONE) {
    commentAddHandleResponse();
  }
};

// 댓글 삭제

const requestCommentDelete = new XMLHttpRequest();

const commentDeleteBtn = document.querySelector(`button.delete_button`);

const commentDelete = (comment_id) => {
  console.log(comment_id);
  const url = "/comment_delete_ajax/";
  requestCommentDelete.open("POST", url, true);
  requestCommentDelete.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestCommentDelete.send(
    JSON.stringify({
      comment_id: comment_id,
    })
  );
};

const commentDeleteHandleResponse = () => {
  if (requestCommentDelete.status < 400) {
    const { comment_id } = JSON.parse(requestCommentDelete.response);
    const deleted_comment = document.querySelector(`.comment-id-${comment_id}`);
    deleted_comment.remove();
  }
};

requestCommentDelete.onreadystatechange = () => {
  if (requestCommentDelete.readyState === XMLHttpRequest.DONE) {
    commentDeleteHandleResponse();
  }
};
