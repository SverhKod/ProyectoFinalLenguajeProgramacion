// Diccionario básico de Braille
const brailleDict = {
  a: "⠁",
  b: "⠃",
  c: "⠉",
  d: "⠙",
  e: "⠑",
  f: "⠋",
  g: "⠛",
  h: "⠓",
  i: "⠊",
  j: "⠚",
  k: "⠅",
  l: "⠇",
  m: "⠍",
  n: "⠝",
  o: "⠕",
  p: "⠏",
  q: "⠟",
  r: "⠗",
  s: "⠎",
  t: "⠞",
  u: "⠥",
  v: "⠧",
  w: "⠺",
  x: "⠭",
  y: "⠽",
  z: "⠵",
  " ": " ",
  ".": "⠲",
  ",": "⠂",
  "?": "⠦",
  "!": "⠖",
  ":": "⠒",
  ";": "⠆",
  "'": "⠄",
  "-": "⠤",
  "(": "⠶",
  ")": "⠶",
};

function convertToBraille(text) {
  return text
    .toLowerCase()
    .split("")
    .map((char) => brailleDict[char] || char)
    .join("");
}

// Conversión en tiempo real
const entrada = document.getElementById("entrada");
const brailleOutput = document.getElementById("braille");

entrada.addEventListener("input", function () {
  const text = this.value;
  if (text.trim() === "") {
    brailleOutput.innerHTML = `
                    <span class="text-muted">
                        <i class="bi bi-cursor-text me-2"></i>
                        El texto convertido aparecerá aquí...
                    </span>
                `;
    brailleOutput.classList.remove("active");
  } else {
    const brailleText = convertToBraille(text);
    brailleOutput.textContent = brailleText;
    brailleOutput.classList.add("active");
  }
});

// Función para copiar al portapapeles
function copyBraille() {
  const brailleText = brailleOutput.textContent;
  if (
    brailleText &&
    brailleText.trim() !== "" &&
    !brailleText.includes("aparecerá aquí")
  ) {
    navigator.clipboard.writeText(brailleText).then(() => {
      // Feedback visual
      const btn = event.target.closest("button");
      const originalText = btn.innerHTML;
      btn.innerHTML = '<i class="bi bi-check-circle me-2"></i>¡Copiado!';
      btn.classList.add("btn-success-modern");

      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.classList.remove("btn-success-modern");
        btn.classList.add("btn-primary-modern");
      }, 2000);
    });
  }
}

// Animaciones al hacer scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = "1";
      entry.target.style.transform = "translateY(0)";
    }
  });
}, observerOptions);

// Observar elementos con animaciones
document.addEventListener("DOMContentLoaded", () => {
  const animatedElements = document.querySelectorAll(
    ".fade-in-up, .fade-in-left, .fade-in-right"
  );
  animatedElements.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "all 0.6s ease-out";
    observer.observe(el);
  });
});
