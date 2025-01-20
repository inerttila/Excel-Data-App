// ==UserScript==
// @name         Modify Amount and Date/Time Display
// @namespace    http://tampermonkey.net/
// @version      2025-01-17
// @description  Modify the displayed amount and date/time on the page
// @author       You
// @match        https://stake.com/transactions/deposits
// @icon         https://www.google.com/s2/favicons?sz=64&domain=stake.com
// @grant        none
// ==/UserScript==

(function () {
  "use strict";

  // Function to modify the amount
  function modifyAmount() {
    const amountElement = document.querySelector(
      "td.table-cell-item div.row-wrap div.col div.currency span.content > span.weight-normal.line-height-default.align-left.size-default.text-size-default.variant-subtle.numeric.with-icon-space.is-truncate.svelte-17v69ua"
    );

    if (amountElement) {
      amountElement.textContent = "21.21111"; // Update the amount
    } else {
      console.warn("Amount element not found, retrying...");
    }
  }

  // Function to modify the time and date
  function modifyTimeAndDate() {
    const dateTimeElement = document.querySelector(
      "td.table-cell-item div.row-wrap div.col.header-stack"
    );

    if (dateTimeElement) {
      dateTimeElement.textContent = "13:15 8/21/2021"; // Update the time and date
    } else {
      console.warn("Date and time element not found, retrying...");
    }
  }

  function modifyContent() {
    modifyAmount();
    modifyTimeAndDate();
  }

  document.addEventListener("DOMContentLoaded", () => {
    modifyContent();

    const observer = new MutationObserver(() => {
      modifyContent();
    });

    observer.observe(document.body, { childList: true, subtree: true });
  });
})();
