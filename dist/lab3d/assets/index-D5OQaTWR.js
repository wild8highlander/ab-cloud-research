(function(){const e=document.createElement("link").relList;if(e&&e.supports&&e.supports("modulepreload"))return;for(const u of document.querySelectorAll('link[rel="modulepreload"]'))r(u);new MutationObserver(u=>{for(const f of u)if(f.type==="childList")for(const h of f.addedNodes)h.tagName==="LINK"&&h.rel==="modulepreload"&&r(h)}).observe(document,{childList:!0,subtree:!0});function i(u){const f={};return u.integrity&&(f.integrity=u.integrity),u.referrerPolicy&&(f.referrerPolicy=u.referrerPolicy),u.crossOrigin==="use-credentials"?f.credentials="include":u.crossOrigin==="anonymous"?f.credentials="omit":f.credentials="same-origin",f}function r(u){if(u.ep)return;u.ep=!0;const f=i(u);fetch(u.href,f)}})();var ld={exports:{}},nl={};var iv;function LM(){if(iv)return nl;iv=1;var o=Symbol.for("react.transitional.element"),e=Symbol.for("react.fragment");function i(r,u,f){var h=null;if(f!==void 0&&(h=""+f),u.key!==void 0&&(h=""+u.key),"key"in u){f={};for(var d in u)d!=="key"&&(f[d]=u[d])}else f=u;return u=f.ref,{$$typeof:o,type:r,key:h,ref:u!==void 0?u:null,props:f}}return nl.Fragment=e,nl.jsx=i,nl.jsxs=i,nl}var av;function OM(){return av||(av=1,ld.exports=LM()),ld.exports}var cn=OM(),ud={exports:{}},ne={};var sv;function PM(){if(sv)return ne;sv=1;var o=Symbol.for("react.transitional.element"),e=Symbol.for("react.portal"),i=Symbol.for("react.fragment"),r=Symbol.for("react.strict_mode"),u=Symbol.for("react.profiler"),f=Symbol.for("react.consumer"),h=Symbol.for("react.context"),d=Symbol.for("react.forward_ref"),p=Symbol.for("react.suspense"),g=Symbol.for("react.memo"),v=Symbol.for("react.lazy"),_=Symbol.for("react.activity"),y=Symbol.for("react.view_transition"),M=Symbol.iterator;function E(D){return D===null||typeof D!="object"?null:(D=M&&D[M]||D["@@iterator"],typeof D=="function"?D:null)}var R={isMounted:function(){return!1},enqueueForceUpdate:function(){},enqueueReplaceState:function(){},enqueueSetState:function(){}},x=Object.assign,S={};function L(D,X,dt){this.props=D,this.context=X,this.refs=S,this.updater=dt||R}L.prototype.isReactComponent={},L.prototype.setState=function(D,X){if(typeof D!="object"&&typeof D!="function"&&D!=null)throw Error("takes an object of state variables to update or a function which returns an object of state variables.");this.updater.enqueueSetState(this,D,X,"setState")},L.prototype.forceUpdate=function(D){this.updater.enqueueForceUpdate(this,D,"forceUpdate")};function U(){}U.prototype=L.prototype;function P(D,X,dt){this.props=D,this.context=X,this.refs=S,this.updater=dt||R}var J=P.prototype=new U;J.constructor=P,x(J,L.prototype),J.isPureReactComponent=!0;var B=Array.isArray;function O(){}var V={H:null,A:null,T:null,S:null},gt=Object.prototype.hasOwnProperty;function T(D,X,dt){var ht=dt.ref;return{$$typeof:o,type:D,key:X,ref:ht!==void 0?ht:null,props:dt}}function w(D,X){return T(D.type,X,D.props)}function nt(D){return typeof D=="object"&&D!==null&&D.$$typeof===o}function rt(D){var X={"=":"=0",":":"=2"};return"$"+D.replace(/[=:]/g,function(dt){return X[dt]})}var lt=/\/+/g;function ft(D,X){return typeof D=="object"&&D!==null&&D.key!=null?rt(""+D.key):X.toString(36)}function H(D){switch(D.status){case"fulfilled":return D.value;case"rejected":throw D.reason;default:switch(typeof D.status=="string"?D.then(O,O):(D.status="pending",D.then(function(X){D.status==="pending"&&(D.status="fulfilled",D.value=X)},function(X){D.status==="pending"&&(D.status="rejected",D.reason=X)})),D.status){case"fulfilled":return D.value;case"rejected":throw D.reason}}throw D}function at(D,X,dt,ht,Ct){var Rt=typeof D;(Rt==="undefined"||Rt==="boolean")&&(D=null);var Ht=!1;if(D===null)Ht=!0;else switch(Rt){case"bigint":case"string":case"number":Ht=!0;break;case"object":switch(D.$$typeof){case o:case e:Ht=!0;break;case v:return Ht=D._init,at(Ht(D._payload),X,dt,ht,Ct)}}if(Ht)return Ct=Ct(D),Ht=ht===""?"."+ft(D,0):ht,B(Ct)?(dt="",Ht!=null&&(dt=Ht.replace(lt,"$&/")+"/"),at(Ct,X,dt,"",function(F){return F})):Ct!=null&&(nt(Ct)&&(Ct=w(Ct,dt+(Ct.key==null||D&&D.key===Ct.key?"":(""+Ct.key).replace(lt,"$&/")+"/")+Ht)),X.push(Ct)),1;Ht=0;var Mt=ht===""?".":ht+":";if(B(D))for(var bt=0;bt<D.length;bt++)ht=D[bt],Rt=Mt+ft(ht,bt),Ht+=at(ht,X,dt,Rt,Ct);else if(bt=E(D),typeof bt=="function")for(D=bt.call(D),bt=0;!(ht=D.next()).done;)ht=ht.value,Rt=Mt+ft(ht,bt++),Ht+=at(ht,X,dt,Rt,Ct);else if(Rt==="object"){if(typeof D.then=="function")return at(H(D),X,dt,ht,Ct);throw X=String(D),Error("Objects are not valid as a React child (found: "+(X==="[object Object]"?"object with keys {"+Object.keys(D).join(", ")+"}":X)+"). If you meant to render a collection of children, use an array instead.")}return Ht}function Z(D,X,dt){if(D==null)return D;var ht=[],Ct=0;return at(D,ht,"","",function(Rt){return X.call(dt,Rt,Ct++)}),ht}function yt(D){if(D._status===-1){var X=D._result,dt=X();dt.then(function(ht){(D._status===0||D._status===-1)&&(D._status=1,D._result=ht,dt.status===void 0&&(dt.status="fulfilled",dt.value=ht))},function(ht){(D._status===0||D._status===-1)&&(D._status=2,D._result=ht,dt.status===void 0&&(dt.status="rejected",dt.reason=ht))}),D._status===-1&&(D._status=0,D._result=dt)}if(D._status===1)return D._result.default;throw D._result}var St=typeof reportError=="function"?reportError:function(D){if(typeof window=="object"&&typeof window.ErrorEvent=="function"){var X=new window.ErrorEvent("error",{bubbles:!0,cancelable:!0,message:typeof D=="object"&&D!==null&&typeof D.message=="string"?String(D.message):String(D),error:D});if(!window.dispatchEvent(X))return}else if(typeof process=="object"&&typeof process.emit=="function"){process.emit("uncaughtException",D);return}console.error(D)};function Pt(D){var X=V.T,dt={};dt.types=X!==null?X.types:null,V.T=dt;try{var ht=D(),Ct=V.S;Ct!==null&&Ct(dt,ht),typeof ht=="object"&&ht!==null&&typeof ht.then=="function"&&ht.then(O,St)}catch(Rt){St(Rt)}finally{X!==null&&dt.types!==null&&(X.types=dt.types),V.T=X}}function oe(D){var X=V.T;if(X!==null){var dt=X.types;dt===null?X.types=[D]:dt.indexOf(D)===-1&&dt.push(D)}else Pt(oe.bind(null,D))}var me={map:Z,forEach:function(D,X,dt){Z(D,function(){X.apply(this,arguments)},dt)},count:function(D){var X=0;return Z(D,function(){X++}),X},toArray:function(D){return Z(D,function(X){return X})||[]},only:function(D){if(!nt(D))throw Error("React.Children.only expected to receive a single React element child.");return D}};return ne.Activity=_,ne.Children=me,ne.Component=L,ne.Fragment=i,ne.Profiler=u,ne.PureComponent=P,ne.StrictMode=r,ne.Suspense=p,ne.ViewTransition=y,ne.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE=V,ne.__COMPILER_RUNTIME={__proto__:null,c:function(D){return V.H.useMemoCache(D)}},ne.addTransitionType=oe,ne.cache=function(D){return function(){return D.apply(null,arguments)}},ne.cacheSignal=function(){return null},ne.cloneElement=function(D,X,dt){if(D==null)throw Error("The argument must be a React element, but you passed "+D+".");var ht=x({},D.props),Ct=D.key;if(X!=null)for(Rt in X.key!==void 0&&(Ct=""+X.key),X)!gt.call(X,Rt)||Rt==="key"||Rt==="__self"||Rt==="__source"||Rt==="ref"&&X.ref===void 0||(ht[Rt]=X[Rt]);var Rt=arguments.length-2;if(Rt===1)ht.children=dt;else if(1<Rt){for(var Ht=Array(Rt),Mt=0;Mt<Rt;Mt++)Ht[Mt]=arguments[Mt+2];ht.children=Ht}return T(D.type,Ct,ht)},ne.createContext=function(D){return D={$$typeof:h,_currentValue:D,_currentValue2:D,_threadCount:0,Provider:null,Consumer:null},D.Provider=D,D.Consumer={$$typeof:f,_context:D},D},ne.createElement=function(D,X,dt){var ht,Ct={},Rt=null;if(X!=null)for(ht in X.key!==void 0&&(Rt=""+X.key),X)gt.call(X,ht)&&ht!=="key"&&ht!=="__self"&&ht!=="__source"&&(Ct[ht]=X[ht]);var Ht=arguments.length-2;if(Ht===1)Ct.children=dt;else if(1<Ht){for(var Mt=Array(Ht),bt=0;bt<Ht;bt++)Mt[bt]=arguments[bt+2];Ct.children=Mt}if(D&&D.defaultProps)for(ht in Ht=D.defaultProps,Ht)Ct[ht]===void 0&&(Ct[ht]=Ht[ht]);return T(D,Rt,Ct)},ne.createRef=function(){return{current:null}},ne.forwardRef=function(D){return{$$typeof:d,render:D}},ne.isValidElement=nt,ne.lazy=function(D){return{$$typeof:v,_payload:{_status:-1,_result:D},_init:yt}},ne.memo=function(D,X){return{$$typeof:g,type:D,compare:X===void 0?null:X}},ne.startTransition=Pt,ne.unstable_useCacheRefresh=function(){return V.H.useCacheRefresh()},ne.use=function(D){return V.H.use(D)},ne.useActionState=function(D,X,dt){return V.H.useActionState(D,X,dt)},ne.useCallback=function(D,X){return V.H.useCallback(D,X)},ne.useContext=function(D){return V.H.useContext(D)},ne.useDebugValue=function(){},ne.useDeferredValue=function(D,X){return V.H.useDeferredValue(D,X)},ne.useEffect=function(D,X){return V.H.useEffect(D,X)},ne.useEffectEvent=function(D){return V.H.useEffectEvent(D)},ne.useId=function(){return V.H.useId()},ne.useImperativeHandle=function(D,X,dt){return V.H.useImperativeHandle(D,X,dt)},ne.useInsertionEffect=function(D,X){return V.H.useInsertionEffect(D,X)},ne.useLayoutEffect=function(D,X){return V.H.useLayoutEffect(D,X)},ne.useMemo=function(D,X){return V.H.useMemo(D,X)},ne.useOptimistic=function(D,X){return V.H.useOptimistic(D,X)},ne.useReducer=function(D,X,dt){return V.H.useReducer(D,X,dt)},ne.useRef=function(D){return V.H.useRef(D)},ne.useState=function(D){return V.H.useState(D)},ne.useSyncExternalStore=function(D,X,dt){return V.H.useSyncExternalStore(D,X,dt)},ne.useTransition=function(){return V.H.useTransition()},ne.version="19.3.1",ne}var rv;function Op(){return rv||(rv=1,ud.exports=PM()),ud.exports}var wi=Op(),cd={exports:{}},il={},fd={exports:{}},hd={};var ov;function zM(){return ov||(ov=1,(function(o){function e(H,at){var Z=H.length;H.push(at);t:for(;0<Z;){var yt=Z-1>>>1,St=H[yt];if(0<u(St,at))H[yt]=at,H[Z]=St,Z=yt;else break t}}function i(H){return H.length===0?null:H[0]}function r(H){if(H.length===0)return null;var at=H[0],Z=H.pop();if(Z!==at){H[0]=Z;t:for(var yt=0,St=H.length,Pt=St>>>1;yt<Pt;){var oe=2*(yt+1)-1,me=H[oe],D=oe+1,X=H[D];if(0>u(me,Z))D<St&&0>u(X,me)?(H[yt]=X,H[D]=Z,yt=D):(H[yt]=me,H[oe]=Z,yt=oe);else if(D<St&&0>u(X,Z))H[yt]=X,H[D]=Z,yt=D;else break t}}return at}function u(H,at){var Z=H.sortIndex-at.sortIndex;return Z!==0?Z:H.id-at.id}if(o.unstable_now=void 0,typeof performance=="object"&&typeof performance.now=="function"){var f=performance;o.unstable_now=function(){return f.now()}}else{var h=Date,d=h.now();o.unstable_now=function(){return h.now()-d}}var p=[],g=[],v=1,_=null,y=3,M=!1,E=!1,R=!1,x=!1,S=typeof setTimeout=="function"?setTimeout:null,L=typeof clearTimeout=="function"?clearTimeout:null,U=typeof setImmediate<"u"?setImmediate:null;function P(H){for(var at=i(g);at!==null;){if(at.callback===null)r(g);else if(at.startTime<=H)r(g),at.sortIndex=at.expirationTime,e(p,at);else break;at=i(g)}}function J(H){if(R=!1,P(H),!E)if(i(p)!==null)E=!0,B||(B=!0,nt());else{var at=i(g);at!==null&&ft(J,at.startTime-H)}}var B=!1,O=-1,V=5,gt=-1;function T(){return x?!0:!(o.unstable_now()-gt<V)}function w(){if(x=!1,B){var H=o.unstable_now();gt=H;var at=!0;try{t:{E=!1,R&&(R=!1,L(O),O=-1),M=!0;var Z=y;try{e:{for(P(H),_=i(p);_!==null&&!(_.expirationTime>H&&T());){var yt=_.callback;if(typeof yt=="function"){_.callback=null,y=_.priorityLevel;var St=yt(_.expirationTime<=H);if(H=o.unstable_now(),typeof St=="function"){_.callback=St,P(H),at=!0;break e}_===i(p)&&r(p),P(H)}else r(p);_=i(p)}if(_!==null)at=!0;else{var Pt=i(g);Pt!==null&&ft(J,Pt.startTime-H),at=!1}}break t}finally{_=null,y=Z,M=!1}at=void 0}}finally{at?nt():B=!1}}}var nt;if(typeof U=="function")nt=function(){U(w)};else if(typeof MessageChannel<"u"){var rt=new MessageChannel,lt=rt.port2;rt.port1.onmessage=w,nt=function(){lt.postMessage(null)}}else nt=function(){S(w,0)};function ft(H,at){O=S(function(){H(o.unstable_now())},at)}o.unstable_IdlePriority=5,o.unstable_ImmediatePriority=1,o.unstable_LowPriority=4,o.unstable_NormalPriority=3,o.unstable_Profiling=null,o.unstable_UserBlockingPriority=2,o.unstable_cancelCallback=function(H){H.callback=null},o.unstable_forceFrameRate=function(H){0>H||125<H?console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported"):V=0<H?Math.floor(1e3/H):5},o.unstable_getCurrentPriorityLevel=function(){return y},o.unstable_next=function(H){switch(y){case 1:case 2:case 3:var at=3;break;default:at=y}var Z=y;y=at;try{return H()}finally{y=Z}},o.unstable_requestPaint=function(){x=!0},o.unstable_runWithPriority=function(H,at){switch(H){case 1:case 2:case 3:case 4:case 5:break;default:H=3}var Z=y;y=H;try{return at()}finally{y=Z}},o.unstable_scheduleCallback=function(H,at,Z){var yt=o.unstable_now();switch(typeof Z=="object"&&Z!==null?(Z=Z.delay,Z=typeof Z=="number"&&0<Z?yt+Z:yt):Z=yt,H){case 1:var St=-1;break;case 2:St=250;break;case 5:St=1073741823;break;case 4:St=1e4;break;default:St=5e3}return St=Z+St,H={id:v++,callback:at,priorityLevel:H,startTime:Z,expirationTime:St,sortIndex:-1},Z>yt?(H.sortIndex=Z,e(g,H),i(p)===null&&H===i(g)&&(R?(L(O),O=-1):R=!0,ft(J,Z-yt))):(H.sortIndex=St,e(p,H),E||M||(E=!0,B||(B=!0,nt()))),H},o.unstable_shouldYield=T,o.unstable_wrapCallback=function(H){var at=y;return function(){var Z=y;y=at;try{return H.apply(this,arguments)}finally{y=Z}}}})(hd)),hd}var lv;function IM(){return lv||(lv=1,fd.exports=zM()),fd.exports}var dd={exports:{}},Tn={};var uv;function BM(){if(uv)return Tn;uv=1;var o=Op();function e(v){var _="https://react.dev/errors/"+v;if(1<arguments.length){_+="?args[]="+encodeURIComponent(arguments[1]);for(var y=2;y<arguments.length;y++)_+="&args[]="+encodeURIComponent(arguments[y])}return"Minified React error #"+v+"; visit "+_+" for the full message or use the non-minified dev environment for full errors and additional helpful warnings."}function i(){}var r={d:{f:i,r:function(){throw Error(e(522))},D:i,C:i,L:i,m:i,X:i,S:i,M:i},p:0,findDOMNode:null},u=Symbol.for("react.portal"),f=Symbol.for("react.recoverable"),h=Symbol.for("react.optimistic_key");function d(v,_,y){var M=3<arguments.length&&arguments[3]!==void 0?arguments[3]:null;return{$$typeof:u,key:M==null?null:M===h?h:""+M,children:v,containerInfo:_,implementation:y}}var p=o.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE;function g(v,_){if(v==="font")return"";if(typeof _=="string")return _==="use-credentials"?_:""}return Tn.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE=r,Tn.browser=function(v){return{$$typeof:f,_reason:v}},Tn.createPortal=function(v,_){var y=2<arguments.length&&arguments[2]!==void 0?arguments[2]:null;if(!_||_.nodeType!==1&&_.nodeType!==9&&_.nodeType!==11)throw Error(e(299));return d(v,_,null,y)},Tn.flushSync=function(v){var _=p.T,y=r.p;try{if(p.T=null,r.p=2,v)return v()}finally{p.T=_,r.p=y,r.d.f()}},Tn.preconnect=function(v,_){typeof v=="string"&&(_?(_=_.crossOrigin,_=typeof _=="string"?_==="use-credentials"?_:"":void 0):_=null,r.d.C(v,_))},Tn.prefetchDNS=function(v){typeof v=="string"&&r.d.D(v)},Tn.preinit=function(v,_){if(typeof v=="string"&&_&&typeof _.as=="string"){var y=_.as,M=g(y,_.crossOrigin),E=typeof _.integrity=="string"?_.integrity:void 0,R=typeof _.fetchPriority=="string"?_.fetchPriority:void 0;y==="style"?r.d.S(v,typeof _.precedence=="string"?_.precedence:void 0,{crossOrigin:M,integrity:E,fetchPriority:R}):y==="script"&&r.d.X(v,{crossOrigin:M,integrity:E,fetchPriority:R,nonce:typeof _.nonce=="string"?_.nonce:void 0})}},Tn.preinitModule=function(v,_){if(typeof v=="string")if(typeof _=="object"&&_!==null){if(_.as==null||_.as==="script"){var y=g(_.as,_.crossOrigin);r.d.M(v,{crossOrigin:y,integrity:typeof _.integrity=="string"?_.integrity:void 0,nonce:typeof _.nonce=="string"?_.nonce:void 0,fetchPriority:typeof _.fetchPriority=="string"?_.fetchPriority:void 0})}}else _==null&&r.d.M(v)},Tn.preload=function(v,_){if(typeof v=="string"&&typeof _=="object"&&_!==null&&typeof _.as=="string"){var y=_.as,M=g(y,_.crossOrigin);r.d.L(v,y,{crossOrigin:M,integrity:typeof _.integrity=="string"?_.integrity:void 0,nonce:typeof _.nonce=="string"?_.nonce:void 0,type:typeof _.type=="string"?_.type:void 0,fetchPriority:typeof _.fetchPriority=="string"?_.fetchPriority:void 0,referrerPolicy:typeof _.referrerPolicy=="string"?_.referrerPolicy:void 0,imageSrcSet:typeof _.imageSrcSet=="string"?_.imageSrcSet:void 0,imageSizes:typeof _.imageSizes=="string"?_.imageSizes:void 0,media:typeof _.media=="string"?_.media:void 0})}},Tn.preloadModule=function(v,_){if(typeof v=="string")if(_){var y=g(_.as,_.crossOrigin);r.d.m(v,{as:typeof _.as=="string"&&_.as!=="script"?_.as:void 0,crossOrigin:y,integrity:typeof _.integrity=="string"?_.integrity:void 0,nonce:typeof _.nonce=="string"?_.nonce:void 0,fetchPriority:typeof _.fetchPriority=="string"?_.fetchPriority:void 0})}else r.d.m(v)},Tn.requestFormReset=function(v){r.d.r(v)},Tn.unstable_batchedUpdates=function(v,_){return v(_)},Tn.useFormState=function(v,_,y){return p.H.useFormState(v,_,y)},Tn.useFormStatus=function(){return p.H.useHostTransitionStatus()},Tn.version="19.3.1",Tn}var cv;function FM(){if(cv)return dd.exports;cv=1;function o(){if(!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__>"u"||typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE!="function"))try{__REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(o)}catch(e){console.error(e)}}return o(),dd.exports=BM(),dd.exports}var fv;function HM(){if(fv)return il;fv=1;var o=IM(),e=Op(),i=FM();function r(t){var n="https://react.dev/errors/"+t;if(1<arguments.length){n+="?args[]="+encodeURIComponent(arguments[1]);for(var a=2;a<arguments.length;a++)n+="&args[]="+encodeURIComponent(arguments[a])}return"Minified React error #"+t+"; visit "+n+" for the full message or use the non-minified dev environment for full errors and additional helpful warnings."}function u(t){return!(!t||t.nodeType!==1&&t.nodeType!==9&&t.nodeType!==11)}function f(t){for(var n=t,a=n;a&&!a.alternate;)n=a,(n.flags&4098)!==0&&(t=n.return),a=n.return;for(;n.return;)n=n.return;return n.tag===3?t:null}function h(t){if(t.tag===13){var n=t.memoizedState;if(n===null&&(t=t.alternate,t!==null&&(n=t.memoizedState)),n!==null)return n.dehydrated}return null}function d(t){if(t.tag===31){var n=t.memoizedState;if(n===null&&(t=t.alternate,t!==null&&(n=t.memoizedState)),n!==null)return n.dehydrated}return null}function p(t){if(f(t)!==t)throw Error(r(188))}function g(t){var n=t.alternate;if(!n){if(n=f(t),n===null)throw Error(r(188));return n!==t?null:t}for(var a=t,s=n;;){var l=a.return;if(l===null)break;var c=l.alternate;if(c===null){if(s=l.return,s!==null){a=s;continue}break}if(l.child===c.child){for(c=l.child;c;){if(c===a)return p(l),t;if(c===s)return p(l),n;c=c.sibling}throw Error(r(188))}if(a.return!==s.return)a=l,s=c;else{for(var m=!1,b=l.child;b;){if(b===a){m=!0,a=l,s=c;break}if(b===s){m=!0,s=l,a=c;break}b=b.sibling}if(!m){for(b=c.child;b;){if(b===a){m=!0,a=c,s=l;break}if(b===s){m=!0,s=c,a=l;break}b=b.sibling}if(!m)throw Error(r(189))}}if(a.alternate!==s)throw Error(r(190))}if(a.tag!==3)throw Error(r(188));return a.stateNode.current===a?t:n}function v(t){var n=t.tag;if(n===5||n===26||n===27||n===6)return t;for(t=t.child;t!==null;){if(n=v(t),n!==null)return n;t=t.sibling}return null}function _(t,n,a,s,l,c){for(;t!==null;){if((t.tag===5||t.tag===27||t.tag===6)&&a(t,s,l,c)||(t.tag!==22||t.memoizedState===null)&&(n||t.tag!==5&&t.tag!==27)&&_(t.child,n,a,s,l,c))return!0;t=t.sibling}return!1}function y(t){for(t=t.return;t!==null;){if(t.tag===3||t.tag===5||t.tag===27)return t;t=t.return}return null}function M(t){var n=!1;for(t=t.return;t!==null&&(t.tag===4&&(n=!0),!(t.tag===3||t.tag===5||t.tag===27));)t=t.return;return n}function E(t){var n=[null,null],a=y(t);return a===null||R(n,t,a.child,{foundSelf:!1}),n}function R(t,n,a,s){for(;a!==null;){if(a===n)s.foundSelf=!0;else if(a.tag===5||a.tag===27||a.tag===6){if(s.foundSelf)return t[1]=a,!0;t[0]=a}else if((a.tag!==22||a.memoizedState===null)&&R(t,n,a.child,s))return!0;a=a.sibling}return!1}function x(t){switch(t.tag){case 5:case 27:case 6:return t.stateNode;case 3:return t.stateNode.containerInfo;default:throw Error(r(559))}}var S=null,L=null;function U(t,n,a){return t===a?!0:t===n?(S=t,!0):!1}function P(t,n,a){return t===a?(L=t,!1):t===n?(L!==null&&(S=t),!0):!1}function J(t){if(t===null)return null;do t=t===null?null:t.return;while(t&&t.tag!==5&&t.tag!==27&&t.tag!==3);return t||null}function B(t,n,a){for(var s=0,l=t;l;l=a(l))s++;l=0;for(var c=n;c;c=a(c))l++;for(;0<s-l;)t=a(t),s--;for(;0<l-s;)n=a(n),l--;for(;s--;){if(t===n||n!==null&&t===n.alternate)return t;t=a(t),n=a(n)}return null}var O=Object.assign,V=Symbol.for("react.element"),gt=Symbol.for("react.transitional.element"),T=Symbol.for("react.portal"),w=Symbol.for("react.fragment"),nt=Symbol.for("react.strict_mode"),rt=Symbol.for("react.profiler"),lt=Symbol.for("react.consumer"),ft=Symbol.for("react.context"),H=Symbol.for("react.forward_ref"),at=Symbol.for("react.suspense"),Z=Symbol.for("react.suspense_list"),yt=Symbol.for("react.memo"),St=Symbol.for("react.lazy"),Pt=Symbol.for("react.activity"),oe=Symbol.for("react.legacy_hidden"),me=Symbol.for("react.memo_cache_sentinel"),D=Symbol.for("react.view_transition"),X=Symbol.for("react.recoverable"),dt=Symbol.iterator;function ht(t){return t===null||typeof t!="object"?null:(t=dt&&t[dt]||t["@@iterator"],typeof t=="function"?t:null)}var Ct=Symbol.for("react.client.reference");function Rt(t){if(t==null)return null;if(typeof t=="function")return t.$$typeof===Ct?null:t.displayName||t.name||null;if(typeof t=="string")return t;switch(t){case w:return"Fragment";case rt:return"Profiler";case nt:return"StrictMode";case at:return"Suspense";case Z:return"SuspenseList";case Pt:return"Activity";case D:return"ViewTransition"}if(typeof t=="object")switch(t.$$typeof){case T:return"Portal";case ft:return t.displayName||"Context";case lt:return(t._context.displayName||"Context")+".Consumer";case H:var n=t.render;return t=t.displayName,t||(t=n.displayName||n.name||"",t=t!==""?"ForwardRef("+t+")":"ForwardRef"),t;case yt:return n=t.displayName||null,n!==null?n:Rt(t.type)||"Memo";case St:n=t._payload,t=t._init;try{return Rt(t(n))}catch{}}return null}var Ht=Array.isArray,Mt=e.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE,bt=i.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE,F={pending:!1,data:null,method:null,action:null},vn=[],le=-1;function ae(t){return{current:t}}function Xt(t){0>le||(t.current=vn[le],vn[le]=null,le--)}function Kt(t,n){le++,vn[le]=t.current,t.current=n}var Zt=ae(null),N=ae(null),A=ae(null),tt=ae(null);function pt(t,n){switch(Kt(A,n),Kt(N,t),Kt(Zt,null),n.nodeType){case 9:case 11:t=(t=n.documentElement)&&(t=t.namespaceURI)?h0(t):0;break;default:if(t=n.tagName,n=n.namespaceURI)n=h0(n),t=d0(n,t);else switch(t){case"svg":t=1;break;case"math":t=2;break;default:t=0}}Xt(Zt),Kt(Zt,t)}function vt(){Xt(Zt),Xt(N),Xt(A)}function mt(t){var n=t.memoizedState;n!==null&&(Or._currentValue=n.memoizedState,Kt(tt,t)),n=Zt.current;var a=d0(n,t.type);n!==a&&(Kt(N,t),Kt(Zt,a))}function kt(t){N.current===t&&(Xt(Zt),Xt(N)),tt.current===t&&(Xt(tt),Or._currentValue=F)}var wt,It;function ue(t){if(wt===void 0)try{throw Error()}catch(a){var n=a.stack.trim().match(/\n( *(at )?)/);wt=n&&n[1]||"",It=-1<a.stack.indexOf(`
    at`)?" (<anonymous>)":-1<a.stack.indexOf("@")?"@unknown:0:0":""}return`
`+wt+t+It}var xt=!1;function Bt(t,n){if(!t||xt)return"";xt=!0;var a=Error.prepareStackTrace;Error.prepareStackTrace=void 0;try{var s={DetermineComponentFrameRoot:function(){try{if(n){var ct=function(){throw Error()};if(Object.defineProperty(ct.prototype,"props",{set:function(){throw Error()}}),typeof Reflect=="object"&&Reflect.construct){try{Reflect.construct(ct,[])}catch(At){var G=At}Reflect.construct(t,[],ct)}else{try{ct.call()}catch(At){G=At}ct=!1;try{var $=Object.getOwnPropertyDescriptor(t.prototype,"props");Object.defineProperty(t.prototype,"props",{configurable:!0,set:function(){throw Error()}}),ct=!0,new t}finally{ct&&($!==void 0?Object.defineProperty(t.prototype,"props",$):delete t.prototype.props)}}}else{try{throw Error()}catch(At){G=At}(ct=t())&&typeof ct.catch=="function"&&ct.catch(function(){})}}catch(At){if(At&&G&&typeof At.stack=="string")return[At.stack,G.stack]}return[null,null]}};s.DetermineComponentFrameRoot.displayName="DetermineComponentFrameRoot";var l=Object.getOwnPropertyDescriptor(s.DetermineComponentFrameRoot,"name");l&&l.configurable&&Object.defineProperty(s.DetermineComponentFrameRoot,"name",{value:"DetermineComponentFrameRoot"});var c=s.DetermineComponentFrameRoot(),m=c[0],b=c[1];if(m&&b){var z=m.split(`
`),W=b.split(`
`);for(l=s=0;s<z.length&&!z[s].includes("DetermineComponentFrameRoot");)s++;for(;l<W.length&&!W[l].includes("DetermineComponentFrameRoot");)l++;if(s===z.length||l===W.length)for(s=z.length-1,l=W.length-1;1<=s&&0<=l&&z[s]!==W[l];)l--;for(;1<=s&&0<=l;s--,l--)if(z[s]!==W[l]){if(s!==1||l!==1)do if(s--,l--,0>l||z[s]!==W[l]){var et=`
`+z[s].replace(" at new "," at ");return t.displayName&&et.includes("<anonymous>")&&(et=et.replace("<anonymous>",t.displayName)),et}while(1<=s&&0<=l);break}}}finally{xt=!1,Error.prepareStackTrace=a}return(a=t?t.displayName||t.name:"")?ue(a):""}function te(t,n){switch(t.tag){case 26:case 27:case 5:return ue(t.type);case 16:return ue("Lazy");case 13:return t.child!==n&&n!==null?ue("Suspense Fallback"):ue("Suspense");case 19:return ue("SuspenseList");case 0:case 15:return Bt(t.type,!1);case 11:return Bt(t.type.render,!1);case 1:return Bt(t.type,!0);case 31:return ue("Activity");case 30:return ue("ViewTransition");default:return""}}function $t(t){try{var n="",a=null;do n+=te(t,a),a=t,t=t.return;while(t);return n}catch(s){return`
Error generating stack: `+s.message+`
`+s.stack}}var Ft=Object.prototype.hasOwnProperty,pe=o.unstable_scheduleCallback,ee=o.unstable_cancelCallback,Oe=o.unstable_shouldYield,Y=o.unstable_requestPaint,Tt=o.unstable_now,ot=o.unstable_getCurrentPriorityLevel,_t=o.unstable_ImmediatePriority,Lt=o.unstable_UserBlockingPriority,Ot=o.unstable_NormalPriority,xe=o.unstable_LowPriority,ke=o.unstable_IdlePriority,An=o.log,Te=o.unstable_setDisableYieldValue,tn=null,qe=null;function Mi(t){if(typeof An=="function"&&Te(t),qe&&typeof qe.setStrictMode=="function")try{qe.setStrictMode(tn,t)}catch{}}var Rn=Math.clz32?Math.clz32:xl,Ki=Math.log,ho=Math.LN2;function xl(t){return t>>>=0,t===0?32:31-(Ki(t)/ho|0)|0}var fs=256,Qi=262144,hs=4194304;function li(t){var n=t&42;if(n!==0)return n;switch(t&-t){case 1:return 1;case 2:return 2;case 4:return 4;case 8:return 8;case 16:return 16;case 32:return 32;case 64:return 64;case 128:return 128;case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:return t&-t;case 262144:case 524288:case 1048576:case 2097152:return t&3932160;case 4194304:case 8388608:case 16777216:case 33554432:return t&62914560;case 67108864:return 67108864;case 134217728:return 134217728;case 268435456:return 268435456;case 536870912:return 536870912;case 1073741824:return 0;default:return t}}function ds(t,n,a){var s=t.pendingLanes;if(s===0)return 0;var l=0,c=t.suspendedLanes,m=t.pingedLanes;t=t.warmLanes;var b=s&134217727;return b!==0?(s=b&~c,s!==0?l=li(s):(m&=b,m!==0?l=li(m):a||(a=b&~t,a!==0&&(l=li(a))))):(b=s&~c,b!==0?l=li(b):m!==0?l=li(m):a||(a=s&~t,a!==0&&(l=li(a)))),l===0?0:n!==0&&n!==l&&(n&c)===0&&(c=l&-l,a=n&-n,c>=a||c===32&&(a&4194048)!==0)?n:l}function ba(t,n){return(t.pendingLanes&~(t.suspendedLanes&~t.pingedLanes)&n)===0}function Ml(t,n){(n&8)!==0&&(n|=n&32);var a=t.entangledLanes;if(a!==0)for(t=t.entanglements,a&=n;0<a;){var s=31-Rn(a),l=1<<s;n|=t[s],a&=~l}return n}function zc(t,n){switch(t){case 1:case 2:case 4:case 8:case 64:return n+250;case 16:case 32:case 128:case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:case 262144:case 524288:case 1048576:case 2097152:return n+5e3;case 4194304:case 8388608:case 16777216:case 33554432:return-1;case 67108864:case 134217728:case 268435456:case 536870912:case 1073741824:return-1;default:return-1}}function El(){var t=hs;return hs<<=1,(hs&62914560)===0&&(hs=4194304),t}function C(t){for(var n=[],a=0;31>a;a++)n.push(t);return n}function k(t,n){t.pendingLanes|=n,n!==268435456&&(t.suspendedLanes=0,t.pingedLanes=0,t.warmLanes=0)}function it(t,n,a,s,l,c){var m=t.pendingLanes;t.pendingLanes=a,t.suspendedLanes=0,t.pingedLanes=0,t.warmLanes=0,t.expiredLanes&=a,t.entangledLanes&=a,t.errorRecoveryDisabledLanes&=a,t.shellSuspendCounter=0;var b=t.entanglements,z=t.expirationTimes,W=t.hiddenUpdates;for(a=m&~a;0<a;){var et=31-Rn(a),ct=1<<et;b[et]=0,z[et]=-1;var G=W[et];if(G!==null)for(W[et]=null,et=0;et<G.length;et++){var $=G[et];$!==null&&($.lane&=-536870913)}a&=~ct}s!==0&&st(t,s,0),c!==0&&l===0&&t.tag!==0&&(t.suspendedLanes|=c&~(m&~n))}function st(t,n,a){t.pendingLanes|=n,t.suspendedLanes&=~n;var s=31-Rn(n);t.entangledLanes|=n,t.entanglements[s]=t.entanglements[s]|1073741824|a&261930}function j(t,n){var a=t.entangledLanes|=n;for(t=t.entanglements;a;){var s=31-Rn(a),l=1<<s;l&n|t[s]&n&&(t[s]|=n),a&=~l}}function Et(t,n){var a=n&-n;return a=(a&42)!==0?1:Nt(a),(a&(t.suspendedLanes|n))!==0?0:a}function Nt(t){switch(t){case 2:t=1;break;case 8:t=4;break;case 32:t=16;break;case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:case 262144:case 524288:case 1048576:case 2097152:case 4194304:case 8388608:case 16777216:case 33554432:t=128;break;case 268435456:t=134217728;break;default:t=0}return t}function Gt(t){return t&=-t,2<t?8<t?(t&134217727)!==0?32:268435456:8:2}function Yt(){var t=bt.p;return t!==0?t:(t=window.event,t===void 0?32:K0(t.type))}function Qt(t,n){var a=bt.p;try{return bt.p=t,n()}finally{bt.p=a}}var jt=Math.random().toString(36).slice(2),Ut="__reactFiber$"+jt,ie="__reactProps$"+jt,be="__reactContainer$"+jt,Ve="__reactEvents$"+jt,Nn="__reactListeners$"+jt,Ae="__reactHandles$"+jt,qt="__reactResources$"+jt,We="__reactMarker$"+jt,Me="__reactLoad$"+jt;function Cn(t){delete t[Ut],delete t[ie],delete t[Nn],delete t[Ae]}function Hn(t){var n;if(n=t[Ut])return n;for(var a=t.parentNode;a;){if(n=a[be]||a[Ut]){if(a=n.alternate,n.child!==null||a!==null&&a.child!==null)for(t=D0(t);t!==null;){if(a=t[Ut])return a;t=D0(t)}return n}t=a,a=t.parentNode}return null}function en(t){if(t=t[Ut]||t[be]){var n=t.tag;if(n===5||n===6||n===13||n===31||n===26||n===27||n===3)return t}return null}function Ji(t){var n=t.tag;if(n===5||n===26||n===27||n===6)return t.stateNode;throw Error(r(33))}function Pe(t){var n=t[qt];return n||(n=t[qt]={hoistableStyles:new Map,hoistableScripts:new Map}),n}function Be(t){t[We]=!0}function Ks(t){t[Me]=void 0}var Ln=new Set,Qs={};function $i(t,n){ta(t,n),ta(t+"Capture",n)}function ta(t,n){for(Qs[t]=n,t=0;t<n.length;t++)Ln.add(n[t])}var QS=RegExp("^[:A-Z_a-z\\u00C0-\\u00D6\\u00D8-\\u00F6\\u00F8-\\u02FF\\u0370-\\u037D\\u037F-\\u1FFF\\u200C-\\u200D\\u2070-\\u218F\\u2C00-\\u2FEF\\u3001-\\uD7FF\\uF900-\\uFDCF\\uFDF0-\\uFFFD][:A-Z_a-z\\u00C0-\\u00D6\\u00D8-\\u00F6\\u00F8-\\u02FF\\u0370-\\u037D\\u037F-\\u1FFF\\u200C-\\u200D\\u2070-\\u218F\\u2C00-\\u2FEF\\u3001-\\uD7FF\\uF900-\\uFDCF\\uFDF0-\\uFFFD\\-.0-9\\u00B7\\u0300-\\u036F\\u203F-\\u2040]*$"),Kp={},Qp={};function JS(t){return Ft.call(Qp,t)?!0:Ft.call(Kp,t)?!1:QS.test(t)?Qp[t]=!0:(Kp[t]=!0,!1)}var Re=!1;function Jp(){var t=Re;return Re=!1,t}function Tl(t,n,a){if(JS(n))if(a===null)t.removeAttribute(n);else{switch(typeof a){case"undefined":case"function":case"symbol":t.removeAttribute(n);return;case"boolean":var s=n.toLowerCase().slice(0,5);if(s!=="data-"&&s!=="aria-"){t.removeAttribute(n);return}}t.setAttribute(n,a)}}function bl(t,n,a){if(a===null)t.removeAttribute(n);else{switch(typeof a){case"undefined":case"function":case"symbol":case"boolean":t.removeAttribute(n);return}t.setAttribute(n,a)}}function ea(t,n,a,s){if(s===null)t.removeAttribute(a);else{switch(typeof s){case"undefined":case"function":case"symbol":case"boolean":t.removeAttribute(a);return}t.setAttributeNS(n,a,s)}}function Jn(t){switch(typeof t){case"bigint":case"boolean":case"number":case"string":case"undefined":return t;case"object":return t;default:return""}}function $p(t){var n=t.type;return(t=t.nodeName)&&t.toLowerCase()==="input"&&(n==="checkbox"||n==="radio")}function $S(t,n,a){var s=Object.getOwnPropertyDescriptor(t.constructor.prototype,n);if(!t.hasOwnProperty(n)&&typeof s<"u"&&typeof s.get=="function"&&typeof s.set=="function"){var l=s.get,c=s.set;return Object.defineProperty(t,n,{configurable:!0,get:function(){return l.call(this)},set:function(m){a=""+m,c.call(this,m)}}),Object.defineProperty(t,n,{enumerable:s.enumerable}),{getValue:function(){return a},setValue:function(m){a=""+m},stopTracking:function(){t._valueTracker=null,delete t[n]}}}}function Ic(t){if(!t._valueTracker){var n=$p(t)?"checked":"value";t._valueTracker=$S(t,n,""+t[n])}}function tm(t){if(!t)return!1;var n=t._valueTracker;if(!n)return!0;var a=n.getValue(),s="";return t&&(s=$p(t)?t.checked?"true":"false":t.value),t=s,t!==a?(n.setValue(t),!0):!1}var ty=/[\n"\\]/g;function ui(t){return t.replace(ty,function(n){return"\\"+n.charCodeAt(0).toString(16)+" "})}function Bc(t,n,a,s,l,c,m,b){t.name="",m!=null&&typeof m!="function"&&typeof m!="symbol"&&typeof m!="boolean"?t.type=m:t.removeAttribute("type"),n!=null?m==="number"?(n===0&&t.value===""||t.value!=n)&&(t.value=""+Jn(n)):t.value!==""+Jn(n)&&(t.value=""+Jn(n)):m!=="submit"&&m!=="reset"||t.removeAttribute("value"),n!=null?m==="number"&&t.value==n?Fc(t,Jn(t.value)):Fc(t,Jn(n)):a!=null?Fc(t,Jn(a)):s!=null&&t.removeAttribute("value"),l==null&&c!=null&&(t.defaultChecked=!!c),l!=null&&(t.checked=l&&typeof l!="function"&&typeof l!="symbol"),b!=null&&typeof b!="function"&&typeof b!="symbol"&&typeof b!="boolean"?t.name=""+Jn(b):t.removeAttribute("name")}function em(t,n,a,s,l,c,m,b){if(c!=null&&typeof c!="function"&&typeof c!="symbol"&&typeof c!="boolean"&&(t.type=c),n!=null||a!=null){if(!(c!=="submit"&&c!=="reset"||n!=null)){Ic(t);return}a=a!=null?""+Jn(a):"",n=n!=null?""+Jn(n):a,b||n===t.value||(t.value=n),t.defaultValue=n}s=s??l,s=typeof s!="function"&&typeof s!="symbol"&&!!s,t.checked=b?t.checked:!!s,t.defaultChecked=!!s,m!=null&&typeof m!="function"&&typeof m!="symbol"&&typeof m!="boolean"&&(t.name=m),Ic(t)}function Fc(t,n){t.defaultValue!==""+n&&(t.defaultValue=""+n)}function Js(t,n,a,s){if(t=t.options,n){n={};for(var l=0;l<a.length;l++)n["$"+a[l]]=!0;for(a=0;a<t.length;a++)l=n.hasOwnProperty("$"+t[a].value),t[a].selected!==l&&(t[a].selected=l),l&&s&&(t[a].defaultSelected=!0)}else{for(a=""+Jn(a),n=null,l=0;l<t.length;l++){if(t[l].value===a){t[l].selected=!0,s&&(t[l].defaultSelected=!0);return}n!==null||t[l].disabled||(n=t[l])}n!==null&&(n.selected=!0)}}function nm(t,n,a){if(n!=null&&(n=""+Jn(n),n!==t.value&&(t.value=n),a==null)){t.defaultValue!==n&&(t.defaultValue=n);return}t.defaultValue=a!=null?""+Jn(a):""}function im(t,n,a,s){if(n==null){if(s!=null){if(a!=null)throw Error(r(92));if(Ht(s)){if(1<s.length)throw Error(r(93));s=s[0]}a=s}a==null&&(a=""),n=a}a=Jn(n),t.defaultValue=a,s=t.textContent,s===a&&s!==""&&s!==null&&(t.value=s),Ic(t)}function $s(t,n){if(n){var a=t.firstChild;if(a&&a===t.lastChild&&a.nodeType===3){a.nodeValue=n;return}}t.textContent=n}var ey=new Set("animationIterationCount aspectRatio borderImageOutset borderImageSlice borderImageWidth boxFlex boxFlexGroup boxOrdinalGroup columnCount columns flex flexGrow flexPositive flexShrink flexNegative flexOrder gridArea gridRow gridRowEnd gridRowSpan gridRowStart gridColumn gridColumnEnd gridColumnSpan gridColumnStart fontWeight lineClamp lineHeight opacity order orphans scale tabSize widows zIndex zoom fillOpacity floodOpacity stopOpacity strokeDasharray strokeDashoffset strokeMiterlimit strokeOpacity strokeWidth MozAnimationIterationCount MozBoxFlex MozBoxFlexGroup MozLineClamp msAnimationIterationCount msFlex msZoom msFlexGrow msFlexNegative msFlexOrder msFlexPositive msFlexShrink msGridColumn msGridColumnSpan msGridRow msGridRowSpan WebkitAnimationIterationCount WebkitBoxFlex WebKitBoxFlexGroup WebkitBoxOrdinalGroup WebkitColumnCount WebkitColumns WebkitFlex WebkitFlexGrow WebkitFlexPositive WebkitFlexShrink WebkitLineClamp".split(" "));function am(t,n,a){var s=n.indexOf("--")===0;a==null||typeof a=="boolean"||a===""?s?t.setProperty(n,""):n==="float"?t.cssFloat="":t[n]="":s?t.setProperty(n,a):typeof a!="number"||a===0||ey.has(n)?n==="float"?t.cssFloat=a:t[n]=(""+a).trim():t[n]=a+"px"}function sm(t,n,a){if(n!=null&&typeof n!="object")throw Error(r(62));if(t=t.style,a!=null){for(var s in a)!a.hasOwnProperty(s)||n!=null&&n.hasOwnProperty(s)||(s.indexOf("--")===0?t.setProperty(s,""):s==="float"?t.cssFloat="":t[s]="",Re=!0);for(var l in n)s=n[l],n.hasOwnProperty(l)&&a[l]!==s&&(am(t,l,s),Re=!0)}else for(var c in n)n.hasOwnProperty(c)&&am(t,c,n[c])}function Hc(t){if(t.indexOf("-")===-1)return!1;switch(t){case"annotation-xml":case"color-profile":case"font-face":case"font-face-src":case"font-face-uri":case"font-face-format":case"font-face-name":case"missing-glyph":return!1;default:return!0}}var ny=new Map([["acceptCharset","accept-charset"],["htmlFor","for"],["httpEquiv","http-equiv"],["crossOrigin","crossorigin"],["accentHeight","accent-height"],["alignmentBaseline","alignment-baseline"],["arabicForm","arabic-form"],["baselineShift","baseline-shift"],["capHeight","cap-height"],["clipPath","clip-path"],["clipRule","clip-rule"],["colorInterpolation","color-interpolation"],["colorInterpolationFilters","color-interpolation-filters"],["colorProfile","color-profile"],["colorRendering","color-rendering"],["dominantBaseline","dominant-baseline"],["enableBackground","enable-background"],["fillOpacity","fill-opacity"],["fillRule","fill-rule"],["floodColor","flood-color"],["floodOpacity","flood-opacity"],["fontFamily","font-family"],["fontSize","font-size"],["fontSizeAdjust","font-size-adjust"],["fontStretch","font-stretch"],["fontStyle","font-style"],["fontVariant","font-variant"],["fontWeight","font-weight"],["glyphName","glyph-name"],["glyphOrientationHorizontal","glyph-orientation-horizontal"],["glyphOrientationVertical","glyph-orientation-vertical"],["horizAdvX","horiz-adv-x"],["horizOriginX","horiz-origin-x"],["imageRendering","image-rendering"],["letterSpacing","letter-spacing"],["lightingColor","lighting-color"],["markerEnd","marker-end"],["markerMid","marker-mid"],["markerStart","marker-start"],["maskType","mask-type"],["overlinePosition","overline-position"],["overlineThickness","overline-thickness"],["paintOrder","paint-order"],["panose-1","panose-1"],["pointerEvents","pointer-events"],["renderingIntent","rendering-intent"],["shapeRendering","shape-rendering"],["stopColor","stop-color"],["stopOpacity","stop-opacity"],["strikethroughPosition","strikethrough-position"],["strikethroughThickness","strikethrough-thickness"],["strokeDasharray","stroke-dasharray"],["strokeDashoffset","stroke-dashoffset"],["strokeLinecap","stroke-linecap"],["strokeLinejoin","stroke-linejoin"],["strokeMiterlimit","stroke-miterlimit"],["strokeOpacity","stroke-opacity"],["strokeWidth","stroke-width"],["textAnchor","text-anchor"],["textDecoration","text-decoration"],["textRendering","text-rendering"],["transformOrigin","transform-origin"],["underlinePosition","underline-position"],["underlineThickness","underline-thickness"],["unicodeBidi","unicode-bidi"],["unicodeRange","unicode-range"],["unitsPerEm","units-per-em"],["vAlphabetic","v-alphabetic"],["vHanging","v-hanging"],["vIdeographic","v-ideographic"],["vMathematical","v-mathematical"],["vectorEffect","vector-effect"],["vertAdvY","vert-adv-y"],["vertOriginX","vert-origin-x"],["vertOriginY","vert-origin-y"],["wordSpacing","word-spacing"],["writingMode","writing-mode"],["xmlnsXlink","xmlns:xlink"],["xHeight","x-height"]]),iy=/^[\u0000-\u001F ]*j[\r\n\t]*a[\r\n\t]*v[\r\n\t]*a[\r\n\t]*s[\r\n\t]*c[\r\n\t]*r[\r\n\t]*i[\r\n\t]*p[\r\n\t]*t[\r\n\t]*:/i;function Al(t){return iy.test(""+t)?"javascript:throw new Error('React has blocked a javascript: URL as a security precaution.')":t}function Ii(){}var Gc=null;function Vc(t){return t=t.target||t.srcElement||window,t.correspondingUseElement&&(t=t.correspondingUseElement),t.nodeType===3?t.parentNode:t}var tr=null,er=null;function rm(t){var n=en(t);if(n&&(t=n.stateNode)){var a=t[ie]||null;t:switch(t=n.stateNode,n.type){case"input":if(Bc(t,a.value,a.defaultValue,a.defaultValue,a.checked,a.defaultChecked,a.type,a.name),n=a.name,a.type==="radio"&&n!=null){for(a=t;a.parentNode;)a=a.parentNode;for(a=a.querySelectorAll('input[name="'+ui(""+n)+'"][type="radio"]'),n=0;n<a.length;n++){var s=a[n];if(s!==t&&s.form===t.form){var l=s[ie]||null;if(!l)throw Error(r(90));Bc(s,l.value,l.defaultValue,l.defaultValue,l.checked,l.defaultChecked,l.type,l.name)}}for(n=0;n<a.length;n++)s=a[n],s.form===t.form&&tm(s)}break t;case"textarea":nm(t,a.value,a.defaultValue);break t;case"select":n=a.value,n!=null&&Js(t,!!a.multiple,n,!1)}}}var Xc=!1;function om(t,n,a){if(Xc)return t(n,a);Xc=!0;try{var s=t(n);return s}finally{if(Xc=!1,(tr!==null||er!==null)&&(Au(),tr&&(n=tr,t=er,er=tr=null,rm(n),t)))for(n=0;n<t.length;n++)rm(t[n])}}function po(t,n){var a=t.stateNode;if(a===null)return null;var s=a[ie]||null;if(s===null)return null;a=s[n];t:switch(n){case"onClick":case"onClickCapture":case"onDoubleClick":case"onDoubleClickCapture":case"onMouseDown":case"onMouseDownCapture":case"onMouseMove":case"onMouseMoveCapture":case"onMouseUp":case"onMouseUpCapture":case"onMouseEnter":(s=!s.disabled)||(t=t.type,s=!(t==="button"||t==="input"||t==="select"||t==="textarea")),t=!s;break t;default:t=!1}if(t)return null;if(a&&typeof a!="function")throw Error(r(231,n,typeof a));return a}var na=!(typeof window>"u"||typeof window.document>"u"||typeof window.document.createElement>"u"),Yc=!1;if(na)try{var mo={};Object.defineProperty(mo,"passive",{get:function(){Yc=!0}}),window.addEventListener("test",mo,mo),window.removeEventListener("test",mo,mo)}catch{Yc=!1}var Aa=null,kc=null,Rl=null;function lm(){if(Rl)return Rl;var t,n=kc,a=n.length,s,l="value"in Aa?Aa.value:Aa.textContent,c=l.length;for(t=0;t<a&&n[t]===l[t];t++);var m=a-t;for(s=1;s<=m&&n[a-s]===l[c-s];s++);return Rl=l.slice(t,1<s?1-s:void 0)}function Cl(t){var n=t.keyCode;return"charCode"in t?(t=t.charCode,t===0&&n===13&&(t=13)):t=n,t===10&&(t=13),32<=t||t===13?t:0}function wl(){return!0}function um(){return!1}function On(t){function n(a,s,l,c,m){this._reactName=a,this._targetInst=l,this.type=s,this.nativeEvent=c,this.target=m,this.currentTarget=null;for(var b in t)t.hasOwnProperty(b)&&(a=t[b],this[b]=a?a(c):c[b]);return this.isDefaultPrevented=(c.defaultPrevented!=null?c.defaultPrevented:c.returnValue===!1)?wl:um,this.isPropagationStopped=um,this}return O(n.prototype,{preventDefault:function(){this.defaultPrevented=!0;var a=this.nativeEvent;a&&(a.preventDefault?a.preventDefault():typeof a.returnValue!="unknown"&&(a.returnValue=!1),this.isDefaultPrevented=wl)},stopPropagation:function(){var a=this.nativeEvent;a&&(a.stopPropagation?a.stopPropagation():typeof a.cancelBubble!="unknown"&&(a.cancelBubble=!0),this.isPropagationStopped=wl)},persist:function(){},isPersistent:wl}),n}var Ra={eventPhase:0,bubbles:0,cancelable:0,timeStamp:function(t){return t.timeStamp||Date.now()},defaultPrevented:0,isTrusted:0},Dl=On(Ra),_o=O({},Ra,{view:0,detail:0}),ay=On(_o),qc,Wc,go,Ul=O({},_o,{screenX:0,screenY:0,clientX:0,clientY:0,pageX:0,pageY:0,ctrlKey:0,shiftKey:0,altKey:0,metaKey:0,getModifierState:Zc,button:0,buttons:0,relatedTarget:function(t){return t.relatedTarget===void 0?t.fromElement===t.srcElement?t.toElement:t.fromElement:t.relatedTarget},movementX:function(t){return"movementX"in t?t.movementX:(t!==go&&(go&&t.type==="mousemove"?(qc=t.screenX-go.screenX,Wc=t.screenY-go.screenY):Wc=qc=0,go=t),qc)},movementY:function(t){return"movementY"in t?t.movementY:Wc}}),cm=On(Ul),sy=O({},Ul,{dataTransfer:0}),ry=On(sy),oy=O({},_o,{relatedTarget:0}),jc=On(oy),ly=O({},Ra,{animationName:0,elapsedTime:0,pseudoElement:0}),uy=On(ly),cy=O({},Ra,{clipboardData:function(t){return"clipboardData"in t?t.clipboardData:window.clipboardData}}),fy=On(cy),hy=O({},Ra,{data:0}),fm=On(hy),dy={Esc:"Escape",Spacebar:" ",Left:"ArrowLeft",Up:"ArrowUp",Right:"ArrowRight",Down:"ArrowDown",Del:"Delete",Win:"OS",Menu:"ContextMenu",Apps:"ContextMenu",Scroll:"ScrollLock",MozPrintableKey:"Unidentified"},py={8:"Backspace",9:"Tab",12:"Clear",13:"Enter",16:"Shift",17:"Control",18:"Alt",19:"Pause",20:"CapsLock",27:"Escape",32:" ",33:"PageUp",34:"PageDown",35:"End",36:"Home",37:"ArrowLeft",38:"ArrowUp",39:"ArrowRight",40:"ArrowDown",45:"Insert",46:"Delete",112:"F1",113:"F2",114:"F3",115:"F4",116:"F5",117:"F6",118:"F7",119:"F8",120:"F9",121:"F10",122:"F11",123:"F12",144:"NumLock",145:"ScrollLock",224:"Meta"},my={Alt:"altKey",Control:"ctrlKey",Meta:"metaKey",Shift:"shiftKey"};function _y(t){var n=this.nativeEvent;return n.getModifierState?n.getModifierState(t):(t=my[t])?!!n[t]:!1}function Zc(){return _y}var gy=O({},_o,{key:function(t){if(t.key){var n=dy[t.key]||t.key;if(n!=="Unidentified")return n}return t.type==="keypress"?(t=Cl(t),t===13?"Enter":String.fromCharCode(t)):t.type==="keydown"||t.type==="keyup"?py[t.keyCode]||"Unidentified":""},code:0,location:0,ctrlKey:0,shiftKey:0,altKey:0,metaKey:0,repeat:0,locale:0,getModifierState:Zc,charCode:function(t){return t.type==="keypress"?Cl(t):0},keyCode:function(t){return t.type==="keydown"||t.type==="keyup"?t.keyCode:0},which:function(t){return t.type==="keypress"?Cl(t):t.type==="keydown"||t.type==="keyup"?t.keyCode:0}}),vy=On(gy),Sy=O({},Ul,{pointerId:0,width:0,height:0,pressure:0,tangentialPressure:0,tiltX:0,tiltY:0,twist:0,pointerType:0,isPrimary:0}),hm=On(Sy),yy=O({},Ra,{submitter:0}),xy=On(yy),My=O({},_o,{touches:0,targetTouches:0,changedTouches:0,altKey:0,metaKey:0,ctrlKey:0,shiftKey:0,getModifierState:Zc}),Ey=On(My),Ty=O({},Ra,{propertyName:0,elapsedTime:0,pseudoElement:0}),by=On(Ty),Ay=O({},Ul,{deltaX:function(t){return"deltaX"in t?t.deltaX:"wheelDeltaX"in t?-t.wheelDeltaX:0},deltaY:function(t){return"deltaY"in t?t.deltaY:"wheelDeltaY"in t?-t.wheelDeltaY:"wheelDelta"in t?-t.wheelDelta:0},deltaZ:0,deltaMode:0}),Ry=On(Ay),Cy=O({},Ra,{newState:0,oldState:0,source:0}),wy=On(Cy),Dy=[9,13,27,32],Kc=na&&"CompositionEvent"in window,vo=null;na&&"documentMode"in document&&(vo=document.documentMode);var Uy=na&&"TextEvent"in window&&!vo,dm=na&&(!Kc||vo&&8<vo&&11>=vo),pm=" ",mm=!1;function _m(t,n){switch(t){case"keyup":return Dy.indexOf(n.keyCode)!==-1;case"keydown":return n.keyCode!==229;case"keypress":case"mousedown":case"focusout":return!0;default:return!1}}function gm(t){return t=t.detail,typeof t=="object"&&"data"in t?t.data:null}var nr=!1;function Ny(t,n){switch(t){case"compositionend":return gm(n);case"keypress":return n.which!==32?null:(mm=!0,pm);case"textInput":return t=n.data,t===pm&&mm?null:t;default:return null}}function Ly(t,n){if(nr)return t==="compositionend"||!Kc&&_m(t,n)?(t=lm(),Rl=kc=Aa=null,nr=!1,t):null;switch(t){case"paste":return null;case"keypress":if(!(n.ctrlKey||n.altKey||n.metaKey)||n.ctrlKey&&n.altKey){if(n.char&&1<n.char.length)return n.char;if(n.which)return String.fromCharCode(n.which)}return null;case"compositionend":return dm&&n.locale!=="ko"?null:n.data;default:return null}}var Oy={color:!0,date:!0,datetime:!0,"datetime-local":!0,email:!0,month:!0,number:!0,password:!0,range:!0,search:!0,tel:!0,text:!0,time:!0,url:!0,week:!0};function vm(t){var n=t&&t.nodeName&&t.nodeName.toLowerCase();return n==="input"?!!Oy[t.type]:n==="textarea"}function Sm(t,n,a,s){tr?er?er.push(s):er=[s]:tr=s,n=Nu(n,"onChange"),0<n.length&&(a=new Dl("onChange","change",null,a,s),t.push({event:a,listeners:n}))}var So=null,yo=null;function Py(t){r0(t,0)}function Nl(t){var n=Ji(t);if(tm(n))return t}function ym(t,n){if(t==="change")return n}var xm=!1;if(na){var Qc;if(na){var Jc="oninput"in document;if(!Jc){var Mm=document.createElement("div");Mm.setAttribute("oninput","return;"),Jc=typeof Mm.oninput=="function"}Qc=Jc}else Qc=!1;xm=Qc&&(!document.documentMode||9<document.documentMode)}function Em(){So&&(So.detachEvent("onpropertychange",Tm),yo=So=null)}function Tm(t){if(t.propertyName==="value"&&Nl(yo)){var n=[];Sm(n,yo,t,Vc(t)),om(Py,n)}}function zy(t,n,a){t==="focusin"?(Em(),So=n,yo=a,So.attachEvent("onpropertychange",Tm)):t==="focusout"&&Em()}function Iy(t){if(t==="selectionchange"||t==="keyup"||t==="keydown")return Nl(yo)}function By(t,n){if(t==="click")return Nl(n)}function Fy(t,n){if(t==="input"||t==="change")return Nl(n)}function Hy(t,n){return t===n&&(t!==0||1/t===1/n)||t!==t&&n!==n}var $n=typeof Object.is=="function"?Object.is:Hy;function xo(t,n){if($n(t,n))return!0;if(typeof t!="object"||t===null||typeof n!="object"||n===null)return!1;var a=Object.keys(t),s=Object.keys(n);if(a.length!==s.length)return!1;for(s=0;s<a.length;s++){var l=a[s];if(!Ft.call(n,l)||!$n(t[l],n[l]))return!1}return!0}function $c(t){if(t=t||(typeof document<"u"?document:void 0),typeof t>"u")return null;try{return t.activeElement||t.body}catch{return t.body}}function bm(t){for(;t&&t.firstChild;)t=t.firstChild;return t}function Am(t,n){var a=bm(t);t=0;for(var s;a;){if(a.nodeType===3){if(s=t+a.textContent.length,t<=n&&s>=n)return{node:a,offset:n-t};t=s}t:{for(;a;){if(a.nextSibling){a=a.nextSibling;break t}a=a.parentNode}a=void 0}a=bm(a)}}function Rm(t,n){return t&&n?t===n?!0:t&&t.nodeType===3?!1:n&&n.nodeType===3?Rm(t,n.parentNode):"contains"in t?t.contains(n):t.compareDocumentPosition?!!(t.compareDocumentPosition(n)&16):!1:!1}function Cm(t){t=t!=null&&t.ownerDocument!=null&&t.ownerDocument.defaultView!=null?t.ownerDocument.defaultView:window;for(var n=$c(t.document);n instanceof t.HTMLIFrameElement;){try{var a=typeof n.contentWindow.location.href=="string"}catch{a=!1}if(a)t=n.contentWindow;else break;n=$c(t.document)}return n}function tf(t){var n=t&&t.nodeName&&t.nodeName.toLowerCase();return n&&(n==="input"&&(t.type==="text"||t.type==="search"||t.type==="tel"||t.type==="url"||t.type==="password")||n==="textarea"||t.contentEditable==="true")}var Gy=na&&"documentMode"in document&&11>=document.documentMode,ir=null,ef=null,Mo=null,nf=!1;function wm(t,n,a){var s=a.window===a?a.document:a.nodeType===9?a:a.ownerDocument;nf||ir==null||ir!==$c(s)||(s=ir,"selectionStart"in s&&tf(s)?s={start:s.selectionStart,end:s.selectionEnd}:(s=(s.ownerDocument&&s.ownerDocument.defaultView||window).getSelection(),s={anchorNode:s.anchorNode,anchorOffset:s.anchorOffset,focusNode:s.focusNode,focusOffset:s.focusOffset}),Mo&&xo(Mo,s)||(Mo=s,s=Nu(ef,"onSelect"),0<s.length&&(n=new Dl("onSelect","select",null,n,a),t.push({event:n,listeners:s}),n.target=ir)))}function ps(t,n){var a={};return a[t.toLowerCase()]=n.toLowerCase(),a["Webkit"+t]="webkit"+n,a["Moz"+t]="moz"+n,a}var ar={animationend:ps("Animation","AnimationEnd"),animationiteration:ps("Animation","AnimationIteration"),animationstart:ps("Animation","AnimationStart"),transitionrun:ps("Transition","TransitionRun"),transitionstart:ps("Transition","TransitionStart"),transitioncancel:ps("Transition","TransitionCancel"),transitionend:ps("Transition","TransitionEnd")},af={},Dm={};na&&(Dm=document.createElement("div").style,"AnimationEvent"in window||(delete ar.animationend.animation,delete ar.animationiteration.animation,delete ar.animationstart.animation),"TransitionEvent"in window||delete ar.transitionend.transition);function ms(t){if(af[t])return af[t];if(!ar[t])return t;var n=ar[t],a;for(a in n)if(n.hasOwnProperty(a)&&a in Dm)return af[t]=n[a];return t}var Um=ms("animationend"),Nm=ms("animationiteration"),Lm=ms("animationstart"),Vy=ms("transitionrun"),Xy=ms("transitionstart"),Yy=ms("transitioncancel"),Om=ms("transitionend"),Pm=new Map,sf="abort auxClick beforeToggle cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error fullscreenChange fullscreenError gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");sf.push("scrollEnd");function Ei(t,n){Pm.set(t,n),$i(n,[t])}var ky=0;function ia(t,n){if(t.name!=null&&t.name!=="auto")return t.name;if(n.autoName!==null)return n.autoName;t=Ri.identifierPrefix;var a=ky++;return t="_"+t+"t_"+a.toString(32)+"_",n.autoName=t}function zm(t){if(t==null||typeof t=="string")return t;var n=null,a=Tr;if(a!==null)for(var s=0;s<a.length;s++){var l=t[a[s]];if(l!=null){if(l==="none")return"none";n=n==null?l:n+(" "+l)}}return n??t.default}function aa(t,n){return t=zm(t),n=zm(n),n==null?t==="auto"?null:t:n==="auto"?null:n}var Ll=typeof reportError=="function"?reportError:function(t){if(typeof window=="object"&&typeof window.ErrorEvent=="function"){var n=new window.ErrorEvent("error",{bubbles:!0,cancelable:!0,message:typeof t=="object"&&t!==null&&typeof t.message=="string"?String(t.message):String(t),error:t});if(!window.dispatchEvent(n))return}else if(typeof process=="object"&&typeof process.emit=="function"){process.emit("uncaughtException",t);return}console.error(t)},ci=[],sr=0,rf=0;function Ol(){for(var t=sr,n=rf=sr=0;n<t;){var a=ci[n];ci[n++]=null;var s=ci[n];ci[n++]=null;var l=ci[n];ci[n++]=null;var c=ci[n];if(ci[n++]=null,s!==null&&l!==null){var m=s.pending;m===null?l.next=l:(l.next=m.next,m.next=l),s.pending=l}c!==0&&Im(a,l,c)}}function Pl(t,n,a,s){ci[sr++]=t,ci[sr++]=n,ci[sr++]=a,ci[sr++]=s,rf|=s,t.lanes|=s,t=t.alternate,t!==null&&(t.lanes|=s)}function of(t,n,a,s){return Pl(t,n,a,s),zl(t)}function _s(t,n){return Pl(t,null,null,n),zl(t)}function Im(t,n,a){t.lanes|=a;var s=t.alternate;s!==null&&(s.lanes|=a);for(var l=!1,c=t.return;c!==null;)c.childLanes|=a,s=c.alternate,s!==null&&(s.childLanes|=a),c.tag===22&&(t=c.stateNode,t===null||t._visibility&1||(l=!0)),t=c,c=c.return;return t.tag===3?(c=t.stateNode,l&&n!==null&&(l=31-Rn(a),t=c.hiddenUpdates,s=t[l],s===null?t[l]=[n]:s.push(n),n.lane=a|536870912),c):null}function zl(t){if(50<Yo)throw Yo=0,bu=null,Error(r(185));for(var n=t.return;n!==null;)t=n,n=t.return;return t.tag===3?t.stateNode:null}var rr={};function qy(t,n,a,s){this.tag=t,this.key=a,this.sibling=this.child=this.return=this.stateNode=this.type=this.elementType=null,this.index=0,this.refCleanup=this.ref=null,this.pendingProps=n,this.dependencies=this.memoizedState=this.updateQueue=this.memoizedProps=null,this.mode=s,this.subtreeFlags=this.flags=0,this.deletions=null,this.childLanes=this.lanes=0,this.alternate=null}function Gn(t,n,a,s){return new qy(t,n,a,s)}function lf(t){return t=t.prototype,!(!t||!t.isReactComponent)}function sa(t,n){var a=t.alternate;return a===null?(a=Gn(t.tag,n,t.key,t.mode),a.elementType=t.elementType,a.type=t.type,a.stateNode=t.stateNode,a.alternate=t,t.alternate=a):(a.pendingProps=n,a.type=t.type,a.flags=0,a.subtreeFlags=0,a.deletions=null),a.flags=t.flags&1206910976,a.childLanes=t.childLanes,a.lanes=t.lanes,a.child=t.child,a.memoizedProps=t.memoizedProps,a.memoizedState=t.memoizedState,a.updateQueue=t.updateQueue,n=t.dependencies,a.dependencies=n===null?null:{lanes:n.lanes,firstContext:n.firstContext},a.sibling=t.sibling,a.index=t.index,a.ref=t.ref,a.refCleanup=t.refCleanup,a}function Bm(t,n){t.flags&=1206910978;var a=t.alternate;return a===null?(t.childLanes=0,t.lanes=n,t.child=null,t.subtreeFlags=0,t.memoizedProps=null,t.memoizedState=null,t.updateQueue=null,t.dependencies=null,t.stateNode=null):(t.childLanes=a.childLanes,t.lanes=a.lanes,t.child=a.child,t.subtreeFlags=0,t.deletions=null,t.memoizedProps=a.memoizedProps,t.memoizedState=a.memoizedState,t.updateQueue=a.updateQueue,t.type=a.type,n=a.dependencies,t.dependencies=n===null?null:{lanes:n.lanes,firstContext:n.firstContext}),t}function Il(t,n,a,s,l,c){var m=0;if(s=t,typeof s=="function")lf(s)&&(m=1);else if(typeof s=="string")m=yM(t,a,Zt.current)?26:t==="html"||t==="head"||t==="body"?27:5;else t:switch(s){case Pt:return t=Gn(31,a,n,l),t.elementType=Pt,t.lanes=c,t;case w:return gs(a.children,l,c,n);case nt:m=8,l|=24;break;case rt:return t=Gn(12,a,n,l|2),t.elementType=rt,t.lanes=c,t;case at:return t=Gn(13,a,n,l),t.elementType=at,t.lanes=c,t;case Z:return t=Gn(19,a,n,l),t.elementType=Z,t.lanes=c,t;case oe:case D:return t=l|32,t=Gn(30,a,n,t),t.elementType=D,t.lanes=c,t.stateNode={autoName:null,paired:null,clones:null,ref:null},t;default:if(typeof s=="object"&&s!==null)switch(s.$$typeof){case ft:m=10;break t;case lt:m=9;break t;case H:m=11;break t;case yt:m=14;break t;case St:m=16,s=null;break t}m=29,a=Error(r(130,t===null?"null":typeof t,"")),s=null}return n=Gn(m,a,n,l),n.elementType=t,n.type=s,n.lanes=c,n}function gs(t,n,a,s){return t=Gn(7,t,s,n),t.lanes=a,t}function uf(t,n,a){return t=Gn(6,t,null,n),t.lanes=a,t}function Fm(t){var n=Gn(18,null,null,0);return n.stateNode=t,n}function cf(t,n,a){return n=Gn(4,t.children!==null?t.children:[],t.key,n),n.lanes=a,n.stateNode={containerInfo:t.containerInfo,pendingChildren:null,implementation:t.implementation},n}var Hm=new WeakMap;function fi(t,n){if(typeof t=="object"&&t!==null){var a=Hm.get(t);return a!==void 0?a:(n={value:t,source:n,stack:$t(n)},Hm.set(t,n),n)}return{value:t,source:n,stack:$t(n)}}var or=[],lr=0,Bl=null,Eo=0,hi=[],di=0,Ca=null,Bi=1,Fi="";function ra(t,n){or[lr++]=Eo,or[lr++]=Bl,Bl=t,Eo=n}function Gm(t,n,a){hi[di++]=Bi,hi[di++]=Fi,hi[di++]=Ca,Ca=t;var s=Bi;t=Fi;var l=32-Rn(s)-1;s&=~(1<<l),a+=1;var c=32-Rn(n)+l;if(30<c){var m=l-l%5;c=(s&(1<<m)-1).toString(32),s>>=m,l-=m,Bi=1<<32-Rn(n)+l|a<<l|s,Fi=c+t}else Bi=1<<c|a<<l|s,Fi=t}function Fl(t){t.return!==null&&(ra(t,1),Gm(t,1,0))}function ff(t){for(;t===Bl;)Bl=or[--lr],or[lr]=null,Eo=or[--lr],or[lr]=null;for(;t===Ca;)Ca=hi[--di],hi[di]=null,Fi=hi[--di],hi[di]=null,Bi=hi[--di],hi[di]=null}function Vm(t,n){hi[di++]=Bi,hi[di++]=Fi,hi[di++]=Ca,Bi=n.id,Fi=n.overflow,Ca=t}var dn=null,He=null,de=!1,wa=null,pi=!1,hf=Error(r(519));function Da(t){var n=Error(r(418,1<arguments.length&&arguments[1]!==void 0&&arguments[1]?"text":"HTML",""));throw To(fi(n,t)),hf}function Xm(t){var n=t.stateNode,a=t.type,s=t.memoizedProps;switch(n[Ut]=t,n[ie]=s,a){case"dialog":ge("cancel",n),ge("close",n);break;case"iframe":case"object":case"embed":ge("load",n);break;case"video":case"audio":for(a=0;a<qo.length;a++)ge(qo[a],n);break;case"source":ge("error",n);break;case"img":case"image":case"link":ge("error",n),ge("load",n);break;case"details":ge("toggle",n);break;case"input":ge("invalid",n),em(n,s.value,s.defaultValue,s.checked,s.defaultChecked,s.type,s.name,!0);break;case"select":ge("invalid",n);break;case"textarea":ge("invalid",n),im(n,s.value,s.defaultValue,s.children)}a=s.children,typeof a!="string"&&typeof a!="number"&&typeof a!="bigint"||n.textContent===""+a||s.suppressHydrationWarning===!0||c0(n.textContent,a)?(s.popover!=null&&(ge("beforetoggle",n),ge("toggle",n)),s.onScroll!=null&&ge("scroll",n),s.onScrollEnd!=null&&ge("scrollend",n),s.onClick!=null&&(n.onclick=Ii),n=!0):n=!1,n||Da(t,!0)}function Hl(t){for(dn=t.return;dn;)switch(dn.tag){case 5:case 31:case 13:pi=!1;return;case 27:case 3:pi=!0;return;default:dn=dn.return}}function ur(t){if(t!==dn)return!1;if(!de)return Hl(t),de=!0,!1;var n=t.tag,a;if((a=n!==3&&n!==27)&&((a=n===5)&&(a=t.type,a=!(a!=="form"&&a!=="button")||Vh(t.type,t.memoizedProps)),a=!a),a&&He&&Da(t),Hl(t),n===13){if(t=t.memoizedState,t=t!==null?t.dehydrated:null,!t)throw Error(r(317));He=w0(t)}else if(n===31){if(t=t.memoizedState,t=t!==null?t.dehydrated:null,!t)throw Error(r(317));He=w0(t)}else n===27?(n=He,qa(t.type)?(t=Qh,Qh=null,He=t):He=n):He=dn?_i(t.stateNode.nextSibling):null;return!0}function vs(){He=dn=null,de=!1}function df(){var t=wa;return t!==null&&(Yn===null?Yn=t:Yn.push.apply(Yn,t),wa=null),t}function To(t){wa===null?wa=[t]:wa.push(t)}var pf=ae(null),Ss=null,oa=null;function Ua(t,n,a){Kt(pf,n._currentValue),n._currentValue=a}function la(t){t._currentValue=pf.current,Xt(pf)}function Gl(t,n,a){for(;t!==null;){var s=t.alternate;if((t.childLanes&n)!==n?(t.childLanes|=n,s!==null&&(s.childLanes|=n)):s!==null&&(s.childLanes&n)!==n&&(s.childLanes|=n),t===a)break;t=t.return}}function mf(t,n,a,s){var l=t.child;for(l!==null&&(l.return=t);l!==null;){var c=l.dependencies;if(c!==null){var m=l.child;c=c.firstContext;t:for(;c!==null;){var b=c;c=l;for(var z=0;z<n.length;z++)if(b.context===n[z]){c.lanes|=a,b=c.alternate,b!==null&&(b.lanes|=a),Gl(c.return,a,t),s||(m=null);break t}c=b.next}}else if(l.tag===18){if(m=l.return,m===null)throw Error(r(341));m.lanes|=a,c=m.alternate,c!==null&&(c.lanes|=a),Gl(m,a,t),m=null}else l.tag===13&&l.memoizedState!==null&&l.memoizedState.dehydrated===null?(l.lanes|=a,m=l.alternate,m!==null&&(m.lanes|=a),Gl(l.return,a,t),m=l.child,m=m!==null?m.sibling:null):m=l.child;if(m!==null)m.return=l;else for(m=l;m!==null;){if(m===t){m=null;break}if(l=m.sibling,l!==null){l.return=m.return,m=l;break}m=m.return}l=m}}function ys(t,n,a,s){t=null;for(var l=n,c=!1;l!==null;){if(!c){if((l.flags&524288)!==0)c=!0;else if((l.flags&262144)!==0)break}if(l.tag===10){var m=l.alternate;if(m===null)throw Error(r(387));if(m=m.memoizedProps,m!==null){var b=l.type;$n(l.pendingProps.value,m.value)||(t!==null?t.push(b):t=[b])}}else if(l===tt.current){if(m=l.alternate,m===null)throw Error(r(387));m.memoizedState.memoizedState!==l.memoizedState.memoizedState&&(t!==null?t.push(Or):t=[Or])}l=l.return}return t!==null&&mf(n,t,a,s),n.flags|=262144,t!==null}function Vl(t){for(t=t.firstContext;t!==null;){if(!$n(t.context._currentValue,t.memoizedValue))return!0;t=t.next}return!1}function xs(t){Ss=t,oa=null,t=t.dependencies,t!==null&&(t.firstContext=null)}function Sn(t){return Ym(Ss,t)}function Xl(t,n){return Ss===null&&xs(t),Ym(t,n)}function Ym(t,n){var a=n._currentValue;if(n={context:n,memoizedValue:a,next:null},oa===null){if(t===null)throw Error(r(308));oa=n,t.dependencies={lanes:0,firstContext:n},t.flags|=524288}else oa=oa.next=n;return a}var Wy=typeof AbortController<"u"?AbortController:function(){var t=[],n=this.signal={aborted:!1,addEventListener:function(a,s){t.push(s)}};this.abort=function(){n.aborted=!0,t.forEach(function(a){return a()})}},jy=o.unstable_scheduleCallback,Zy=o.unstable_NormalPriority,nn={$$typeof:ft,Consumer:null,Provider:null,_currentValue:null,_currentValue2:null,_threadCount:0};function _f(){return{controller:new Wy,data:new Map,refCount:0}}function bo(t){t.refCount--,t.refCount===0&&jy(Zy,function(){t.controller.abort()})}function km(t,n){if((t.pendingLanes&4194048)!==0){var a=t.transitionTypes;for(a===null&&(a=t.transitionTypes=[]),t=0;t<n.length;t++){var s=n[t];a.indexOf(s)===-1&&a.push(s)}}}var Ao=null;function Ky(t){var n=t.transitionTypes;return t.transitionTypes=null,n}var Ro=null,gf=0,Ms=0,cr=null;function Qy(t,n){if(Ro===null){var a=Ro=[];gf=0,Ms=Lh(),cr={status:"pending",value:void 0,then:function(s){a.push(s)}}}return gf++,n.then(qm,qm),n}function qm(){if(--gf===0&&(Ao=null,Ro!==null)){cr!==null&&(cr.status="fulfilled");var t=Ro;Ro=null,Ms=0,cr=null;for(var n=0;n<t.length;n++)(0,t[n])()}}function Jy(t,n){var a=[],s={status:"pending",value:null,reason:null,then:function(l){a.push(l)}};return t.then(function(){s.status="fulfilled",s.value=n;for(var l=0;l<a.length;l++)(0,a[l])(n)},function(l){for(s.status="rejected",s.reason=l,l=0;l<a.length;l++)(0,a[l])(void 0)}),s}var Wm=Mt.S;Mt.S=function(t,n){if(Fg=Tt(),typeof n=="object"&&n!==null&&typeof n.then=="function"&&Qy(t,n),Ao!==null)for(var a=Cr;a!==null;)km(a,Ao),a=a.next;if(a=t.types,a!==null){for(var s=Cr;s!==null;)km(s,a),s=s.next;if(Ms!==0){s=Ao,s===null&&(s=Ao=[]);for(var l=0;l<a.length;l++){var c=a[l];s.indexOf(c)===-1&&s.push(c)}}}Wm!==null&&Wm(t,n)};var Es=ae(null);function vf(){var t=Es.current;return t!==null?t:Fe.pooledCache}function Yl(t,n){n===null?Kt(Es,Es.current):Kt(Es,n.pool)}function jm(){var t=vf();return t===null?null:{parent:nn._currentValue,pool:t}}var fr=Error(r(460)),Sf=Error(r(474)),kl=Error(r(542)),ql={then:function(){}};function Zm(t){return t=t.status,t==="fulfilled"||t==="rejected"}function Km(t,n,a){switch(a=t[a],a===void 0?t.push(n):a!==n&&(n.then(Ii,Ii),n=a),n.status){case"fulfilled":return n.value;case"rejected":throw t=n.reason,Jm(t),t===void 0&&!("reason"in n)?Error(r(600)):t;default:if(typeof n.status=="string")n.then(Ii,Ii);else{if(t=Fe,t!==null&&100<t.shellSuspendCounter)throw Error(r(482));t=n,t.status="pending",t.then(function(s){if(n.status==="pending"){var l=n;l.status="fulfilled",l.value=s}},function(s){if(n.status==="pending"){var l=n;l.status="rejected",l.reason=s}})}switch(n.status){case"fulfilled":return n.value;case"rejected":throw t=n.reason,Jm(t),t}throw bs=n,fr}}function Ts(t){try{var n=t._init;return n(t._payload)}catch(a){throw a!==null&&typeof a=="object"&&typeof a.then=="function"?(bs=a,fr):a}}var bs=null;function Qm(){if(bs===null)throw Error(r(459));var t=bs;return bs=null,t}function Jm(t){if(t===fr||t===kl)throw Error(r(483))}var hr=null,Co=0;function Wl(t){var n=Co;return Co+=1,hr===null&&(hr=[]),Km(hr,t,n)}function Na(t,n){n=n.props.ref,t.ref=n!==void 0?n:null}function jl(t,n){throw n.$$typeof===V?Error(r(525)):(t=Object.prototype.toString.call(n),Error(r(31,t==="[object Object]"?"object with keys {"+Object.keys(n).join(", ")+"}":t)))}function $m(t){function n(q,I){if(t){var K=q.deletions;K===null?(q.deletions=[I],q.flags|=16):K.push(I)}}function a(q,I){if(!t)return null;for(;I!==null;)n(q,I),I=I.sibling;return null}function s(q){for(var I=new Map;q!==null;)q.key===null?I.set(q.index,q):I.set(q.key,q),q=q.sibling;return I}function l(q,I){return q=sa(q,I),q.index=0,q.sibling=null,q}function c(q,I,K){return q.index=K,t?(K=q.alternate,K!==null?(K=K.index,K<I?(q.flags|=2,I):K):(q.flags|=134217730,I)):(q.flags|=1048576,I)}function m(q){return t&&q.alternate===null&&(q.flags|=134217730),q}function b(q,I,K,ut){return I===null||I.tag!==6?(I=uf(K,q.mode,ut),I.return=q,I):(I=l(I,K),I.return=q,I)}function z(q,I,K,ut){var zt=K.type;return zt===w?(q=et(q,I,K.props.children,ut,K.key),Na(q,K),q):I!==null&&(I.elementType===zt||typeof zt=="object"&&zt!==null&&zt.$$typeof===St&&Ts(zt)===I.type)?(I=l(I,K.props),Na(I,K),I.return=q,I):(I=Il(K.type,K.key,K.props,null,q.mode,ut),Na(I,K),I.return=q,I)}function W(q,I,K,ut){return I===null||I.tag!==4||I.stateNode.containerInfo!==K.containerInfo||I.stateNode.implementation!==K.implementation?(I=cf(K,q.mode,ut),I.return=q,I):(I=l(I,K.children||[]),I.return=q,I)}function et(q,I,K,ut,zt){return I===null||I.tag!==7?(I=gs(K,q.mode,ut,zt),I.return=q,I):(I=l(I,K),I.return=q,I)}function ct(q,I,K){if(typeof I=="string"&&I!==""||typeof I=="number"||typeof I=="bigint")return I=uf(""+I,q.mode,K),I.return=q,I;if(typeof I=="object"&&I!==null){switch(I.$$typeof){case gt:return K=Il(I.type,I.key,I.props,null,q.mode,K),Na(K,I),K.return=q,K;case T:return I=cf(I,q.mode,K),I.return=q,I;case St:return I=Ts(I),ct(q,I,K)}if(Ht(I)||ht(I))return I=gs(I,q.mode,K,null),I.return=q,I;if(typeof I.then=="function")return ct(q,Wl(I),K);if(I.$$typeof===ft)return ct(q,Xl(q,I),K);jl(q,I)}return null}function G(q,I,K,ut){var zt=I!==null?I.key:null;if(typeof K=="string"&&K!==""||typeof K=="number"||typeof K=="bigint")return zt!==null?null:b(q,I,""+K,ut);if(typeof K=="object"&&K!==null){switch(K.$$typeof){case gt:return K.key===zt?z(q,I,K,ut):null;case T:return K.key===zt?W(q,I,K,ut):null;case St:return K=Ts(K),G(q,I,K,ut)}if(Ht(K)||ht(K))return zt!==null?null:et(q,I,K,ut,null);if(typeof K.then=="function")return G(q,I,Wl(K),ut);if(K.$$typeof===ft)return G(q,I,Xl(q,K),ut);jl(q,K)}return null}function $(q,I,K,ut,zt){if(typeof ut=="string"&&ut!==""||typeof ut=="number"||typeof ut=="bigint")return q=q.get(K)||null,b(I,q,""+ut,zt);if(typeof ut=="object"&&ut!==null){switch(ut.$$typeof){case gt:return q=q.get(ut.key===null?K:ut.key)||null,z(I,q,ut,zt);case T:return q=q.get(ut.key===null?K:ut.key)||null,W(I,q,ut,zt);case St:return ut=Ts(ut),$(q,I,K,ut,zt)}if(Ht(ut)||ht(ut))return q=q.get(K)||null,et(I,q,ut,zt,null);if(typeof ut.then=="function")return $(q,I,K,Wl(ut),zt);if(ut.$$typeof===ft)return $(q,I,K,Xl(I,ut),zt);jl(I,ut)}return null}function At(q,I,K,ut){for(var zt=null,Se=null,Wt=I,Jt=I=0,rn=null;Wt!==null&&Jt<K.length;Jt++){Wt.index>Jt?(rn=Wt,Wt=null):rn=Wt.sibling;var Ee=G(q,Wt,K[Jt],ut);if(Ee===null){Wt===null&&(Wt=rn);break}t&&Wt&&Ee.alternate===null&&n(q,Wt),I=c(Ee,I,Jt),Se===null?zt=Ee:Se.sibling=Ee,Se=Ee,Wt=rn}if(Jt===K.length)return a(q,Wt),de&&ra(q,Jt),zt;if(Wt===null){for(;Jt<K.length;Jt++)Wt=ct(q,K[Jt],ut),Wt!==null&&(I=c(Wt,I,Jt),Se===null?zt=Wt:Se.sibling=Wt,Se=Wt);return de&&ra(q,Jt),zt}for(Wt=s(Wt);Jt<K.length;Jt++)rn=$(Wt,q,Jt,K[Jt],ut),rn!==null&&(t&&(Ee=rn.alternate,Ee!==null&&Wt.delete(Ee.key===null?Jt:Ee.key)),I=c(rn,I,Jt),Se===null?zt=rn:Se.sibling=rn,Se=rn);return t&&Wt.forEach(function(Qa){return n(q,Qa)}),de&&ra(q,Jt),zt}function Vt(q,I,K,ut){if(K==null)throw Error(r(151));for(var zt=null,Se=null,Wt=I,Jt=I=0,rn=null,Ee=K.next();Wt!==null&&!Ee.done;Jt++,Ee=K.next()){Wt.index>Jt?(rn=Wt,Wt=null):rn=Wt.sibling;var Qa=G(q,Wt,Ee.value,ut);if(Qa===null){Wt===null&&(Wt=rn);break}t&&Wt&&Qa.alternate===null&&n(q,Wt),I=c(Qa,I,Jt),Se===null?zt=Qa:Se.sibling=Qa,Se=Qa,Wt=rn}if(Ee.done)return a(q,Wt),de&&ra(q,Jt),zt;if(Wt===null){for(;!Ee.done;Jt++,Ee=K.next())Ee=ct(q,Ee.value,ut),Ee!==null&&(I=c(Ee,I,Jt),Se===null?zt=Ee:Se.sibling=Ee,Se=Ee);return de&&ra(q,Jt),zt}for(Wt=s(Wt);!Ee.done;Jt++,Ee=K.next())Ee=$(Wt,q,Jt,Ee.value,ut),Ee!==null&&(t&&(rn=Ee.alternate,rn!==null&&Wt.delete(rn.key===null?Jt:rn.key)),I=c(Ee,I,Jt),Se===null?zt=Ee:Se.sibling=Ee,Se=Ee);return t&&Wt.forEach(function(NM){return n(q,NM)}),de&&ra(q,Jt),zt}function re(q,I,K,ut){if(typeof K=="object"&&K!==null&&K.type===w&&K.key===null&&K.props.ref===void 0&&(K=K.props.children),typeof K=="object"&&K!==null){switch(K.$$typeof){case gt:t:{for(var zt=K.key;I!==null;){if(I.key===zt){if(zt=K.type,zt===w){if(I.tag===7){a(q,I.sibling),ut=l(I,K.props.children),Na(ut,K),ut.return=q,q=ut;break t}}else if(I.elementType===zt||typeof zt=="object"&&zt!==null&&zt.$$typeof===St&&Ts(zt)===I.type){a(q,I.sibling),ut=l(I,K.props),Na(ut,K),ut.return=q,q=ut;break t}a(q,I);break}else n(q,I);I=I.sibling}K.type===w?(ut=gs(K.props.children,q.mode,ut,K.key),Na(ut,K),ut.return=q,q=ut):(ut=Il(K.type,K.key,K.props,null,q.mode,ut),Na(ut,K),ut.return=q,q=ut)}return m(q);case T:t:{for(zt=K.key;I!==null;){if(I.key===zt)if(I.tag===4&&I.stateNode.containerInfo===K.containerInfo&&I.stateNode.implementation===K.implementation){a(q,I.sibling),ut=l(I,K.children||[]),ut.return=q,q=ut;break t}else{a(q,I);break}else n(q,I);I=I.sibling}ut=cf(K,q.mode,ut),ut.return=q,q=ut}return m(q);case St:return K=Ts(K),re(q,I,K,ut)}if(Ht(K))return At(q,I,K,ut);if(ht(K)){if(zt=ht(K),typeof zt!="function")throw Error(r(150));return K=zt.call(K),Vt(q,I,K,ut)}if(typeof K.then=="function")return re(q,I,Wl(K),ut);if(K.$$typeof===ft)return re(q,I,Xl(q,K),ut);jl(q,K)}return typeof K=="string"&&K!==""||typeof K=="number"||typeof K=="bigint"?(K=""+K,I!==null&&I.tag===6?(a(q,I.sibling),ut=l(I,K),ut.return=q,q=ut):(a(q,I),ut=uf(K,q.mode,ut),ut.return=q,q=ut),m(q)):a(q,I)}return function(q,I,K,ut){try{Co=0;var zt=re(q,I,K,ut);return hr=null,zt}catch(Wt){if(Wt===fr||Wt===kl)throw Wt;var Se=Gn(29,Wt,null,q.mode);return Se.lanes=ut,Se.return=q,Se}}}var As=$m(!0),t_=$m(!1),La=!1;function yf(t){t.updateQueue={baseState:t.memoizedState,firstBaseUpdate:null,lastBaseUpdate:null,shared:{pending:null,lanes:0,hiddenCallbacks:null},callbacks:null}}function xf(t,n){t=t.updateQueue,n.updateQueue===t&&(n.updateQueue={baseState:t.baseState,firstBaseUpdate:t.firstBaseUpdate,lastBaseUpdate:t.lastBaseUpdate,shared:t.shared,callbacks:null})}function Oa(t){return{lane:t,tag:0,payload:null,callback:null,next:null}}function Pa(t,n,a){var s=t.updateQueue;if(s===null)return null;if(s=s.shared,(Ce&2)!==0){var l=s.pending;return l===null?n.next=n:(n.next=l.next,l.next=n),s.pending=n,n=zl(t),Im(t,null,a),n}return Pl(t,s,n,a),zl(t)}function wo(t,n,a){if(n=n.updateQueue,n!==null&&(n=n.shared,(a&4194048)!==0)){var s=n.lanes;s&=t.pendingLanes,a|=s,n.lanes=a,j(t,a)}}function Mf(t,n){var a=t.updateQueue,s=t.alternate;if(s!==null&&(s=s.updateQueue,a===s)){var l=null,c=null;if(a=a.firstBaseUpdate,a!==null){do{var m={lane:a.lane,tag:a.tag,payload:a.payload,callback:null,next:null};c===null?l=c=m:c=c.next=m,a=a.next}while(a!==null);c===null?l=c=n:c=c.next=n}else l=c=n;a={baseState:s.baseState,firstBaseUpdate:l,lastBaseUpdate:c,shared:s.shared,callbacks:s.callbacks},t.updateQueue=a;return}t=a.lastBaseUpdate,t===null?a.firstBaseUpdate=n:t.next=n,a.lastBaseUpdate=n}var Ef=!1;function Do(){if(Ef){var t=cr;if(t!==null)throw t}}function Uo(t,n,a,s){Ef=!1;var l=t.updateQueue;La=!1;var c=l.firstBaseUpdate,m=l.lastBaseUpdate,b=l.shared.pending;if(b!==null){l.shared.pending=null;var z=b,W=z.next;z.next=null,m===null?c=W:m.next=W,m=z;var et=t.alternate;et!==null&&(et=et.updateQueue,b=et.lastBaseUpdate,b!==m&&(b===null?et.firstBaseUpdate=W:b.next=W,et.lastBaseUpdate=z))}if(c!==null){var ct=l.baseState;m=0,et=W=z=null,b=c;do{var G=b.lane&-536870913,$=G!==b.lane;if($?(ve&G)===G:(s&G)===G){G!==0&&G===Ms&&(Ef=!0),et!==null&&(et=et.next={lane:0,tag:b.tag,payload:b.payload,callback:null,next:null});t:{var At=t,Vt=b;G=n;var re=a;switch(Vt.tag){case 1:if(At=Vt.payload,typeof At=="function"){ct=At.call(re,ct,G);break t}ct=At;break t;case 3:At.flags=At.flags&-65537|128;case 0:if(At=Vt.payload,G=typeof At=="function"?At.call(re,ct,G):At,G==null)break t;ct=O({},ct,G);break t;case 2:La=!0}}G=b.callback,G!==null&&(t.flags|=64,$&&(t.flags|=8192),$=l.callbacks,$===null?l.callbacks=[G]:$.push(G))}else $={lane:G,tag:b.tag,payload:b.payload,callback:b.callback,next:null},et===null?(W=et=$,z=ct):et=et.next=$,m|=G;if(b=b.next,b===null){if(b=l.shared.pending,b===null)break;$=b,b=$.next,$.next=null,l.lastBaseUpdate=$,l.shared.pending=null}}while(!0);et===null&&(z=ct),l.baseState=z,l.firstBaseUpdate=W,l.lastBaseUpdate=et,c===null&&(l.shared.lanes=0),Va|=m,t.lanes=m,t.memoizedState=ct}}function e_(t,n){if(typeof t!="function")throw Error(r(191,t));t.call(n)}function n_(t,n){var a=t.callbacks;if(a!==null)for(t.callbacks=null,t=0;t<a.length;t++)e_(a[t],n)}var za=ae(null),Zl=ae(0);function i_(t,n){t=da,Kt(Zl,t),Kt(za,n),da=t|n.baseLanes}function Tf(){Kt(Zl,da),Kt(za,za.current)}function bf(){da=Zl.current,Xt(za),Xt(Zl)}var yn=ae(null),wn=null;function Ia(t){var n=t.alternate;Kt(xn,xn.current&1),Kt(yn,t),wn===null&&(n===null||za.current!==null||n.memoizedState!==null)&&(wn=t)}function Af(t){Kt(xn,xn.current),Kt(yn,t),wn===null&&(wn=t)}function a_(t){t.tag===22?(Kt(xn,xn.current),Kt(yn,t),wn===null&&(wn=t)):Ba()}function Ba(){Kt(xn,xn.current),Kt(yn,yn.current)}function ti(t){Xt(yn),wn===t&&(wn=null),Xt(xn)}var xn=ae(0);function No(t,n){Kt(yn,yn.current),Kt(xn,n)}function Rf(t){Xt(xn),Xt(yn),wn===t&&(wn=null)}function Kl(t){for(var n=t;n!==null;){if(n.tag===13){var a=n.memoizedState;if(a!==null&&(a=a.dehydrated,a===null||Zh(a)||Kh(a)))return n}else if(n.tag===19&&n.memoizedProps.revealOrder!=="independent"){if((n.flags&128)!==0)return n}else if(n.child!==null){n.child.return=n,n=n.child;continue}if(n===t)break;for(;n.sibling===null;){if(n.return===null||n.return===t)return null;n=n.return}n.sibling.return=n.return,n=n.sibling}return null}var ua=0,se=null,ze=null,an=null,Ql=!1,dr=!1,Rs=!1,Jl=0,Lo=0,pr=null,$y=0;function Ke(){throw Error(r(321))}function Cf(t,n){if(n===null)return!1;for(var a=0;a<n.length&&a<t.length;a++)if(!$n(t[a],n[a]))return!1;return!0}function wf(t,n,a,s,l,c){return ua=c,se=n,n.memoizedState=null,n.updateQueue=null,n.lanes=0,Mt.H=t===null||t.memoizedState===null?G_:V_,Rs=!1,c=a(s,l),Rs=!1,dr&&(c=r_(n,a,s,l)),s_(t),c}function s_(t){Mt.H=su;var n=ze!==null&&ze.next!==null;if(ua=0,an=ze=se=null,Ql=!1,Lo=0,pr=null,n)throw Error(r(300));t===null||sn||(t=t.dependencies,t!==null&&Vl(t)&&(sn=!0))}function r_(t,n,a,s){se=t;var l=0;do{if(dr&&(pr=null),Lo=0,dr=!1,25<=l)throw Error(r(301));if(l+=1,an=ze=null,t.updateQueue!=null){var c=t.updateQueue;c.lastEffect=null,c.events=null,c.stores=null,c.memoCache!=null&&(c.memoCache.index=0)}Mt.H=ox,c=n(a,s)}while(dr);return c}function tx(){var t=Mt.H,n=t.useState()[0];return n=typeof n.then=="function"?Oo(n):n,t=t.useState()[0],(ze!==null?ze.memoizedState:null)!==t&&(se.flags|=1024),n}function Df(){var t=Jl!==0;return Jl=0,t}function Uf(t,n,a){n.updateQueue=t.updateQueue,n.flags&=-2053,t.lanes&=~a}function Nf(t){if(Ql){for(t=t.memoizedState;t!==null;){var n=t.queue;n!==null&&(n.pending=null),t=t.next}Ql=!1}ua=0,an=ze=se=null,dr=!1,Lo=Jl=0,pr=null}function Pn(){var t={memoizedState:null,baseState:null,baseQueue:null,queue:null,next:null};return an===null?se.memoizedState=an=t:an=an.next=t,an}function $e(){if(ze===null){var t=se.alternate;t=t!==null?t.memoizedState:null}else t=ze.next;var n=an===null?se.memoizedState:an.next;if(n!==null)an=n,ze=t;else{if(t===null)throw se.alternate===null?Error(r(467)):Error(r(310));ze=t,t={memoizedState:ze.memoizedState,baseState:ze.baseState,baseQueue:ze.baseQueue,queue:ze.queue,next:null},an===null?se.memoizedState=an=t:an=an.next=t}return an}function $l(){return{lastEffect:null,events:null,stores:null,memoCache:null}}function Oo(t){var n=Lo;return Lo+=1,pr===null&&(pr=[]),t=Km(pr,t,n),n=se,(an===null?n.memoizedState:an.next)===null&&(n=n.alternate,Mt.H=n===null||n.memoizedState===null?G_:V_),t}function tu(t){if(t!==null&&typeof t=="object"){if(typeof t.then=="function")return Oo(t);if(t.$$typeof===X)return;if(t.$$typeof===ft)return Sn(t)}throw Error(r(438,String(t)))}function Lf(t){var n=null,a=se.updateQueue;if(a!==null&&(n=a.memoCache),n==null){var s=se.alternate;s!==null&&(s=s.updateQueue,s!==null&&(s=s.memoCache,s!=null&&(n={data:s.data.map(function(l){return l.slice()}),index:0})))}if(n==null&&(n={data:[],index:0}),a===null&&(a=$l(),se.updateQueue=a),a.memoCache=n,a=n.data[n.index],a===void 0)for(a=n.data[n.index]=Array(t),s=0;s<t;s++)a[s]=me;return n.index++,a}function ca(t,n){return typeof n=="function"?n(t):n}function eu(t){var n=$e();return Of(n,ze,t)}function Of(t,n,a){var s=t.queue;if(s===null)throw Error(r(311));s.lastRenderedReducer=a;var l=t.baseQueue,c=s.pending;if(c!==null){if(l!==null){var m=l.next;l.next=c.next,c.next=m}n.baseQueue=l=c,s.pending=null}if(c=t.baseState,l===null)t.memoizedState=c;else{n=l.next;var b=m=null,z=null,W=n,et=!1;do{var ct=W.lane&-536870913;if(ct!==W.lane?(ve&ct)===ct:(ua&ct)===ct){var G=W.revertLane;if(G===0)z!==null&&(z=z.next={lane:0,revertLane:0,gesture:null,action:W.action,hasEagerState:W.hasEagerState,eagerState:W.eagerState,next:null}),ct===Ms&&(et=!0);else if((ua&G)===G){W=W.next,G===Ms&&(et=!0);continue}else ct={lane:0,revertLane:W.revertLane,gesture:null,action:W.action,hasEagerState:W.hasEagerState,eagerState:W.eagerState,next:null},z===null?(b=z=ct,m=c):z=z.next=ct,se.lanes|=G,Va|=G;ct=W.action,Rs&&a(c,ct),c=W.hasEagerState?W.eagerState:a(c,ct)}else G={lane:ct,revertLane:W.revertLane,gesture:W.gesture,action:W.action,hasEagerState:W.hasEagerState,eagerState:W.eagerState,next:null},z===null?(b=z=G,m=c):z=z.next=G,se.lanes|=ct,Va|=ct;W=W.next}while(W!==null&&W!==n);if(z===null?m=c:z.next=b,!$n(c,t.memoizedState)&&(sn=!0,et&&(a=cr,a!==null)))throw a;t.memoizedState=c,t.baseState=m,t.baseQueue=z,s.lastRenderedState=c}return l===null&&(s.lanes=0),[t.memoizedState,s.dispatch]}function Pf(t){var n=$e(),a=n.queue;if(a===null)throw Error(r(311));a.lastRenderedReducer=t;var s=a.dispatch,l=a.pending,c=n.memoizedState;if(l!==null){a.pending=null;var m=l=l.next;do c=t(c,m.action),m=m.next;while(m!==l);$n(c,n.memoizedState)||(sn=!0),n.memoizedState=c,n.baseQueue===null&&(n.baseState=c),a.lastRenderedState=c}return[c,s]}function o_(t,n,a){var s=se,l=$e(),c=de;if(c){if(a===void 0)throw Error(r(407));a=a()}else a=n();var m=!$n((ze||l).memoizedState,a);if(m&&(l.memoizedState=a,sn=!0),l=l.queue,Bf(c_.bind(null,s,l,t),[t]),t=l.getSnapshot!==n||m||an!==null&&(an.memoizedState.tag&1)!==0,mr(t?9:8,{destroy:void 0},u_.bind(null,s,l,a,n),null),t){if(s.flags|=2048,Fe===null)throw Error(r(349));c||(ua&127)!==0||l_(s,n,a)}return a}function l_(t,n,a){t.flags|=16384,t={getSnapshot:n,value:a},n=se.updateQueue,n===null?(n=$l(),se.updateQueue=n,n.stores=[t]):(a=n.stores,a===null?n.stores=[t]:a.push(t))}function u_(t,n,a,s){n.value=a,n.getSnapshot=s,f_(n)&&h_(t)}function c_(t,n,a){return a(function(){f_(n)&&h_(t)})}function f_(t){var n=t.getSnapshot;t=t.value;try{var a=n();return!$n(t,a)}catch{return!0}}function h_(t){var n=_s(t,2);n!==null&&kn(n,t,2)}function zf(t){var n=Pn();if(typeof t=="function"){var a=t;if(t=a(),Rs){Mi(!0);try{a()}finally{Mi(!1)}}}return n.memoizedState=n.baseState=t,n.queue={pending:null,lanes:0,dispatch:null,lastRenderedReducer:ca,lastRenderedState:t},n}function d_(t,n,a,s){return t.baseState=a,Of(t,ze,typeof s=="function"?s:ca)}function ex(t,n,a,s,l){if(au(t))throw Error(r(485));if(t=n.action,t!==null){var c={payload:l,action:t,next:null,isTransition:!0,status:"pending",value:null,reason:null,listeners:[],then:function(m){c.listeners.push(m)}};Mt.T!==null?a(!0):c.isTransition=!1,s(c),a=n.pending,a===null?(c.next=n.pending=c,p_(n,c)):(c.next=a.next,n.pending=a.next=c)}}function p_(t,n){var a=n.action,s=n.payload,l=t.state;if(n.isTransition){var c=Mt.T,m={};m.types=c!==null?c.types:null,Mt.T=m;try{var b=a(l,s),z=Mt.S;z!==null&&z(m,b),m_(t,n,b)}catch(W){If(t,n,W)}finally{c!==null&&m.types!==null&&(c.types=m.types),Mt.T=c}}else try{c=a(l,s),m_(t,n,c)}catch(W){If(t,n,W)}}function m_(t,n,a){a!==null&&typeof a=="object"&&typeof a.then=="function"?a.then(function(s){__(t,n,s)},function(s){return If(t,n,s)}):__(t,n,a)}function __(t,n,a){n.status="fulfilled",n.value=a,g_(n),t.state=a,n=t.pending,n!==null&&(a=n.next,a===n?t.pending=null:(a=a.next,n.next=a,p_(t,a)))}function If(t,n,a){var s=t.pending;if(t.pending=null,s!==null){s=s.next;do n.status="rejected",n.reason=a,g_(n),n=n.next;while(n!==s)}t.action=null}function g_(t){t=t.listeners;for(var n=0;n<t.length;n++)(0,t[n])()}function v_(t,n){return n}function S_(t,n){if(de){var a=Fe.formState;if(a!==null){t:{var s=se;if(de){if(He){e:{for(var l=He,c=pi;l.nodeType!==8;){if(!c){l=null;break e}if(l=_i(l.nextSibling),l===null){l=null;break e}}c=l.data,l=c==="F!"||c==="F"?l:null}if(l){He=_i(l.nextSibling),s=l.data==="F!";break t}}Da(s)}s=!1}s&&(n=a[0])}}return a=Pn(),a.memoizedState=a.baseState=n,s={pending:null,lanes:0,dispatch:null,lastRenderedReducer:v_,lastRenderedState:n},a.queue=s,a=B_.bind(null,se,s),s.dispatch=a,s=zf(!1),c=Xf.bind(null,se,!1,s.queue),s=Pn(),l={state:n,dispatch:null,action:t,pending:null},s.queue=l,a=ex.bind(null,se,l,c,a),l.dispatch=a,s.memoizedState=t,[n,a,!1]}function y_(t){var n=$e();return x_(n,ze,t)}function x_(t,n,a){if(n=Of(t,n,v_)[0],t=eu(ca)[0],typeof n=="object"&&n!==null&&typeof n.then=="function")try{var s=Oo(n)}catch(m){throw m===fr?kl:m}else s=n;n=$e();var l=n.queue,c=l.dispatch;return a!==n.memoizedState&&(se.flags|=2048,mr(9,{destroy:void 0},nx.bind(null,l,a),null)),[s,c,t]}function nx(t,n){t.action=n}function M_(t){var n=$e(),a=ze;if(a!==null)return x_(n,a,t);$e(),n=n.memoizedState,a=$e();var s=a.queue.dispatch;return a.memoizedState=t,[n,s,!1]}function mr(t,n,a,s){return t={tag:t,create:a,deps:s,inst:n,next:null},n=se.updateQueue,n===null&&(n=$l(),se.updateQueue=n),a=n.lastEffect,a===null?n.lastEffect=t.next=t:(s=a.next,a.next=t,t.next=s,n.lastEffect=t),t}function E_(){return $e().memoizedState}function nu(t,n,a,s){var l=Pn();se.flags|=t,l.memoizedState=mr(1|n,{destroy:void 0},a,s===void 0?null:s)}function iu(t,n,a,s){var l=$e();s=s===void 0?null:s;var c=l.memoizedState.inst;ze!==null&&s!==null&&Cf(s,ze.memoizedState.deps)?l.memoizedState=mr(n,c,a,s):(se.flags|=t,l.memoizedState=mr(1|n,c,a,s))}function T_(t,n){nu(8390656,8,t,n)}function Bf(t,n){iu(2048,8,t,n)}function ix(t){se.flags|=4;var n=se.updateQueue;if(n===null)n=$l(),se.updateQueue=n,n.events=[t];else{var a=n.events;a===null?n.events=[t]:a.push(t)}}function b_(t){var n=$e().memoizedState;return ix({ref:n,nextImpl:t}),function(){if((Ce&2)!==0)throw Error(r(440));return n.impl.apply(void 0,arguments)}}function A_(t,n){return iu(4,2,t,n)}function R_(t,n){return iu(4,4,t,n)}function C_(t,n){if(typeof n=="function"){t=t();var a=n(t);return function(){typeof a=="function"?a():n(null)}}if(n!=null)return t=t(),n.current=t,function(){n.current=null}}function w_(t,n,a){a=a!=null?a.concat([t]):null,iu(4,4,C_.bind(null,n,t),a)}function Ff(){}function D_(t,n){var a=$e();n=n===void 0?null:n;var s=a.memoizedState;return n!==null&&Cf(n,s[1])?s[0]:(a.memoizedState=[t,n],t)}function U_(t,n){var a=$e();n=n===void 0?null:n;var s=a.memoizedState;if(n!==null&&Cf(n,s[1]))return s[0];if(s=t(),Rs){Mi(!0);try{t()}finally{Mi(!1)}}return a.memoizedState=[s,n],s}function Hf(t,n,a){return a===void 0||(ua&1073741824)!==0&&(ve&261930)===0?t.memoizedState=n:(t.memoizedState=a,t=Gg(),se.lanes|=t,Va|=t,a)}function N_(t,n,a,s){return $n(a,n)?a:za.current!==null?(t=Hf(t,a,s),$n(t,n)||(sn=!0),t):(ua&106)===0||(ua&1073741824)!==0&&(ve&261930)===0?(sn=!0,t.memoizedState=a):(t=Gg(),se.lanes|=t,Va|=t,n)}function L_(t,n,a,s,l){var c=bt.p;bt.p=c!==0&&8>c?c:8;var m=Mt.T,b={};b.types=m!==null?m.types:null,Mt.T=b,Xf(t,!1,n,a);try{var z=l(),W=Mt.S;if(W!==null&&W(b,z),z!==null&&typeof z=="object"&&typeof z.then=="function"){var et=Jy(z,s);Po(t,n,et,ai(t))}else Po(t,n,s,ai(t))}catch(ct){Po(t,n,{then:function(){},status:"rejected",reason:ct},ai())}finally{bt.p=c,m!==null&&b.types!==null&&(m.types=b.types),Mt.T=m}}function ax(){}function Gf(t,n,a,s){if(t.tag!==5)throw Error(r(476));var l=O_(t).queue;L_(t,l,n,F,a===null?ax:function(){return P_(t),a(s)})}function O_(t){var n=t.memoizedState;if(n!==null)return n;n={memoizedState:F,baseState:F,baseQueue:null,queue:{pending:null,lanes:0,dispatch:null,lastRenderedReducer:ca,lastRenderedState:F},next:null};var a={};return n.next={memoizedState:a,baseState:a,baseQueue:null,queue:{pending:null,lanes:0,dispatch:null,lastRenderedReducer:ca,lastRenderedState:a},next:null},t.memoizedState=n,t=t.alternate,t!==null&&(t.memoizedState=n),n}function P_(t){var n=O_(t);n.next===null&&(n=t.alternate.memoizedState),Po(t,n.next.queue,{},ai())}function Vf(){return Sn(Or)}function z_(){return $e().memoizedState}function I_(){return $e().memoizedState}function sx(t){for(var n=t.return;n!==null;){switch(n.tag){case 24:case 3:var a=ai();t=Oa(a);var s=Pa(n,t,a);s!==null&&(kn(s,n,a),wo(s,n,a)),n={cache:_f()},t.payload=n;return}n=n.return}}function rx(t,n,a){var s=ai();a={lane:s,revertLane:0,gesture:null,action:a,hasEagerState:!1,eagerState:null,next:null},au(t)?F_(n,a):(a=of(t,n,a,s),a!==null&&(kn(a,t,s),H_(a,n,s)))}function B_(t,n,a){var s=ai();Po(t,n,a,s)}function Po(t,n,a,s){var l={lane:s,revertLane:0,gesture:null,action:a,hasEagerState:!1,eagerState:null,next:null};if(au(t))F_(n,l);else{var c=t.alternate;if(t.lanes===0&&(c===null||c.lanes===0)&&(c=n.lastRenderedReducer,c!==null))try{var m=n.lastRenderedState,b=c(m,a);if(l.hasEagerState=!0,l.eagerState=b,$n(b,m))return Pl(t,n,l,0),Fe===null&&Ol(),!1}catch{}if(a=of(t,n,l,s),a!==null)return kn(a,t,s),H_(a,n,s),!0}return!1}function Xf(t,n,a,s){if(s={lane:2,revertLane:Lh(),gesture:null,action:s,hasEagerState:!1,eagerState:null,next:null},au(t)){if(n)throw Error(r(479))}else n=of(t,a,s,2),n!==null&&kn(n,t,2)}function au(t){var n=t.alternate;return t===se||n!==null&&n===se}function F_(t,n){dr=Ql=!0;var a=t.pending;a===null?n.next=n:(n.next=a.next,a.next=n),t.pending=n}function H_(t,n,a){if((a&4194048)!==0){var s=n.lanes;s&=t.pendingLanes,a|=s,n.lanes=a,j(t,a)}}var su={readContext:Sn,use:tu,useCallback:Ke,useContext:Ke,useEffect:Ke,useImperativeHandle:Ke,useLayoutEffect:Ke,useInsertionEffect:Ke,useMemo:Ke,useReducer:Ke,useRef:Ke,useState:Ke,useDebugValue:Ke,useDeferredValue:Ke,useTransition:Ke,useSyncExternalStore:Ke,useId:Ke,useHostTransitionStatus:Ke,useFormState:Ke,useActionState:Ke,useOptimistic:Ke,useMemoCache:Ke,useCacheRefresh:Ke,useEffectEvent:Ke},G_={readContext:Sn,use:tu,useCallback:function(t,n){return Pn().memoizedState=[t,n===void 0?null:n],t},useContext:Sn,useEffect:T_,useImperativeHandle:function(t,n,a){a=a!=null?a.concat([t]):null,nu(4194308,4,C_.bind(null,n,t),a)},useLayoutEffect:function(t,n){return nu(4194308,4,t,n)},useInsertionEffect:function(t,n){nu(4,2,t,n)},useMemo:function(t,n){var a=Pn();n=n===void 0?null:n;var s=t();if(Rs){Mi(!0);try{t()}finally{Mi(!1)}}return a.memoizedState=[s,n],s},useReducer:function(t,n,a){var s=Pn();if(a!==void 0){var l=a(n);if(Rs){Mi(!0);try{a(n)}finally{Mi(!1)}}}else l=n;return s.memoizedState=s.baseState=l,t={pending:null,lanes:0,dispatch:null,lastRenderedReducer:t,lastRenderedState:l},s.queue=t,t=t.dispatch=rx.bind(null,se,t),[s.memoizedState,t]},useRef:function(t){var n=Pn();return t={current:t},n.memoizedState=t},useState:function(t){t=zf(t);var n=t.queue,a=B_.bind(null,se,n);return n.dispatch=a,[t.memoizedState,a]},useDebugValue:Ff,useDeferredValue:function(t,n){var a=Pn();return Hf(a,t,n)},useTransition:function(){var t=zf(!1);return t=L_.bind(null,se,t.queue,!0,!1),Pn().memoizedState=t,[!1,t]},useSyncExternalStore:function(t,n,a){var s=se,l=Pn();if(de){if(a===void 0)throw Error(r(407));a=a()}else{if(a=n(),Fe===null)throw Error(r(349));(ve&127)!==0||l_(s,n,a)}l.memoizedState=a;var c={value:a,getSnapshot:n};return l.queue=c,T_(c_.bind(null,s,c,t),[t]),s.flags|=2048,mr(9,{destroy:void 0},u_.bind(null,s,c,a,n),null),a},useId:function(){var t=Pn(),n=Fe.identifierPrefix;if(de){var a=Fi,s=Bi;a=(s&~(1<<32-Rn(s)-1)).toString(32)+a,n="_"+n+"R_"+a,a=Jl++,0<a&&(n+="H"+a.toString(32)),n+="_"}else a=$y++,n="_"+n+"r_"+a.toString(32)+"_";return t.memoizedState=n},useHostTransitionStatus:Vf,useFormState:S_,useActionState:S_,useOptimistic:function(t){var n=Pn();n.memoizedState=n.baseState=t;var a={pending:null,lanes:0,dispatch:null,lastRenderedReducer:null,lastRenderedState:null};return n.queue=a,n=Xf.bind(null,se,!0,a),a.dispatch=n,[t,n]},useMemoCache:Lf,useCacheRefresh:function(){return Pn().memoizedState=sx.bind(null,se)},useEffectEvent:function(t){var n=Pn(),a={impl:t};return n.memoizedState=a,function(){if((Ce&2)!==0)throw Error(r(440));return a.impl.apply(void 0,arguments)}}},V_={readContext:Sn,use:tu,useCallback:D_,useContext:Sn,useEffect:Bf,useImperativeHandle:w_,useInsertionEffect:A_,useLayoutEffect:R_,useMemo:U_,useReducer:eu,useRef:E_,useState:function(){return eu(ca)},useDebugValue:Ff,useDeferredValue:function(t,n){var a=$e();return N_(a,ze.memoizedState,t,n)},useTransition:function(){var t=eu(ca)[0],n=$e().memoizedState;return[typeof t=="boolean"?t:Oo(t),n]},useSyncExternalStore:o_,useId:z_,useHostTransitionStatus:Vf,useFormState:y_,useActionState:y_,useOptimistic:function(t,n){var a=$e();return d_(a,ze,t,n)},useMemoCache:Lf,useCacheRefresh:I_,useEffectEvent:b_},ox={readContext:Sn,use:tu,useCallback:D_,useContext:Sn,useEffect:Bf,useImperativeHandle:w_,useInsertionEffect:A_,useLayoutEffect:R_,useMemo:U_,useReducer:Pf,useRef:E_,useState:function(){return Pf(ca)},useDebugValue:Ff,useDeferredValue:function(t,n){var a=$e();return ze===null?Hf(a,t,n):N_(a,ze.memoizedState,t,n)},useTransition:function(){var t=Pf(ca)[0],n=$e().memoizedState;return[typeof t=="boolean"?t:Oo(t),n]},useSyncExternalStore:o_,useId:z_,useHostTransitionStatus:Vf,useFormState:M_,useActionState:M_,useOptimistic:function(t,n){var a=$e();return ze!==null?d_(a,ze,t,n):(a.baseState=t,[t,a.queue.dispatch])},useMemoCache:Lf,useCacheRefresh:I_,useEffectEvent:b_};function Yf(t,n,a,s){n=t.memoizedState,a=a(s,n),a=a==null?n:O({},n,a),t.memoizedState=a,t.lanes===0&&(t.updateQueue.baseState=a)}var kf={enqueueSetState:function(t,n,a){t=t._reactInternals;var s=ai(),l=Oa(s);l.payload=n,a!=null&&(l.callback=a),n=Pa(t,l,s),n!==null&&(kn(n,t,s),wo(n,t,s))},enqueueReplaceState:function(t,n,a){t=t._reactInternals;var s=ai(),l=Oa(s);l.tag=1,l.payload=n,a!=null&&(l.callback=a),n=Pa(t,l,s),n!==null&&(kn(n,t,s),wo(n,t,s))},enqueueForceUpdate:function(t,n){t=t._reactInternals;var a=ai(),s=Oa(a);s.tag=2,n!=null&&(s.callback=n),n=Pa(t,s,a),n!==null&&(kn(n,t,a),wo(n,t,a))}};function X_(t,n,a,s,l,c,m){return t=t.stateNode,typeof t.shouldComponentUpdate=="function"?t.shouldComponentUpdate(s,c,m):n.prototype&&n.prototype.isPureReactComponent?!xo(a,s)||!xo(l,c):!0}function Y_(t,n,a,s){t=n.state,typeof n.componentWillReceiveProps=="function"&&n.componentWillReceiveProps(a,s),typeof n.UNSAFE_componentWillReceiveProps=="function"&&n.UNSAFE_componentWillReceiveProps(a,s),n.state!==t&&kf.enqueueReplaceState(n,n.state,null)}function Cs(t,n){var a=n;if("ref"in n){a={};for(var s in n)s!=="ref"&&(a[s]=n[s])}if(t=t.defaultProps){a===n&&(a=O({},a));for(var l in t)a[l]===void 0&&(a[l]=t[l])}return a}function k_(t){Ll(t)}function q_(t){console.error(t)}function W_(t){Ll(t)}function ru(t,n){try{var a=t.onUncaughtError;a(n.value,{componentStack:n.stack})}catch(s){setTimeout(function(){throw s})}}function j_(t,n,a){try{var s=t.onCaughtError;s(a.value,{componentStack:a.stack,errorBoundary:n.tag===1?n.stateNode:null})}catch(l){setTimeout(function(){throw l})}}function qf(t,n,a){return a=Oa(a),a.tag=3,a.payload={element:null},a.callback=function(){ru(t,n)},a}function Z_(t){return t=Oa(t),t.tag=3,t}function K_(t,n,a,s){var l=a.type.getDerivedStateFromError;if(typeof l=="function"){var c=s.value;t.payload=function(){return l(c)},t.callback=function(){j_(n,a,s)}}var m=a.stateNode;m!==null&&typeof m.componentDidCatch=="function"&&(t.callback=function(){j_(n,a,s),typeof l!="function"&&(Xa===null?Xa=new Set([this]):Xa.add(this));var b=s.stack;this.componentDidCatch(s.value,{componentStack:b!==null?b:""})})}function lx(t,n,a,s,l){if(a.flags|=32768,s!==null&&typeof s=="object"&&typeof s.then=="function"){if(n=a.alternate,n!==null&&ys(n,a,l,!0),a=yn.current,a!==null){switch(a.tag){case 31:case 13:case 19:return wn===null?Ru():a.alternate===null&&Qe===0&&(Qe=3),a.flags&=-257,a.flags|=65536,a.lanes=l,s===ql?a.flags|=16384:(n=a.updateQueue,n===null?a.updateQueue=new Set([s]):n.add(s),Dh(t,s,l)),!1;case 22:return a.flags|=65536,s===ql?a.flags|=16384:(n=a.updateQueue,n===null?(n={transitions:null,markerInstances:null,retryQueue:new Set([s])},a.updateQueue=n):(a=n.retryQueue,a===null?n.retryQueue=new Set([s]):a.add(s)),Dh(t,s,l)),!1}throw Error(r(435,a.tag))}return Dh(t,s,l),Ru(),!1}if(de)return n=yn.current,n!==null?((n.flags&65536)===0&&(n.flags|=256),n.flags|=65536,n.lanes=l,s!==hf&&(t=Error(r(422),{cause:s}),To(fi(t,a)))):(s!==hf&&(n=Error(r(423),{cause:s}),To(fi(n,a))),t=t.current.alternate,t.flags|=65536,l&=-l,t.lanes|=l,s=fi(s,a),l=qf(t.stateNode,s,l),Mf(t,l),Qe!==4&&(Qe=2)),!1;var c=Error(r(520),{cause:s});if(c=fi(c,a),Xo===null?Xo=[c]:Xo.push(c),Qe!==4&&(Qe=2),n===null)return!0;s=fi(s,a),a=n;do{switch(a.tag){case 3:return a.flags|=65536,t=l&-l,a.lanes|=t,t=qf(a.stateNode,s,t),Mf(a,t),!1;case 1:if(n=a.type,c=a.stateNode,(a.flags&128)===0&&(typeof n.getDerivedStateFromError=="function"||c!==null&&typeof c.componentDidCatch=="function"&&(Xa===null||!Xa.has(c))))return a.flags|=65536,l&=-l,a.lanes|=l,l=Z_(l),K_(l,t,a,s),Mf(a,l),!1;break;case 22:if(a.memoizedState!==null)return a.flags|=65536,!1}a=a.return}while(a!==null);return!1}var Wf=Error(r(461)),sn=!1;function ln(t,n,a,s){n.child=t===null?t_(n,null,a,s):As(n,t.child,a,s)}function Q_(t,n,a,s,l){a=a.render;var c=n.ref;if("ref"in s){var m={};for(var b in s)b!=="ref"&&(m[b]=s[b])}else m=s;return xs(n),s=wf(t,n,a,m,c,l),b=Df(),t!==null&&!sn?(Uf(t,n,l),fa(t,n,l)):(de&&b&&Fl(n),n.flags|=1,ln(t,n,s,l),n.child)}function J_(t,n,a,s,l){if(t===null){var c=a.type;return typeof c=="function"&&!lf(c)&&c.defaultProps===void 0&&a.compare===null?(n.tag=15,n.type=c,$_(t,n,c,s,l)):(t=Il(a.type,null,s,n,n.mode,l),t.ref=n.ref,t.return=n,n.child=t)}if(c=t.child,!eh(t,l)){var m=c.memoizedProps;if(a=a.compare,a=a!==null?a:xo,a(m,s)&&t.ref===n.ref)return fa(t,n,l)}return n.flags|=1,t=sa(c,s),t.ref=n.ref,t.return=n,n.child=t}function $_(t,n,a,s,l){if(t!==null){var c=t.memoizedProps;if(xo(c,s)&&t.ref===n.ref)if(sn=!1,n.pendingProps=s=c,eh(t,l))(t.flags&131072)!==0&&(sn=!0);else return n.lanes=t.lanes,fa(t,n,l)}return jf(t,n,a,s,l)}function tg(t,n,a,s){var l=s.children,c=t!==null?t.memoizedState:null;if(t===null&&n.stateNode===null&&(n.stateNode={_visibility:1,_pendingMarkers:null,_retryCache:null,_transitions:null}),s.mode==="hidden"){if((n.flags&128)!==0){if(c=c!==null?c.baseLanes|a:a,t!==null){for(s=n.child=t.child,l=0;s!==null;)l=l|s.lanes|s.childLanes,s=s.sibling;s=l&~c}else s=0,n.child=null;return eg(t,n,c,a,s)}if((a&536870912)!==0)n.memoizedState={baseLanes:0,cachePool:null},t!==null&&Yl(n,c!==null?c.cachePool:null),c!==null?i_(n,c):Tf(),a_(n);else return s=n.lanes=536870912,eg(t,n,c!==null?c.baseLanes|a:a,a,s)}else c!==null?(Yl(n,c.cachePool),i_(n,c),Ba(),n.memoizedState=null):(t!==null&&Yl(n,null),Tf(),Ba());return ln(t,n,l,a),n.child}function zo(t,n){return t!==null&&t.tag===22||n.stateNode!==null||(n.stateNode={_visibility:1,_pendingMarkers:null,_retryCache:null,_transitions:null}),n.sibling}function eg(t,n,a,s,l){var c=vf();return c=c===null?null:{parent:nn._currentValue,pool:c},n.memoizedState={baseLanes:a,cachePool:c},t!==null&&Yl(n,null),Tf(),a_(n),t!==null&&ys(t,n,s,!0),n.childLanes=l,null}function ou(t,n){return n=lu({mode:n.mode,children:n.children},t.mode),n.ref=t.ref,t.child=n,n.return=t,n}function ng(t,n,a){return As(n,t.child,null,a),t=ou(n,n.pendingProps),t.flags|=2,ti(n),n.memoizedState=null,t}function ux(t,n,a){var s=n.pendingProps,l=(n.flags&128)!==0;if(n.flags&=-129,t===null){if(de){if(s.mode==="hidden")return t=ou(n,s),n.lanes=536870912,t.memoizedState={baseLanes:0,cachePool:null},zo(null,t);if(Af(n),(t=He)?(t=C0(t,pi),t=t!==null&&t.data==="&"?t:null,t!==null&&(n.memoizedState={dehydrated:t,treeContext:Ca!==null?{id:Bi,overflow:Fi}:null,retryLane:536870912,hydrationErrors:null},a=Fm(t),a.return=n,n.child=a,dn=n,He=null)):t=null,t===null)throw Da(n);return n.lanes=536870912,null}return ou(n,s)}var c=t.memoizedState;if(c!==null){var m=c.dehydrated;if(Af(n),l)if(n.flags&256)n.flags&=-257,n=ng(t,n,a);else if(n.memoizedState!==null)n.child=t.child,n.flags|=128,n=null;else throw Error(r(558));else if(sn||ys(t,n,a,!1),l=(a&t.childLanes)!==0,sn||l){if(za.current===null){if(s=Fe,s!==null&&(m=Et(s,a),m!==0&&m!==c.retryLane))throw c.retryLane=m,_s(t,m),kn(s,t,m),Wf;Ru()}n=ng(t,n,a)}else t=c.treeContext,He=_i(m.nextSibling),dn=n,de=!0,wa=null,pi=!1,t!==null&&Vm(n,t),n=ou(n,s),n.flags|=134221824;return n}return t=sa(t.child,{mode:s.mode,children:s.children}),t.ref=n.ref,n.child=t,t.return=n,t}function _r(t,n){var a=n.ref;if(a===null)t!==null&&t.ref!==null&&(n.flags|=4194816);else{if(typeof a!="function"&&typeof a!="object")throw Error(r(284));(t===null||t.ref!==a)&&(n.flags|=4194816)}}function jf(t,n,a,s,l){return xs(n),a=wf(t,n,a,s,void 0,l),s=Df(),t!==null&&!sn?(Uf(t,n,l),fa(t,n,l)):(de&&s&&Fl(n),n.flags|=1,ln(t,n,a,l),n.child)}function ig(t,n,a,s,l,c){return xs(n),n.updateQueue=null,a=r_(n,s,a,l),s_(t),s=Df(),t!==null&&!sn?(Uf(t,n,c),fa(t,n,c)):(de&&s&&Fl(n),n.flags|=1,ln(t,n,a,c),n.child)}function ag(t,n,a,s,l){if(xs(n),n.stateNode===null){var c=rr,m=a.contextType;typeof m=="object"&&m!==null&&(c=Sn(m)),c=new a(s,c),n.memoizedState=c.state!==null&&c.state!==void 0?c.state:null,c.updater=kf,n.stateNode=c,c._reactInternals=n,c=n.stateNode,c.props=s,c.state=n.memoizedState,c.refs={},yf(n),m=a.contextType,c.context=typeof m=="object"&&m!==null?Sn(m):rr,c.state=n.memoizedState,m=a.getDerivedStateFromProps,typeof m=="function"&&(Yf(n,a,m,s),c.state=n.memoizedState),typeof a.getDerivedStateFromProps=="function"||typeof c.getSnapshotBeforeUpdate=="function"||typeof c.UNSAFE_componentWillMount!="function"&&typeof c.componentWillMount!="function"||(m=c.state,typeof c.componentWillMount=="function"&&c.componentWillMount(),typeof c.UNSAFE_componentWillMount=="function"&&c.UNSAFE_componentWillMount(),m!==c.state&&kf.enqueueReplaceState(c,c.state,null),Uo(n,s,c,l),Do(),c.state=n.memoizedState),typeof c.componentDidMount=="function"&&(n.flags|=4194308),s=!0}else if(t===null){c=n.stateNode;var b=n.memoizedProps,z=Cs(a,b);c.props=z;var W=c.context,et=a.contextType;m=rr,typeof et=="object"&&et!==null&&(m=Sn(et));var ct=a.getDerivedStateFromProps;et=typeof ct=="function"||typeof c.getSnapshotBeforeUpdate=="function",b=n.pendingProps!==b,et||typeof c.UNSAFE_componentWillReceiveProps!="function"&&typeof c.componentWillReceiveProps!="function"||(b||W!==m)&&Y_(n,c,s,m),La=!1;var G=n.memoizedState;c.state=G,Uo(n,s,c,l),Do(),W=n.memoizedState,b||G!==W||La?(typeof ct=="function"&&(Yf(n,a,ct,s),W=n.memoizedState),(z=La||X_(n,a,z,s,G,W,m))?(et||typeof c.UNSAFE_componentWillMount!="function"&&typeof c.componentWillMount!="function"||(typeof c.componentWillMount=="function"&&c.componentWillMount(),typeof c.UNSAFE_componentWillMount=="function"&&c.UNSAFE_componentWillMount()),typeof c.componentDidMount=="function"&&(n.flags|=4194308)):(typeof c.componentDidMount=="function"&&(n.flags|=4194308),n.memoizedProps=s,n.memoizedState=W),c.props=s,c.state=W,c.context=m,s=z):(typeof c.componentDidMount=="function"&&(n.flags|=4194308),s=!1)}else{c=n.stateNode,xf(t,n),m=n.memoizedProps,et=Cs(a,m),c.props=et,ct=n.pendingProps,G=c.context,W=a.contextType,z=rr,typeof W=="object"&&W!==null&&(z=Sn(W)),b=a.getDerivedStateFromProps,(W=typeof b=="function"||typeof c.getSnapshotBeforeUpdate=="function")||typeof c.UNSAFE_componentWillReceiveProps!="function"&&typeof c.componentWillReceiveProps!="function"||(m!==ct||G!==z)&&Y_(n,c,s,z),La=!1,G=n.memoizedState,c.state=G,Uo(n,s,c,l),Do();var $=n.memoizedState;m!==ct||G!==$||La||t!==null&&t.dependencies!==null&&Vl(t.dependencies)?(typeof b=="function"&&(Yf(n,a,b,s),$=n.memoizedState),(et=La||X_(n,a,et,s,G,$,z)||t!==null&&t.dependencies!==null&&Vl(t.dependencies))?(W||typeof c.UNSAFE_componentWillUpdate!="function"&&typeof c.componentWillUpdate!="function"||(typeof c.componentWillUpdate=="function"&&c.componentWillUpdate(s,$,z),typeof c.UNSAFE_componentWillUpdate=="function"&&c.UNSAFE_componentWillUpdate(s,$,z)),typeof c.componentDidUpdate=="function"&&(n.flags|=4),typeof c.getSnapshotBeforeUpdate=="function"&&(n.flags|=1024)):(typeof c.componentDidUpdate!="function"||m===t.memoizedProps&&G===t.memoizedState||(n.flags|=4),typeof c.getSnapshotBeforeUpdate!="function"||m===t.memoizedProps&&G===t.memoizedState||(n.flags|=1024),n.memoizedProps=s,n.memoizedState=$),c.props=s,c.state=$,c.context=z,s=et):(typeof c.componentDidUpdate!="function"||m===t.memoizedProps&&G===t.memoizedState||(n.flags|=4),typeof c.getSnapshotBeforeUpdate!="function"||m===t.memoizedProps&&G===t.memoizedState||(n.flags|=1024),s=!1)}return c=s,_r(t,n),s=(n.flags&128)!==0,c||s?(c=n.stateNode,a=s&&typeof a.getDerivedStateFromError!="function"?null:c.render(),n.flags|=1,t!==null&&s?(n.child=As(n,t.child,null,l),n.child=As(n,null,a,l)):ln(t,n,a,l),n.memoizedState=c.state,t=n.child):t=fa(t,n,l),t}function sg(t,n,a,s){return vs(),n.flags|=256,ln(t,n,a,s),n.child}var Zf={dehydrated:null,treeContext:null,retryLane:0,hydrationErrors:null};function Kf(t){return{baseLanes:t,cachePool:jm()}}function Qf(t,n,a){return t=t!==null?t.childLanes&~a:0,n&&(t|=ii),t}function rg(t,n,a){var s=n.pendingProps,l=!1,c=(n.flags&128)!==0,m;if((m=c)||(m=t!==null&&t.memoizedState===null?!1:(xn.current&2)!==0),m&&(l=!0,n.flags&=-129),m=(n.flags&32)!==0,n.flags&=-33,t===null){if(de){if(l?Ia(n):Ba(),(t=He)?(t=C0(t,pi),t=t!==null&&t.data!=="&"?t:null,t!==null&&(n.memoizedState={dehydrated:t,treeContext:Ca!==null?{id:Bi,overflow:Fi}:null,retryLane:536870912,hydrationErrors:null},a=Fm(t),a.return=n,n.child=a,dn=n,He=null)):t=null,t===null)throw Da(n);return Kh(t)?n.lanes=32:n.lanes=536870912,null}return c=s.children,s=s.fallback,l?(Ba(),l=n.mode,c=lu({mode:"hidden",children:c},l),s=gs(s,l,a,null),c.return=n,s.return=n,c.sibling=s,n.child=c,s=n.child,s.memoizedState=Kf(a),s.childLanes=Qf(t,m,a),n.memoizedState=Zf,zo(null,s)):(Ia(n),Jf(n,c))}var b=t.memoizedState;if(b!==null){var z=b.dehydrated;if(z!==null)return cx(t,n,c,m,s,z,b,a)}return l?(Ba(),l=s.fallback,c=n.mode,b=t.child,z=b.sibling,s=sa(b,{mode:"hidden",children:s.children}),s.subtreeFlags=b.subtreeFlags&1206910976,z!==null?l=sa(z,l):(l=gs(l,c,a,null),l.flags|=2),l.return=n,s.return=n,s.sibling=l,n.child=s,zo(null,s),s=n.child,l=t.child.memoizedState,l===null?l=Kf(a):(c=l.cachePool,c!==null?(b=nn._currentValue,c=c.parent!==b?{parent:b,pool:b}:c):c=jm(),l={baseLanes:l.baseLanes|a,cachePool:c}),s.memoizedState=l,s.childLanes=Qf(t,m,a),n.memoizedState=Zf,zo(t.child,s)):(Ia(n),a=t.child,t=a.sibling,a=sa(a,{mode:"visible",children:s.children}),a.return=n,a.sibling=null,t!==null&&(m=n.deletions,m===null?(n.deletions=[t],n.flags|=16):m.push(t)),n.child=a,n.memoizedState=null,a)}function Jf(t,n){return n=lu({mode:"visible",children:n},t.mode),n.return=t,t.child=n}function lu(t,n){return t=Gn(22,t,null,n),t.lanes=0,t}function uu(t,n,a){return As(n,t.child,null,a),t=Jf(n,n.pendingProps.children),t.flags|=2,n.memoizedState=null,t}function cx(t,n,a,s,l,c,m,b){if(a)return n.flags&256?(Ia(n),n.flags&=-257,uu(t,n,b)):n.memoizedState!==null?(Ba(),n.child=t.child,n.flags|=128,null):(Ba(),c=l.fallback,m=n.mode,l=lu({mode:"visible",children:l.children},m),c=gs(c,m,b,null),c.flags|=2,l.return=n,c.return=n,l.sibling=c,n.child=l,As(n,t.child,null,b),l=n.child,l.memoizedState=Kf(b),l.childLanes=Qf(t,s,b),n.memoizedState=Zf,zo(null,l));if(Ia(n),Kh(c)){if(s=c.nextSibling&&c.nextSibling.dataset,s)var z=s.dgst;return s=z,s!==""&&(l=Error(r(419)),l.stack="",l.digest=s,To({value:l,source:null,stack:null})),uu(t,n,b)}if(sn||ys(t,n,b,!1),s=(b&t.childLanes)!==0,sn||s){if(za.current!==null)return uu(t,n,b);if(s=Fe,s!==null&&(l=Et(s,b),l!==0&&l!==m.retryLane))throw m.retryLane=l,_s(t,l),kn(s,t,l),Wf;return Zh(c)||Ru(),uu(t,n,b)}return Zh(c)?(n.flags|=192,n.child=t.child,null):(t=m.treeContext,He=_i(c.nextSibling),dn=n,de=!0,wa=null,pi=!1,t!==null&&Vm(n,t),n=Jf(n,l.children),n.flags|=134221824,n)}function og(t,n,a){t.lanes|=n;var s=t.alternate;s!==null&&(s.lanes|=n),Gl(t.return,n,a)}function lg(t){for(var n=null;t!==null;){var a=t.alternate;a!==null&&Kl(a)===null&&(n=t),t=t.sibling}return n}function cu(t,n,a,s,l,c){var m=t.memoizedState;m===null?t.memoizedState={isBackwards:n,rendering:null,renderingStartTime:0,last:s,tail:a,tailMode:l,treeForkCount:c}:(m.isBackwards=n,m.rendering=null,m.renderingStartTime=0,m.last=s,m.tail=a,m.tailMode=l,m.treeForkCount=c)}function $f(t){var n=t.child;for(t.child=null;n!==null;){var a=n.sibling;n.sibling=t.child,t.child=n,n=a}}function th(t,n,a){var s=n.pendingProps,l=s.revealOrder,c=s.tail;s=s.children;var m=xn.current;if(n.flags&128)return No(n,m),null;var b=(m&2)!==0;if(b?(m=m&1|2,n.flags|=128):m&=1,No(n,m),l==="backwards"&&t!==null?($f(t),ln(t,n,s,a),$f(t)):ln(t,n,s,a),s=de?Eo:0,!b&&t!==null&&(t.flags&128)!==0)t:for(t=n.child;t!==null;){if(t.tag===13)t.memoizedState!==null&&og(t,a,n);else if(t.tag===19)og(t,a,n);else if(t.child!==null){t.child.return=t,t=t.child;continue}if(t===n)break t;for(;t.sibling===null;){if(t.return===null||t.return===n)break t;t=t.return}t.sibling.return=t.return,t=t.sibling}switch(l){case"backwards":a=lg(n.child),a===null?(l=n.child,n.child=null):(l=a.sibling,a.sibling=null,$f(n)),cu(n,!0,l,null,c,s);break;case"unstable_legacy-backwards":for(a=null,l=n.child,n.child=null;l!==null;){if(t=l.alternate,t!==null&&Kl(t)===null){n.child=l;break}t=l.sibling,l.sibling=a,a=l,l=t}cu(n,!0,a,null,c,s);break;case"together":cu(n,!1,null,null,void 0,s);break;case"independent":n.memoizedState=null;break;default:a=lg(n.child),a===null?(l=n.child,n.child=null):(l=a.sibling,a.sibling=null),cu(n,!1,l,a,c,s)}return n.child}function ug(t,n,a){var s=n.pendingProps;return Ua(n,n.type,s.value),ln(t,n,s.children,a),n.child}function fa(t,n,a){if(t!==null&&(n.dependencies=t.dependencies),Va|=n.lanes,(a&n.childLanes)===0)if(t!==null){if(ys(t,n,a,!1),(a&n.childLanes)===0)return null}else return null;if(t!==null&&n.child!==t.child)throw Error(r(153));if(n.child!==null){for(t=n.child,a=sa(t,t.pendingProps),n.child=a,a.return=n;t.sibling!==null;)t=t.sibling,a=a.sibling=sa(t,t.pendingProps),a.return=n;a.sibling=null}return n.child}function eh(t,n){return(t.lanes&n)!==0?!0:(t=t.dependencies,!!(t!==null&&Vl(t)))}function fx(t,n,a){switch(n.tag){case 3:pt(n,n.stateNode.containerInfo),Ua(n,nn,t.memoizedState.cache),vs();break;case 27:case 5:mt(n);break;case 4:pt(n,n.stateNode.containerInfo);break;case 10:Ua(n,n.type,n.memoizedProps.value);break;case 31:if(n.memoizedState!==null)return n.flags|=128,Af(n),null;break;case 13:var s=n.memoizedState;if(s!==null){if(s.dehydrated!==null)return Ia(n),n.flags|=128,null;s=ys(t,n,a,!1);var l=n.child.childLanes;return s||(a&l)!==0?rg(t,n,a):(Ia(n),t=fa(t,n,a),t!==null?t.sibling:null)}Ia(n);break;case 19:if(n.flags&128)return th(t,n,a);if(l=(t.flags&128)!==0,s=(a&n.childLanes)!==0,s||(ys(t,n,a,!1),s=(a&n.childLanes)!==0),l){if(s)return th(t,n,a);n.flags|=128}if(l=n.memoizedState,l!==null&&(l.rendering=null,l.tail=null,l.lastEffect=null),No(n,xn.current),s)break;return null;case 22:return n.lanes=0,tg(t,n,a,n.pendingProps);case 24:Ua(n,nn,t.memoizedState.cache)}return fa(t,n,a)}function cg(t,n,a){if(t!==null)if(t.memoizedProps!==n.pendingProps)sn=!0;else{if(!eh(t,a)&&(n.flags&128)===0)return sn=!1,fx(t,n,a);sn=(t.flags&131072)!==0}else sn=!1,de&&(n.flags&1048576)!==0&&Gm(n,Eo,n.index);switch(n.lanes=0,n.tag){case 16:t:{var s=n.pendingProps;if(t=Ts(n.elementType),n.type=t,typeof t=="function")lf(t)?(s=Cs(t,s),n.tag=1,n=ag(null,n,t,s,a)):(n.tag=0,n=jf(null,n,t,s,a));else{if(t!=null){var l=t.$$typeof;if(l===H){n.tag=11,n=Q_(null,n,t,s,a);break t}else if(l===yt){n.tag=14,n=J_(null,n,t,s,a);break t}else if(l===ft){n.tag=10,n.type=t,n=ug(null,n,a);break t}}throw n=Rt(t)||t,Error(r(306,n,""))}}return n;case 0:return jf(t,n,n.type,n.pendingProps,a);case 1:return s=n.type,l=Cs(s,n.pendingProps),ag(t,n,s,l,a);case 3:t:{if(pt(n,n.stateNode.containerInfo),t===null)throw Error(r(387));s=n.pendingProps;var c=n.memoizedState;l=c.element,xf(t,n),Uo(n,s,null,a);var m=n.memoizedState;if(s=m.cache,Ua(n,nn,s),s!==c.cache&&mf(n,[nn],a,!0),Do(),s=m.element,c.isDehydrated)if(c={element:s,isDehydrated:!1,cache:m.cache},n.updateQueue.baseState=c,n.memoizedState=c,n.flags&256){n=sg(t,n,s,a);break t}else if(s!==l){l=fi(Error(r(424)),n),To(l),n=sg(t,n,s,a);break t}else for(t=n.stateNode.containerInfo,t.nodeType===9?t=t.body:t=t.nodeName==="HTML"?t.ownerDocument.body:t,He=_i(t.firstChild),dn=n,de=!0,wa=null,pi=!0,a=t_(n,null,s,a),n.child=a;a;)a.flags=a.flags&-3|134221824,a=a.sibling;else{if(vs(),s===l){n=fa(t,n,a);break t}ln(t,n,s,a)}n=n.child}return n;case 26:return _r(t,n),t===null?(a=P0(n.type,null,n.pendingProps,null))?n.memoizedState=a:de||(n.stateNode=p0(n.type,n.pendingProps,A.current,n)):n.memoizedState=P0(n.type,t.memoizedProps,n.pendingProps,t.memoizedState),null;case 27:return mt(n),t===null&&de&&(s=n.stateNode=U0(n.type,n.pendingProps,A.current),dn=n,pi=!0,l=He,qa(n.type)?(Qh=l,He=_i(s.firstChild)):He=l),ln(t,n,n.pendingProps.children,a),_r(t,n),t===null&&(n.flags|=4194304),n.child;case 5:return t===null&&de&&((l=s=He)&&(s=sM(s,n.type,n.pendingProps,pi),s!==null?(n.stateNode=s,dn=n,He=_i(s.firstChild),pi=!1,l=!0):l=!1),l||Da(n)),mt(n),l=n.type,c=n.pendingProps,m=t!==null?t.memoizedProps:null,s=c.children,Vh(l,c)?s=null:m!==null&&Vh(l,m)&&(n.flags|=32),n.memoizedState!==null&&(l=wf(t,n,tx,null,null,a),Or._currentValue=l),_r(t,n),ln(t,n,s,a),n.child;case 6:return t===null&&de&&((t=a=He)&&(a=rM(a,n.pendingProps,pi),a!==null?(n.stateNode=a,dn=n,He=null,t=!0):t=!1),t||Da(n)),null;case 13:return rg(t,n,a);case 4:return pt(n,n.stateNode.containerInfo),s=n.pendingProps,t===null?n.child=As(n,null,s,a):ln(t,n,s,a),n.child;case 11:return Q_(t,n,n.type,n.pendingProps,a);case 7:return s=n.pendingProps,_r(t,n),ln(t,n,s,a),n.child;case 8:return ln(t,n,n.pendingProps.children,a),n.child;case 12:return ln(t,n,n.pendingProps.children,a),n.child;case 10:return ug(t,n,a);case 9:return l=n.type._context,s=n.pendingProps.children,xs(n),l=Sn(l),s=s(l),n.flags|=1,ln(t,n,s,a),n.child;case 14:return J_(t,n,n.type,n.pendingProps,a);case 15:return $_(t,n,n.type,n.pendingProps,a);case 19:return th(t,n,a);case 31:return ux(t,n,a);case 22:return tg(t,n,a,n.pendingProps);case 24:return xs(n),s=Sn(nn),t===null?(l=vf(),l===null&&(l=Fe,c=_f(),l.pooledCache=c,c.refCount++,c!==null&&(l.pooledCacheLanes|=a),l=c),n.memoizedState={parent:s,cache:l},yf(n),Ua(n,nn,l)):((t.lanes&a)!==0&&(xf(t,n),Uo(n,null,null,a),Do()),l=t.memoizedState,c=n.memoizedState,l.parent!==s?(l={parent:s,cache:s},n.memoizedState=l,n.lanes===0&&(n.memoizedState=n.updateQueue.baseState=l),Ua(n,nn,s)):(s=c.cache,Ua(n,nn,s),s!==l.cache&&mf(n,[nn],a,!0))),ln(t,n,n.pendingProps.children,a),n.child;case 30:return n.stateNode===null&&(n.stateNode={autoName:null,paired:null,clones:null,ref:null}),s=n.pendingProps,s.name!=null&&s.name!=="auto"?n.flags|=t===null?18882560:18874368:de&&Fl(n),t!==null&&t.memoizedProps.name!==s.name?n.flags|=4194816:_r(t,n),ln(t,n,s.children,a),n.child;case 29:throw n.pendingProps}throw Error(r(156,n.tag))}function ha(t){t.flags|=4}function nh(t,n,a,s,l){var c;if((c=(t.mode&32)!==0)&&(c=a===null?F0(n,s):F0(n,s)&&(s.src!==a.src||s.srcSet!==a.srcSet)),c){if(t.flags|=16777216,(l&335544128)===l)if(t.stateNode.complete)t.flags|=8192;else if(kg())t.flags|=8192;else throw bs=ql,Sf}else t.flags&=-16777217}function fg(t,n){if(n.type!=="stylesheet"||(n.state.loading&4)!==0)t.flags&=-16777217;else if(t.flags|=16777216,!H0(n))if(kg())t.flags|=8192;else throw bs=ql,Sf}function fu(t,n){n!==null&&(t.flags|=4),t.flags&16384&&(n=t.tag!==22?El():536870912,t.lanes|=n,xr|=n)}function Io(t,n){if(!de)switch(t.tailMode){case"visible":break;case"collapsed":for(var a=t.tail,s=null;a!==null;)a.alternate!==null&&(s=a),a=a.sibling;s===null?n||t.tail===null?t.tail=null:t.tail.sibling=null:s.sibling=null;break;default:for(n=t.tail,a=null;n!==null;)n.alternate!==null&&(a=n),n=n.sibling;a===null?t.tail=null:a.sibling=null}}function Ge(t){var n=t.alternate!==null&&t.alternate.child===t.child,a=0,s=0;if(n)for(var l=t.child;l!==null;)a|=l.lanes|l.childLanes,s|=l.subtreeFlags&1206910976,s|=l.flags&1206910976,l.return=t,l=l.sibling;else for(l=t.child;l!==null;)a|=l.lanes|l.childLanes,s|=l.subtreeFlags,s|=l.flags,l.return=t,l=l.sibling;return t.subtreeFlags|=s,t.childLanes=a,n}function hx(t,n,a){var s=n.pendingProps;switch(ff(n),n.tag){case 16:case 15:case 0:case 11:case 7:case 8:case 12:case 9:case 14:return Ge(n),null;case 1:return Ge(n),null;case 3:return a=n.stateNode,s=null,t!==null&&(s=t.memoizedState.cache),n.memoizedState.cache!==s&&(n.flags|=2048),la(nn),vt(),a.pendingContext&&(a.context=a.pendingContext,a.pendingContext=null),(t===null||t.child===null)&&(ur(n)?ha(n):t===null||t.memoizedState.isDehydrated&&(n.flags&256)===0||(n.flags|=1024,df())),Ge(n),null;case 26:var l=n.type,c=n.memoizedState;return t===null?(ha(n),c!==null?(Ge(n),fg(n,c)):(Ge(n),nh(n,l,null,s,a))):c?c!==t.memoizedState?(ha(n),Ge(n),fg(n,c)):(Ge(n),n.flags&=-16777217):(t=t.memoizedProps,t!==s&&ha(n),Ge(n),nh(n,l,t,s,a)),null;case 27:if(kt(n),a=A.current,l=n.type,t!==null&&n.stateNode!=null)t.memoizedProps!==s&&ha(n);else{if(!s){if(n.stateNode===null)throw Error(r(166));return Ge(n),n.subtreeFlags&=-33554433,null}t=Zt.current,ur(n)?Xm(n):(t=U0(l,s,a),n.stateNode=t,ha(n))}return Ge(n),n.subtreeFlags&=-33554433,null;case 5:if(kt(n),l=n.type,t!==null&&n.stateNode!=null)t.memoizedProps!==s&&ha(n);else{if(!s){if(n.stateNode===null)throw Error(r(166));return Ge(n),n.subtreeFlags&=-33554433,null}if(c=Zt.current,ur(n))Xm(n);else{var m=jo(A.current);switch(c){case 1:c=m.createElementNS("http://www.w3.org/2000/svg",l);break;case 2:c=m.createElementNS("http://www.w3.org/1998/Math/MathML",l);break;default:switch(l){case"svg":c=m.createElementNS("http://www.w3.org/2000/svg",l);break;case"math":c=m.createElementNS("http://www.w3.org/1998/Math/MathML",l);break;case"script":c=m.createElement("div"),c.innerHTML="<script><\/script>",c=c.removeChild(c.firstChild);break;case"select":c=typeof s.is=="string"?m.createElement("select",{is:s.is}):m.createElement("select"),s.multiple?c.multiple=!0:s.size&&(c.size=s.size);break;default:c=typeof s.is=="string"?m.createElement(l,{is:s.is}):m.createElement(l)}}c[Ut]=n,c[ie]=s;t:for(m=n.child;m!==null;){if(m.tag===5||m.tag===6)c.appendChild(m.stateNode);else if(m.tag!==4&&m.tag!==27&&m.child!==null){m.child.return=m,m=m.child;continue}if(m===n)break t;for(;m.sibling===null;){if(m.return===null||m.return===n)break t;m=m.return}m.sibling.return=m.return,m=m.sibling}n.stateNode=c;t:switch(En(c,l,s),l){case"button":case"input":case"select":case"textarea":s=!!s.autoFocus;break t;case"img":s=!0;break t;default:s=!1}s&&ha(n)}}return Ge(n),n.subtreeFlags&=-33554433,nh(n,n.type,t===null?null:t.memoizedProps,n.pendingProps,a),null;case 6:if(t&&n.stateNode!=null)t.memoizedProps!==s&&ha(n);else{if(typeof s!="string"&&n.stateNode===null)throw Error(r(166));if(t=A.current,ur(n)){if(t=n.stateNode,a=n.memoizedProps,s=null,l=dn,l!==null)switch(l.tag){case 27:case 5:s=l.memoizedProps}t[Ut]=n,t=!!(t.nodeValue===a||s!==null&&s.suppressHydrationWarning===!0||c0(t.nodeValue,a)),t||Da(n,!0)}else t=jo(t).createTextNode(s),t[Ut]=n,n.stateNode=t}return Ge(n),null;case 31:if(a=n.memoizedState,t===null||t.memoizedState!==null){if(s=ur(n),a!==null){if(t===null){if(!s)throw Error(r(318));if(t=n.memoizedState,t=t!==null?t.dehydrated:null,!t)throw Error(r(557));t[Ut]=n}else vs(),(n.flags&128)===0&&(n.memoizedState=null),n.flags|=4;Ge(n),t=!1}else a=df(),t!==null&&t.memoizedState!==null&&(t.memoizedState.hydrationErrors=a),t=!0;if(!t)return n.flags&256?(ti(n),n):(ti(n),null);if((n.flags&128)!==0)throw Error(r(558))}return Ge(n),null;case 13:if(s=n.memoizedState,t===null||t.memoizedState!==null&&t.memoizedState.dehydrated!==null){if(l=ur(n),s!==null&&s.dehydrated!==null){if(t===null){if(!l)throw Error(r(318));if(l=n.memoizedState,l=l!==null?l.dehydrated:null,!l)throw Error(r(317));l[Ut]=n}else vs(),(n.flags&128)===0&&(n.memoizedState=null),n.flags|=4;Ge(n),l=!1}else l=df(),t!==null&&t.memoizedState!==null&&(t.memoizedState.hydrationErrors=l),l=!0;if(!l)return n.flags&256?(ti(n),n):(ti(n),null)}return ti(n),(n.flags&128)!==0?(n.lanes=a,n):(a=s!==null,t=t!==null&&t.memoizedState!==null,a&&(s=n.child,l=null,s.alternate!==null&&s.alternate.memoizedState!==null&&s.alternate.memoizedState.cachePool!==null&&(l=s.alternate.memoizedState.cachePool.pool),c=null,s.memoizedState!==null&&s.memoizedState.cachePool!==null&&(c=s.memoizedState.cachePool.pool),c!==l&&(s.flags|=2048)),a!==t&&a&&(n.child.flags|=8192),fu(n,n.updateQueue),Ge(n),null);case 4:return vt(),t===null&&Ih(n.stateNode.containerInfo),n.flags|=67108864,Ge(n),null;case 10:return la(n.type),Ge(n),null;case 19:if(Rf(n),s=n.memoizedState,s===null)return Ge(n),null;if(l=(n.flags&128)!==0,c=s.rendering,c===null)if(l)Io(s,!1);else{if(Qe!==0||t!==null&&(t.flags&128)!==0)for(t=n.child;t!==null;){if(c=Kl(t),c!==null){for(n.flags|=128,Io(s,!1),t=c.updateQueue,n.updateQueue=t,fu(n,t),n.subtreeFlags=0,t=a,a=n.child;a!==null;)Bm(a,t),a=a.sibling;return No(n,xn.current&1|2),de&&ra(n,s.treeForkCount),n.child}t=t.sibling}s.tail!==null&&Tt()>Eu&&(n.flags|=128,l=!0,Io(s,!1),n.lanes=4194304)}else{if(!l)if(t=Kl(c),t!==null){if(n.flags|=128,l=!0,t=t.updateQueue,n.updateQueue=t,fu(n,t),Io(s,!0),s.tail===null&&s.tailMode!=="collapsed"&&s.tailMode!=="visible"&&!c.alternate&&!de)return Ge(n),null}else 2*Tt()-s.renderingStartTime>Eu&&a!==536870912&&(n.flags|=128,l=!0,Io(s,!1),n.lanes=4194304);s.isBackwards?(c.sibling=n.child,n.child=c):(t=s.last,t!==null?t.sibling=c:n.child=c,s.last=c)}if(s.tail!==null){t=s.tail;t:{for(a=t;a!==null;){if(a.alternate!==null){a=!1;break t}a=a.sibling}a=!0}return s.rendering=t,s.tail=t.sibling,s.renderingStartTime=Tt(),t.sibling=null,c=xn.current,c=l?c&1|2:c&1,s.tailMode==="visible"||s.tailMode==="collapsed"||!a||de?No(n,c):(a=c,Kt(yn,n),Kt(xn,a),wn===null&&(wn=n)),de&&ra(n,s.treeForkCount),t}return Ge(n),null;case 22:case 23:return ti(n),bf(),s=n.memoizedState!==null,t!==null?t.memoizedState!==null!==s&&(n.flags|=8192):s&&(n.flags|=8192),s?(a&536870912)!==0&&(n.flags&128)===0&&(Ge(n),n.subtreeFlags&6&&(n.flags|=8192)):Ge(n),a=n.updateQueue,a!==null&&fu(n,a.retryQueue),a=null,t!==null&&t.memoizedState!==null&&t.memoizedState.cachePool!==null&&(a=t.memoizedState.cachePool.pool),s=null,n.memoizedState!==null&&n.memoizedState.cachePool!==null&&(s=n.memoizedState.cachePool.pool),s!==a&&(n.flags|=2048),t!==null&&Xt(Es),null;case 24:return a=null,t!==null&&(a=t.memoizedState.cache),n.memoizedState.cache!==a&&(n.flags|=2048),la(nn),Ge(n),null;case 25:return null;case 30:return n.flags|=33554432,Ge(n),null}throw Error(r(156,n.tag))}function dx(t,n){switch(ff(n),n.tag){case 1:return t=n.flags,t&65536?(n.flags=t&-65537|128,n):null;case 3:return la(nn),vt(),t=n.flags,(t&65536)!==0&&(t&128)===0?(n.flags=t&-65537|128,n):null;case 26:case 27:case 5:return kt(n),null;case 31:if(n.memoizedState!==null){if(ti(n),n.alternate===null)throw Error(r(340));vs()}return t=n.flags,t&65536?(n.flags=t&-65537|128,n):null;case 13:if(ti(n),t=n.memoizedState,t!==null&&t.dehydrated!==null){if(n.alternate===null)throw Error(r(340));vs()}return t=n.flags,t&65536?(n.flags=t&-65537|128,n):null;case 19:return Rf(n),t=n.flags,t&65536?(n.flags=t&-65537|128,t=n.memoizedState,t!==null&&(t.rendering=null,t.tail=null),n.flags|=4,n):null;case 4:return vt(),null;case 10:return la(n.type),null;case 22:case 23:return ti(n),bf(),t!==null&&Xt(Es),t=n.flags,t&65536?(n.flags=t&-65537|128,n):null;case 24:return la(nn),null;case 25:return null;default:return null}}function hg(t,n){switch(ff(n),n.tag){case 3:la(nn),vt();break;case 26:case 27:case 5:kt(n);break;case 4:vt();break;case 31:n.memoizedState!==null&&ti(n);break;case 13:ti(n);break;case 19:Rf(n);break;case 10:la(n.type);break;case 22:case 23:ti(n),bf(),t!==null&&Xt(Es);break;case 24:la(nn)}}function Bo(t,n){try{var a=n.updateQueue,s=a!==null?a.lastEffect:null;if(s!==null){var l=s.next;a=l;do{if((a.tag&t)===t){s=void 0;var c=a.create,m=a.inst;s=c(),m.destroy=s}a=a.next}while(a!==l)}}catch(b){Ne(n,n.return,b)}}function Fa(t,n,a){try{var s=n.updateQueue,l=s!==null?s.lastEffect:null;if(l!==null){var c=l.next;s=c;do{if((s.tag&t)===t){var m=s.inst,b=m.destroy;if(b!==void 0){m.destroy=void 0,l=n;var z=a,W=b;try{W()}catch(et){Ne(l,z,et)}}}s=s.next}while(s!==c)}}catch(et){Ne(n,n.return,et)}}function dg(t){var n=t.updateQueue;if(n!==null){var a=t.stateNode;try{n_(n,a)}catch(s){Ne(t,t.return,s)}}}function pg(t,n,a){a.props=Cs(t.type,t.memoizedProps),a.state=t.memoizedState;try{a.componentWillUnmount()}catch(s){Ne(t,n,s)}}function Hi(t,n){try{var a=t.ref;if(a!==null){switch(t.tag){case 26:case 27:case 5:var s=t.stateNode;break;case 30:var l=t.stateNode,c=ia(t.memoizedProps,l);(l.ref===null||l.ref.name!==c)&&(l.ref=x0(c)),s=l.ref;break;case 7:if(t.stateNode===null){var m=new si(t);_(t.child,!1,iM,m,void 0,void 0),t.stateNode=m}s=t.stateNode;break;default:s=t.stateNode}typeof a=="function"?t.refCleanup=a(s):a.current=s}}catch(b){Ne(t,n,b)}}function Mn(t,n){var a=t.ref,s=t.refCleanup;if(a!==null)if(typeof s=="function")try{s()}catch(l){Ne(t,n,l)}finally{t.refCleanup=null,t=t.alternate,t!=null&&(t.refCleanup=null)}else if(typeof a=="function")try{a(null)}catch(l){Ne(t,n,l)}else a.current=null}function hu(t,n){if((t.tag===5||t.tag===27||t.tag===6)&&t.alternate===null&&n!==null)for(var a=0;a<n.length;a++)R0(t.stateNode,n[a])}function mg(t){for(var n=t.return;n!==null&&(ah(n)&&R0(t.stateNode,n.stateNode),!ih(n));)n=n.return}function Fo(t){for(var n=t.return;n!==null&&(ah(n)&&aM(t.stateNode,n.stateNode),!ih(n));)n=n.return}function ih(t){return t.tag===5||t.tag===3||t.tag===27}function ah(t){return t&&t.tag===7&&t.stateNode!==null}function sh(t){var n=t.type,a=t.memoizedProps,s=t.stateNode;try{t:switch(n){case"button":case"input":case"select":case"textarea":a.autoFocus&&s.focus();break t;case"img":a.src?s.src=a.src:a.srcSet&&(s.srcset=a.srcSet)}}catch(l){Ne(t,t.return,l)}}function rh(t,n,a){try{var s=t.stateNode;Fx(s,t.type,a,n),s[ie]=n}catch(l){Ne(t,t.return,l)}}function _g(t){return t.tag===5||t.tag===3||t.tag===26||t.tag===27&&qa(t.type)||t.tag===4}function oh(t){t:for(;;){for(;t.sibling===null;){if(t.return===null||_g(t.return))return null;t=t.return}for(t.sibling.return=t.return,t=t.sibling;t.tag!==5&&t.tag!==6&&t.tag!==18;){if(t.tag===27&&qa(t.type)||t.flags&2||t.child===null||t.tag===4)continue t;t.child.return=t,t=t.child}if(!(t.flags&2))return t.stateNode}}function lh(t,n,a,s){var l=t.tag;if(l===5||l===6)l=t.stateNode,n?(a.nodeType===9?a.body:a.nodeName==="HTML"?a.ownerDocument.body:a).insertBefore(l,n):(n=a.nodeType===9?a.body:a.nodeName==="HTML"?a.ownerDocument.body:a,n.appendChild(l),a=a._reactRootContainer,a!=null||n.onclick!==null||(n.onclick=Ii)),hu(t,s),Re=!0;else if(l!==4&&(l===27&&(hu(t,s),s=null,qa(t.type)&&(a=t.stateNode,n=null)),t=t.child,t!==null))for(lh(t,n,a,s),t=t.sibling;t!==null;)lh(t,n,a,s),t=t.sibling}function du(t,n,a,s){var l=t.tag;if(l===5||l===6)l=t.stateNode,n?a.insertBefore(l,n):a.appendChild(l),hu(t,s),Re=!0;else if(l!==4&&(l===27&&(hu(t,s),s=null,qa(t.type)&&(a=t.stateNode)),t=t.child,t!==null))for(du(t,n,a,s),t=t.sibling;t!==null;)du(t,n,a,s),t=t.sibling}function gg(t){var n=t.stateNode,a=t.memoizedProps;try{for(var s=t.type,l=n.attributes;l.length;)n.removeAttributeNode(l[0]);En(n,s,a),n[Ut]=t,n[ie]=a}catch(c){Ne(t,t.return,c)}}var pu=!1,ei=null;function vg(t){(t.tag===30||(t.subtreeFlags&33554432)!==0)&&(pu=!0)}var Gi=null;function Sg(){var t=Gi;return Gi=null,t}var Vn=0;function gr(t,n,a,s,l){return Vn=0,yg(t.child,n,a,s,l)}function yg(t,n,a,s,l){for(var c=!1;t!==null;){if(t.tag===5){var m=t.stateNode;if(s!==null){var b=kh(m);s.push(b),b.view&&(c=!0)}else c||kh(m).view&&(c=!0);pu=!0,S0(m,Vn===0?n:n+"_"+Vn,a),Vn++}else(t.tag!==22||t.memoizedState===null)&&(t.tag===30&&l||yg(t.child,n,a,s,l)&&(c=!0));t=t.sibling}return c}function Vi(t,n){for(;t!==null;)t.tag===5?y0(t.stateNode,t.memoizedProps):(t.tag!==22||t.memoizedState===null)&&(t.tag===30&&n||Vi(t.child,n)),t=t.sibling}function mu(t){if((t.subtreeFlags&18874368)!==0)for(t=t.child;t!==null;){if((t.tag!==22||t.memoizedState===null)&&(mu(t),t.tag===30&&(t.flags&18874368)!==0&&t.stateNode.paired)){var n=t.memoizedProps;if(n.name==null||n.name==="auto")throw Error(r(544));var a=n.name;n=aa(n.default,n.share),n!=="none"&&(gr(t,a,n,null,!1)||Vi(t.child,!1))}t=t.sibling}}function uh(t,n){if(t.tag===30){var a=t.stateNode,s=t.memoizedProps,l=ia(s,a),c=aa(s.default,a.paired?s.share:s.enter);c!=="none"?gr(t,l,c,null,!1)?(mu(t),a.paired||n||br(t,s.onEnter)):Vi(t.child,!1):mu(t)}else if((t.subtreeFlags&33554432)!==0)for(t=t.child;t!==null;)uh(t,n),t=t.sibling;else mu(t)}function ch(t){if(ei!==null&&ei.size!==0){var n=ei;if((t.subtreeFlags&18874368)!==0)for(t=t.child;t!==null;){if(t.tag!==22||t.memoizedState===null){if(t.tag===30&&(t.flags&18874368)!==0){var a=t.memoizedProps,s=a.name;if(s!=null&&s!=="auto"){var l=n.get(s);if(l!==void 0){var c=aa(a.default,a.share);if(c!=="none"&&(gr(t,s,c,null,!1)?(c=t.stateNode,l.paired=c,c.paired=l,br(t,a.onShare)):Vi(t.child,!1)),n.delete(s),n.size===0)break}}}ch(t)}t=t.sibling}}}function fh(t){if(t.tag===30){var n=t.memoizedProps,a=ia(n,t.stateNode),s=ei!==null?ei.get(a):void 0,l=aa(n.default,s!==void 0?n.share:n.exit);l!=="none"&&(gr(t,a,l,null,!1)?s!==void 0?(l=t.stateNode,s.paired=l,l.paired=s,ei.delete(a),br(t,n.onShare)):br(t,n.onExit):Vi(t.child,!1)),ei!==null&&ch(t)}else if((t.subtreeFlags&33554432)!==0)for(t=t.child;t!==null;)fh(t),t=t.sibling;else ei!==null&&ch(t)}function xg(t){for(t=t.child;t!==null;){if(t.tag===30){var n=t.memoizedProps,a=ia(n,t.stateNode);n=aa(n.default,n.update),t.flags&=-5,n!=="none"&&gr(t,a,n,t.memoizedState=[],!1)}else(t.subtreeFlags&33554432)!==0&&xg(t);t=t.sibling}}function hh(t){if((t.subtreeFlags&18874368)!==0)for(t=t.child;t!==null;){if(t.tag!==22||t.memoizedState===null){if(t.tag===30&&(t.flags&18874368)!==0){var n=t.stateNode;n.paired!==null&&(n.paired=null,Vi(t.child,!1))}hh(t)}t=t.sibling}}function _u(t){if(t.tag===30)t.stateNode.paired=null,Vi(t.child,!1),hh(t);else if((t.subtreeFlags&33554432)!==0)for(t=t.child;t!==null;)_u(t),t=t.sibling;else hh(t)}function Mg(t){for(t=t.child;t!==null;)t.tag===30?Vi(t.child,!1):(t.subtreeFlags&33554432)!==0&&Mg(t),t=t.sibling}function dh(t,n,a,s,l,c,m){for(var b=!1;n!==null;){if(n.tag===5){var z=n.stateNode;if(c!==null&&Vn<c.length){var W=c[Vn],et=kh(z);(W.view||et.view)&&(b=!0);var ct;if(ct=(t.flags&4)===0)if(et.clip)ct=!0;else{ct=W.rect;var G=et.rect;ct=ct.y!==G.y||ct.x!==G.x||ct.height!==G.height||ct.width!==G.width}ct&&(t.flags|=4),et.abs?et=!W.abs:(W=W.rect,et=et.rect,et=W.height!==et.height||W.width!==et.width),et&&(t.flags|=32)}else t.flags|=32;(t.flags&4)!==0&&S0(z,Vn===0?a:a+"_"+Vn,l),b&&(t.flags&4)!==0||(Gi===null&&(Gi=[]),Gi.push(z,Vn===0?s:s+"_"+Vn,n.memoizedProps)),Vn++}else(n.tag!==22||n.memoizedState===null)&&(n.tag===30&&m?t.flags|=n.flags&32:dh(t,n.child,a,s,l,c,m)&&(b=!0));n=n.sibling}return b}function Eg(t,n){for(t=t.child;t!==null;){if(t.tag===30){var a=t.memoizedProps,s=t.stateNode,l=ia(a,s),c=aa(a.default,a.update),m;m=t.memoizedState,t.memoizedState=null,s=t;var b=t.child;Vn=0,l=dh(s,b,l,l,c,m,!1),(t.flags&4)!==0&&l&&br(t,a.onUpdate)}else(t.subtreeFlags&33554432)!==0&&Eg(t);t=t.sibling}}var pn=!1,we=!1,Xi=!1,ph=!1,Tg=typeof WeakSet=="function"?WeakSet:Set,mn=null,Yi=!1,Ho=!1,gu=!1,mh=!1;function px(t,n,a){if(t=t.containerInfo,Hh=Pr,t=Cm(t),tf(t)){if("selectionStart"in t)var s={start:t.selectionStart,end:t.selectionEnd};else t:{s=(s=t.ownerDocument)&&s.defaultView||window;var l=s.getSelection&&s.getSelection();if(l&&l.rangeCount!==0){s=l.anchorNode;var c=l.anchorOffset,m=l.focusNode;l=l.focusOffset;try{s.nodeType,m.nodeType}catch{s=null;break t}var b=0,z=-1,W=-1,et=0,ct=0,G=t,$=null;e:for(;;){for(var At;G!==s||c!==0&&G.nodeType!==3||(z=b+c),G!==m||l!==0&&G.nodeType!==3||(W=b+l),G.nodeType===3&&(b+=G.nodeValue.length),(At=G.firstChild)!==null;)$=G,G=At;for(;;){if(G===t)break e;if($===s&&++et===c&&(z=b),$===m&&++ct===l&&(W=b),(At=G.nextSibling)!==null)break;G=$,$=G.parentNode}G=At}s=z===-1||W===-1?null:{start:z,end:W}}else s=null}s=s||{start:0,end:0}}else s=null;for(Gh={focusedElem:t,selectionRange:s},Pr=!1,a=(a&335544064)===a,mn=n,n=a?9270:1024;mn!==null;){if(t=mn,a&&(s=t.deletions,s!==null))for(c=0;c<s.length;c++)a&&fh(s[c]);if(t.alternate===null&&(t.flags&2)!==0)a&&vg(t),vu(a);else{if(t.tag===22){if(s=t.alternate,t.memoizedState!==null){s!==null&&s.memoizedState===null&&a&&fh(s),vu(a);continue}else if(s!==null&&s.memoizedState!==null){a&&vg(t),vu(a);continue}}s=t.child,(t.subtreeFlags&n)!==0&&s!==null?(s.return=t,mn=s):(a&&xg(t),vu(a))}}ei=null}function vu(t){for(;mn!==null;){var n=mn,a=t,s=n.alternate,l=n.flags;switch(n.tag){case 0:case 11:case 15:break;case 1:if((l&1024)!==0&&s!==null){a=void 0,l=s.memoizedProps,s=s.memoizedState;var c=n.stateNode;try{var m=Cs(n.type,l);a=c.getSnapshotBeforeUpdate(m,s),c.__reactInternalSnapshotBeforeUpdate=a}catch(b){Ne(n,n.return,b)}}break;case 3:if((l&1024)!==0){if(s=n.stateNode.containerInfo,a=s.nodeType,a===9)jh(s);else if(a===1)switch(s.nodeName){case"HEAD":case"HTML":case"BODY":jh(s);break;default:s.textContent=""}}break;case 5:case 26:case 27:case 6:case 4:case 17:break;case 30:a&&s!==null&&(a=ia(s.memoizedProps,s.stateNode),l=n.memoizedProps,l=aa(l.default,l.update),l!=="none"&&gr(s,a,l,s.memoizedState=[],!0));break;default:if((l&1024)!==0)throw Error(r(163))}if(s=n.sibling,s!==null){s.return=n.return,mn=s;break}mn=n.return}}function bg(t,n,a){var s=a.flags;switch(a.tag){case 0:case 11:case 15:ki(t,a),s&4&&Bo(5,a);break;case 1:if(ki(t,a),s&4)if(t=a.stateNode,n===null)try{t.componentDidMount()}catch(m){Ne(a,a.return,m)}else{var l=Cs(a.type,n.memoizedProps);n=n.memoizedState;try{t.componentDidUpdate(l,n,t.__reactInternalSnapshotBeforeUpdate)}catch(m){Ne(a,a.return,m)}}s&64&&dg(a),s&512&&Hi(a,a.return);break;case 3:if(ki(t,a),s&64&&(t=a.updateQueue,t!==null)){if(n=null,a.child!==null)switch(a.child.tag){case 27:case 5:n=a.child.stateNode;break;case 1:n=a.child.stateNode}try{n_(t,n)}catch(m){Ne(a,a.return,m)}}break;case 27:n===null&&s&4&&gg(a);case 26:case 5:ki(t,a),n===null&&s&4&&sh(a),s&512&&Hi(a,a.return);break;case 12:ki(t,a);break;case 31:ki(t,a),s&4&&wg(t,a);break;case 13:ki(t,a),s&4&&Dg(t,a),s&64&&(t=a.memoizedState,t!==null&&(t=t.dehydrated,t!==null&&(a=Ax.bind(null,a),oM(t,a))));break;case 22:if(s=a.memoizedState!==null||pn,!s){var c=n!==null&&n.memoizedState!==null||we;n=pn,l=we,pn=s,(we=c)&&!l?(s=2,(a.subtreeFlags&8772)!==0&&(s|=1),Ai(t,a,s)):ki(t,a),pn=n,we=l}break;case 30:ki(t,a),s&512&&Hi(a,a.return);break;case 7:s&512&&Hi(a,a.return);default:ki(t,a)}}function _h(t,n){for(t=t.child;t!==null;)Ag(t,n),t=t.sibling}function Ag(t,n){switch(t.tag){case 5:case 26:try{var a=t.stateNode;if(n){var s=a.style;typeof s.setProperty=="function"?s.setProperty("display","none","important"):s.display="none"}else{var l=t.stateNode,c=t.memoizedProps.style,m=c!=null&&c.hasOwnProperty("display")?c.display:null;l.style.display=m==null||typeof m=="boolean"?"":(""+m).trim()}}catch(z){Ne(t,t.return,z)}gh(t,n);break;case 6:try{t.stateNode.nodeValue=n?"":t.memoizedProps,Re=!0}catch(z){Ne(t,t.return,z)}break;case 18:try{var b=t.stateNode;n?v0(b,!0):v0(t.stateNode,!1)}catch(z){Ne(t,t.return,z)}break;case 22:case 23:t.memoizedState===null&&_h(t,n);break;default:_h(t,n)}}function gh(t,n){if(t.subtreeFlags&67108864)for(t=t.child;t!==null;){t:{var a=t,s=n;switch(a.tag){case 4:Ag(a,s);break t;case 22:a.memoizedState===null&&gh(a,s);break t;default:gh(a,s)}}t=t.sibling}}function Rg(t){var n=t.alternate;n!==null&&(t.alternate=null,Rg(n)),t.child=null,t.deletions=null,t.sibling=null,t.tag===5&&(n=t.stateNode,n!==null&&Cn(n)),t.stateNode=null,t.return=null,t.dependencies=null,t.memoizedProps=null,t.memoizedState=null,t.pendingProps=null,t.stateNode=null,t.updateQueue=null}var Ye=null,Xn=!1;function Ti(t,n,a){for(a=a.child;a!==null;)Cg(t,n,a),a=a.sibling}function Cg(t,n,a){if(qe&&typeof qe.onCommitFiberUnmount=="function")try{qe.onCommitFiberUnmount(tn,a)}catch{}switch(a.tag){case 26:we||Mn(a,n),Ti(t,n,a),a.memoizedState?a.memoizedState.count--:a.stateNode&&!we&&(a=a.stateNode,a.parentNode.removeChild(a));break;case 27:we||Mn(a,n),Fo(a);var s=Ye,l=Xn;qa(a.type)&&(Ye=a.stateNode,Xn=!1),Ti(t,n,a),N0(a.stateNode,a.type,a.memoizedProps),Ye=s,Xn=l;break;case 5:we||Mn(a,n),Fo(a);case 6:if(a.tag===6&&Fo(a),s=Ye,l=Xn,Ye=null,Ti(t,n,a),Ye=s,Xn=l,Ye!==null)if(Xn)try{(Ye.nodeType===9?Ye.body:Ye.nodeName==="HTML"?Ye.ownerDocument.body:Ye).removeChild(a.stateNode),Re=!0}catch(c){Ne(a,n,c)}else try{Ye.removeChild(a.stateNode),Re=!0}catch(c){Ne(a,n,c)}break;case 18:Ye!==null&&(Xn?(t=Ye,g0(t.nodeType===9?t.body:t.nodeName==="HTML"?t.ownerDocument.body:t,a.stateNode),zr(t)):g0(Ye,a.stateNode));break;case 4:s=Ye,l=Xn,Ye=a.stateNode.containerInfo,Xn=!0,Ti(t,n,a),Ye=s,Xn=l;break;case 0:case 11:case 14:case 15:Fa(2,a,n),we||Fa(4,a,n),Ti(t,n,a);break;case 1:we||(Mn(a,n),s=a.stateNode,typeof s.componentWillUnmount=="function"&&pg(a,n,s)),Ti(t,n,a);break;case 21:Ti(t,n,a);break;case 22:we=(s=we)||a.memoizedState!==null,Ti(t,n,a),we=s;break;case 30:Mn(a,n),Ti(t,n,a);break;case 7:we||Mn(a,n),Ti(t,n,a);break;default:Ti(t,n,a)}}function wg(t,n){if(n.memoizedState===null&&(t=n.alternate,t!==null&&(t=t.memoizedState,t!==null))){t=t.dehydrated;try{zr(t)}catch(a){Ne(n,n.return,a)}}}function Dg(t,n){if(n.memoizedState===null&&(t=n.alternate,t!==null&&(t=t.memoizedState,t!==null&&(t=t.dehydrated,t!==null))))try{zr(t)}catch(a){Ne(n,n.return,a)}}function mx(t){switch(t.tag){case 31:case 13:case 19:var n=t.stateNode;return n===null&&(n=t.stateNode=new Tg),n;case 22:return t=t.stateNode,n=t._retryCache,n===null&&(n=t._retryCache=new Tg),n;default:throw Error(r(435,t.tag))}}function Su(t,n){var a=mx(t);n.forEach(function(s){if(!a.has(s)){a.add(s);var l=Rx.bind(null,t,s);s.then(l,l)}})}function zn(t,n,a){var s=n.deletions;if(s!==null)for(var l=0;l<s.length;l++){var c=s[l],m=t,b=n,z=b;t:for(;z!==null;){switch(z.tag){case 27:if(qa(z.type)){Ye=z.stateNode,Xn=!1;break t}break;case 5:Ye=z.stateNode,Xn=!1;break t;case 3:case 4:Ye=z.stateNode.containerInfo,Xn=!0;break t}z=z.return}if(Ye===null)throw Error(r(160));Cg(m,b,c),Ye=null,Xn=!1,m=c.alternate,m!==null&&(m.return=null),c.return=null}if(n.subtreeFlags&13886)for(n=n.child;n!==null;)Ug(n,t,a),n=n.sibling}var bi=null;function Ug(t,n,a){var s=t.alternate,l=t.flags;switch(t.tag){case 0:case 11:case 14:case 15:if(l&4&&(s=t.updateQueue,s=s!==null?s.events:null,s!==null))for(var c=0;c<s.length;c++){var m=s[c];m.ref.impl=m.nextImpl}zn(n,t,a),In(t),l&4&&(Fa(3,t,t.return),Bo(3,t),Fa(5,t,t.return));break;case 1:zn(n,t,a),In(t),l&512&&(we||s===null||Mn(s,s.return)),l&64&&pn&&(t=t.updateQueue,t!==null&&(n=t.callbacks,n!==null&&(a=t.shared.hiddenCallbacks,t.shared.hiddenCallbacks=a===null?n:a.concat(n))));break;case 26:if(c=bi,zn(n,t,a),In(t),l&512&&(we||s===null||Mn(s,s.return)),l&4)if(l=s!==null?s.memoizedState:null,a=t.memoizedState,s===null)if(a===null)if(t.stateNode===null)if(pn)t.stateNode=p0(t.type,t.memoizedProps,n.containerInfo,t);else{t:{n=t.type,a=t.memoizedProps,l=c.ownerDocument||c;e:switch(n){case"title":s=l.getElementsByTagName("title")[0],(!s||s[We]||s[Ut]||s.namespaceURI==="http://www.w3.org/2000/svg"||s.hasAttribute("itemprop"))&&(s=l.createElement(n),l.head.insertBefore(s,l.querySelector("head > title"))),En(s,n,a),s[Ut]=t,Be(s),n=s;break t;case"link":if(c=B0("link","href",l).get(n+(a.href||""))){for(m=0;m<c.length;m++)if(s=c[m],s.getAttribute("href")===(a.href==null||a.href===""?null:a.href)&&s.getAttribute("rel")===(a.rel==null?null:a.rel)&&s.getAttribute("title")===(a.title==null?null:a.title)&&s.getAttribute("crossorigin")===(a.crossOrigin==null?null:a.crossOrigin)){c.splice(m,1);break e}}s=l.createElement(n),En(s,n,a),l.head.appendChild(s);break;case"meta":if(c=B0("meta","content",l).get(n+(a.content||""))){for(m=0;m<c.length;m++)if(s=c[m],s.getAttribute("content")===(a.content==null?null:""+a.content)&&s.getAttribute("name")===(a.name==null?null:a.name)&&s.getAttribute("property")===(a.property==null?null:a.property)&&s.getAttribute("http-equiv")===(a.httpEquiv==null?null:a.httpEquiv)&&s.getAttribute("charset")===(a.charSet==null?null:a.charSet)){c.splice(m,1);break e}}s=l.createElement(n),En(s,n,a),l.head.appendChild(s);break;default:throw Error(r(468,n))}s[Ut]=t,Be(s),n=s}t.stateNode=n}else pn||ed(c,t.type,t.stateNode);else t.stateNode=I0(c,a,t.memoizedProps);else l!==a?(l===null?(n=s.stateNode,n===null||we||n.parentNode.removeChild(n)):l.count--,a===null?pn||ed(c,t.type,t.stateNode):I0(c,a,t.memoizedProps)):a===null&&t.stateNode!==null&&rh(t,t.memoizedProps,s.memoizedProps);break;case 27:zn(n,t,a),In(t),l&512&&(we||s===null||Mn(s,s.return)),s!==null&&l&4&&rh(t,t.memoizedProps,s.memoizedProps);break;case 5:if(c=Xi,Xi=!1,zn(n,t,a),Xi=c,In(t),l&512&&(we||s===null||Mn(s,s.return)),t.flags&32){n=t.stateNode;try{$s(n,""),Re=!0}catch(et){Ne(t,t.return,et)}}l&4&&t.stateNode!=null&&(n=t.memoizedProps,rh(t,n,s!==null?s.memoizedProps:n)),l&1024&&(ph=!0);break;case 6:if(zn(n,t,a),In(t),l&4){if(t.stateNode===null)throw Error(r(162));n=t.memoizedProps,a=t.stateNode;try{a.nodeValue=n,Re=!0}catch(et){Ne(t,t.return,et)}}break;case 3:if(Re=!1,Ou=null,c=bi,bi=Zo(n.containerInfo),zn(n,t,a),bi=c,In(t),l&4&&s!==null&&s.memoizedState.isDehydrated)try{zr(n.containerInfo)}catch(et){Ne(t,t.return,et)}ph&&(ph=!1,Ng(t)),Re=!1;break;case 4:l=Xi,Xi=pn,s=Jp(),c=bi,bi=Zo(t.stateNode.containerInfo),zn(n,t,a),In(t),bi=c,Re&&Ho&&(gu=!0),Re=s,Xi=l;break;case 12:zn(n,t,a),In(t);break;case 31:zn(n,t,a),In(t),l&4&&(n=t.updateQueue,n!==null&&(t.updateQueue=null,Su(t,n)));break;case 13:zn(n,t,a),In(t),t.child.flags&8192&&t.memoizedState!==null!=(s!==null&&s.memoizedState!==null)&&(Mu=Tt()),l&4&&(n=t.updateQueue,n!==null&&(t.updateQueue=null,Su(t,n)));break;case 22:c=t.memoizedState!==null,m=s!==null&&s.memoizedState!==null;var b=pn,z=we,W=Xi;pn=b||c,Xi=W||c,we=z||m,zn(n,t,a),we=z,Xi=W,pn=b,In(t),l&8192&&(n=t.stateNode,n._visibility=c?n._visibility&-2:n._visibility|1,!c||s===null||m||pn||we||(n=m||we,a=pn,s=we,pn=c||pn,we=n,Ha(t,2),pn=a,we=s),!c&&Xi||_h(t,c)),l&4&&(n=t.updateQueue,n!==null&&(a=n.retryQueue,a!==null&&(n.retryQueue=null,Su(t,a))));break;case 19:zn(n,t,a),In(t),l&4&&(n=t.updateQueue,n!==null&&(t.updateQueue=null,Su(t,n)));break;case 30:l&512&&(we||s===null||Mn(s,s.return)),l=Jp(),c=Ho,m=(a&335544064)===a,b=t.memoizedProps,Ho=m&&aa(b.default,b.update)!=="none",zn(n,t,a),In(t),m&&s!==null&&Re&&(t.flags|=4),Ho=c,Re=l;break;case 21:break;case 7:l&512&&(we||s===null||Mn(s,s.return)),s&&s.stateNode!==null&&(s.stateNode._fragmentFiber=t);default:zn(n,t,a),In(t)}}function In(t){var n=t.flags;if(n&2){try{for(var a,s=t.return;s!==null;){if(_g(s)){a=s;break}s=s.return}s=null;for(var l=t.return;l!==null;){if(ah(l)){var c=l.stateNode;s===null?s=[c]:s.push(c)}if(ih(l))break;l=l.return}var m=s;if(a==null)throw Error(r(160));switch(a.tag){case 27:var b=a.stateNode,z=oh(t);du(t,z,b,m);break;case 5:var W=a.stateNode;a.flags&32&&($s(W,""),a.flags&=-33);var et=oh(t);du(t,et,W,m);break;case 3:case 4:var ct=a.stateNode.containerInfo,G=oh(t);lh(t,G,ct,m);break;default:throw Error(r(161))}}catch($){Ne(t,t.return,$)}t.flags&=-3}n&4096&&(t.flags&=-4097)}function Ng(t){if(t.subtreeFlags&1024)for(t=t.child;t!==null;){var n=t;Ng(n),n.tag===5&&n.flags&1024&&(n=n.stateNode,Pr=!0,n.reset(),Pr=!1),t=t.sibling}}function vr(t,n){if(n.subtreeFlags&9270)for(n=n.child;n!==null;)Lg(n,t),n=n.sibling;else Eg(n)}function Lg(t,n){var a=t.alternate;if(a===null)uh(t,!1);else switch(t.tag){case 3:if(mh=Yi=!1,Sg(),vr(n,t),!Yi&&!gu){if(t=Gi,t!==null)for(var s=0;s<t.length;s+=3){a=t[s];var l=t[s+1];y0(a,t[s+2]),a=a.ownerDocument.documentElement,a!==null&&a.animate({opacity:[0,0],pointerEvents:["none","none"]},{duration:0,fill:"forwards",pseudoElement:"::view-transition-group("+l+")"})}t=n.containerInfo,t=t.nodeType===9?t.documentElement:t.ownerDocument.documentElement,t!==null&&t.style.viewTransitionName===""&&(t.style.viewTransitionName="none",t.animate({opacity:[0,0],pointerEvents:["none","none"]},{duration:0,fill:"forwards",pseudoElement:"::view-transition-group(root)"}),t.animate({width:[0,0],height:[0,0]},{duration:0,fill:"forwards",pseudoElement:"::view-transition"})),mh=!0}Gi=null;break;case 5:vr(n,t);break;case 4:s=Yi,Yi=!1,vr(n,t),Yi&&(gu=!0),Yi=s;break;case 22:t.memoizedState===null&&(a.memoizedState!==null?uh(t,!1):vr(n,t));break;case 30:s=Yi,l=Sg(),Yi=!1,vr(n,t),Yi&&(t.flags|=4);var c=t.memoizedProps,m=t.stateNode;n=ia(c,m),m=ia(a.memoizedProps,m);var b=aa(c.default,c.update);b==="none"?n=!1:(c=a.memoizedState,a.memoizedState=null,a=t.child,Vn=0,n=dh(t,a,n,m,b,c,!0),Vn!==(c===null?0:c.length)&&(t.flags|=32)),(t.flags&4)!==0&&n?(br(t,t.memoizedProps.onUpdate),Gi=l):l!==null&&(l.push.apply(l,Gi),Gi=l),Yi=(t.flags&32)!==0?!0:s;break;default:vr(n,t)}}function ki(t,n){if(n.subtreeFlags&8772)for(n=n.child;n!==null;)bg(t,n.alternate,n),n=n.sibling}function Ha(t,n){for(t=t.child;t!==null;){var a=t,s=n;switch(a.tag){case 0:case 11:case 14:case 15:Fa(4,a,a.return),Ha(a,s);break;case 1:Mn(a,a.return);var l=a.stateNode;typeof l.componentWillUnmount=="function"&&pg(a,a.return,l),Ha(a,s);break;case 27:(s&2)!==0&&N0(a.stateNode,a.type,a.memoizedProps);case 5:Mn(a,a.return),a.tag!==5&&a.tag!==27||Fo(a),Ha(a,s);break;case 6:Fo(a);break;case 26:Mn(a,a.return),l=a.stateNode,a.memoizedState!==null||l===null||we||l.parentNode.removeChild(l),Ha(a,s);break;case 22:a.memoizedState===null&&Ha(a,s);break;case 30:Mn(a,a.return),Ha(a,s);break;case 7:Mn(a,a.return);default:Ha(a,s)}t=t.sibling}}function Ai(t,n,a){for(a=(n.subtreeFlags&8772)!==0?a:a&-2,n=n.child;n!==null;){var s=n.alternate,l=t,c=n,m=c.flags,b=(a&1)!==0;switch(c.tag){case 0:case 11:case 15:Ai(l,c,a),Bo(4,c);break;case 1:if(Ai(l,c,a),s=c,l=s.stateNode,typeof l.componentDidMount=="function")try{l.componentDidMount()}catch(et){Ne(s,s.return,et)}if(s=c,l=s.updateQueue,l!==null){var z=s.stateNode;try{var W=l.shared.hiddenCallbacks;if(W!==null)for(l.shared.hiddenCallbacks=null,l=0;l<W.length;l++)e_(W[l],z)}catch(et){Ne(s,s.return,et)}}b&&m&64&&dg(c),Hi(c,c.return);break;case 27:(a&2)!==0&&gg(c);case 5:c.tag!==5&&c.tag!==27||mg(c),Ai(l,c,a),b&&s===null&&m&4&&sh(c),Hi(c,c.return);break;case 6:mg(c);break;case 26:z=c.stateNode,c.memoizedState!==null||z===null||pn||ed(Zo(z.ownerDocument),c.type,z),Ai(l,c,a),b&&s===null&&m&4&&sh(c),Hi(c,c.return);break;case 12:Ai(l,c,a);break;case 31:Ai(l,c,a),b&&m&4&&wg(l,c);break;case 13:Ai(l,c,a),b&&m&4&&Dg(l,c);break;case 22:c.memoizedState===null&&Ai(l,c,a),Hi(c,c.return);break;case 30:Ai(l,c,a),Hi(c,c.return);break;case 7:Hi(c,c.return);default:Ai(l,c,a)}n=n.sibling}}function vh(t,n){var a=null;t!==null&&t.memoizedState!==null&&t.memoizedState.cachePool!==null&&(a=t.memoizedState.cachePool.pool),t=null,n.memoizedState!==null&&n.memoizedState.cachePool!==null&&(t=n.memoizedState.cachePool.pool),t!==a&&(t!=null&&t.refCount++,a!=null&&bo(a))}function Sh(t,n){t=null,n.alternate!==null&&(t=n.alternate.memoizedState.cache),n=n.memoizedState.cache,n!==t&&(n.refCount++,t!=null&&bo(t))}function mi(t,n,a,s){var l=(a&335544064)===a;if(n.subtreeFlags&(l?10262:10256))for(n=n.child;n!==null;)Og(t,n,a,s),n=n.sibling;else l&&Mg(n)}function Og(t,n,a,s){var l=(a&335544064)===a;l&&n.alternate===null&&n.return!==null&&n.return.alternate!==null&&_u(n);var c=n.flags;switch(n.tag){case 0:case 11:case 15:mi(t,n,a,s),c&2048&&Bo(9,n);break;case 1:mi(t,n,a,s);break;case 3:mi(t,n,a,s),l&&mh&&(t=t.containerInfo,t=t.nodeType===9?t.body:t.nodeName==="HTML"?t.ownerDocument.body:t,t.style.viewTransitionName==="root"&&(t.style.viewTransitionName=""),t=t.ownerDocument.documentElement,t!==null&&t.style.viewTransitionName==="none"&&(t.style.viewTransitionName="")),c&2048&&(c=null,n.alternate!==null&&(c=n.alternate.memoizedState.cache),n=n.memoizedState.cache,n!==c&&(n.refCount++,c!=null&&bo(c)));break;case 12:if(c&2048){mi(t,n,a,s),c=n.stateNode;try{var m=n.memoizedProps,b=m.id,z=m.onPostCommit;typeof z=="function"&&z(b,n.alternate===null?"mount":"update",c.passiveEffectDuration,-0)}catch(W){Ne(n,n.return,W)}}else mi(t,n,a,s);break;case 31:mi(t,n,a,s);break;case 13:mi(t,n,a,s);break;case 23:break;case 22:m=n.stateNode,b=n.alternate,n.memoizedState!==null?(l&&b!==null&&b.memoizedState===null&&_u(b),m._visibility&2?mi(t,n,a,s):Go(t,n)):(l&&b!==null&&b.memoizedState!==null&&_u(n),m._visibility&2?mi(t,n,a,s):(m._visibility|=2,Sr(t,n,a,s,(n.subtreeFlags&10256)!==0||!1))),c&2048&&vh(b,n);break;case 24:mi(t,n,a,s),c&2048&&Sh(n.alternate,n);break;case 30:l&&(c=n.alternate,c!==null&&(Vi(c.child,!0),Vi(n.child,!0))),mi(t,n,a,s);break;default:mi(t,n,a,s)}}function Sr(t,n,a,s,l){for(l=l&&((n.subtreeFlags&10256)!==0||!1),n=n.child;n!==null;){var c=t,m=n,b=a,z=s,W=m.flags;switch(m.tag){case 0:case 11:case 15:Sr(c,m,b,z,l),Bo(8,m);break;case 23:break;case 22:var et=m.stateNode;m.memoizedState!==null?et._visibility&2?Sr(c,m,b,z,l):Go(c,m):(et._visibility|=2,Sr(c,m,b,z,l)),l&&W&2048&&vh(m.alternate,m);break;case 24:Sr(c,m,b,z,l),l&&W&2048&&Sh(m.alternate,m);break;default:Sr(c,m,b,z,l)}n=n.sibling}}function Go(t,n){if(n.subtreeFlags&10256)for(n=n.child;n!==null;){var a=t,s=n,l=s.flags;switch(s.tag){case 22:Go(a,s),l&2048&&vh(s.alternate,s);break;case 24:Go(a,s),l&2048&&Sh(s.alternate,s);break;default:Go(a,s)}n=n.sibling}}var ws=8192;function Ds(t,n,a){if(t.subtreeFlags&ws)for(t=t.child;t!==null;)Pg(t,n,a),t=t.sibling}function Pg(t,n,a){switch(t.tag){case 26:Ds(t,n,a),t.flags&ws&&(t.memoizedState!==null?xM(a,bi,t.memoizedState,t.memoizedProps):(t=t.stateNode,(n&335544128)===n&&V0(a,t)));break;case 5:Ds(t,n,a),t.flags&ws&&(t=t.stateNode,(n&335544128)===n&&V0(a,t));break;case 3:case 4:var s=bi;bi=Zo(t.stateNode.containerInfo),Ds(t,n,a),bi=s;break;case 22:t.memoizedState===null&&(s=t.alternate,s!==null&&s.memoizedState!==null?(s=ws,ws=16777216,Ds(t,n,a),ws=s):Ds(t,n,a));break;case 30:if((t.flags&ws)!==0&&(s=t.memoizedProps.name,s!=null&&s!=="auto")){var l=t.stateNode;l.paired=null,ei===null&&(ei=new Map),ei.set(s,l)}Ds(t,n,a);break;default:Ds(t,n,a)}}function zg(t){var n=t.alternate;if(n!==null&&(t=n.child,t!==null)){n.child=null;do n=t.sibling,t.sibling=null,t=n;while(t!==null)}}function Vo(t){var n=t.deletions;if((t.flags&16)!==0){if(n!==null)for(var a=0;a<n.length;a++){var s=n[a];mn=s,Bg(s,t)}zg(t)}if(t.subtreeFlags&10256)for(t=t.child;t!==null;)Ig(t),t=t.sibling}function Ig(t){switch(t.tag){case 0:case 11:case 15:Vo(t),t.flags&2048&&Fa(9,t,t.return);break;case 3:Vo(t);break;case 12:Vo(t);break;case 22:var n=t.stateNode;t.memoizedState!==null&&n._visibility&2&&(t.return===null||t.return.tag!==13)?(n._visibility&=-3,yu(t)):Vo(t);break;default:Vo(t)}}function yu(t){var n=t.deletions;if((t.flags&16)!==0){if(n!==null)for(var a=0;a<n.length;a++){var s=n[a];mn=s,Bg(s,t)}zg(t)}for(t=t.child;t!==null;){switch(n=t,n.tag){case 0:case 11:case 15:Fa(8,n,n.return),yu(n);break;case 22:a=n.stateNode,a._visibility&2&&(a._visibility&=-3,yu(n));break;default:yu(n)}t=t.sibling}}function Bg(t,n){for(;mn!==null;){var a=mn;switch(a.tag){case 0:case 11:case 15:Fa(8,a,n);break;case 23:case 22:if(a.memoizedState!==null&&a.memoizedState.cachePool!==null){var s=a.memoizedState.cachePool.pool;s!=null&&s.refCount++}break;case 24:bo(a.memoizedState.cache)}if(s=a.child,s!==null)s.return=a,mn=s;else t:for(a=t;mn!==null;){s=mn;var l=s.sibling,c=s.return;if(Rg(s),s===a){mn=null;break t}if(l!==null){l.return=c,mn=l;break t}mn=c}}}var _x={getCacheForType:function(t){var n=Sn(nn),a=n.data.get(t);return a===void 0&&(a=t(),n.data.set(t,a)),a},cacheSignal:function(){return Sn(nn).controller.signal}},gx=typeof WeakMap=="function"?WeakMap:Map,Ce=0,Fe=null,_e=null,ve=0,Ue=0,ni=null,Ga=!1,yr=!1,yh=!1,da=0,Qe=0,Va=0,Us=0,xu=0,ii=0,xr=0,Xo=null,Yn=null,xh=!1,Mu=0,Fg=0,Eu=1/0,Tu=null,Xa=null,je=0,Ri=null,Ns=null,qi=0,Mh=0,Eh=null,Hg=null,Mr=null,Er=null,Tr=null,Yo=0,bu=null;function ai(){return(Ce&2)!==0&&ve!==0?ve&-ve:Mt.T!==null?Lh():Yt()}function Gg(){if(ii===0)if((ve&536870912)===0||de){var t=Qi;Qi<<=1,(Qi&3932160)===0&&(Qi=262144),ii=t}else ii=536870912;return t=yn.current,t!==null&&(t.flags|=32),ii}function br(t,n){if(n!=null){var a=t.stateNode,s=a.ref;s===null&&(s=a.ref=x0(ia(t.memoizedProps,a))),Er===null&&(Er=[]),Er.push(n.bind(null,s))}}function kn(t,n,a){(t===Fe&&(Ue===2||Ue===9)||t.cancelPendingCommit!==null)&&(Ar(t,0),Ya(t,ve,ii,!1)),k(t,a),((Ce&2)===0||t!==Fe)&&(t===Fe&&((Ce&2)===0&&(Us|=a),Qe===4&&Ya(t,ve,ii,!1)),Wi(t))}function Vg(t,n,a){if((Ce&6)!==0)throw Error(r(327));var s=!a&&(n&127)===0&&(n&t.expiredLanes)===0||ba(t,n),l=s?yx(t,n):bh(t,n,!0),c=s;do{if(l===0){yr&&!s&&Ya(t,n,0,!1);break}else{if(a=t.current.alternate,c&&!vx(a)){l=bh(t,n,!1),c=!1;continue}if(l===2){if(c=n,t.errorRecoveryDisabledLanes&c)var m=0;else m=t.pendingLanes&-536870913,m=m!==0?m:m&536870912?536870912:0;if(m!==0){n=m;t:{var b=t;l=Xo;var z=b.current.memoizedState.isDehydrated;if(z&&(Ar(b,m).flags|=256),m=bh(b,m,!1),m!==2&&m!==6){if(yh&&!z){b.errorRecoveryDisabledLanes|=c,Us|=c,l=4;break t}c=Yn,Yn=l,c!==null&&(Yn===null?Yn=c:Yn.push.apply(Yn,c))}l=m}if(c=!1,l!==2)continue}}if(l===1){Ar(t,0),Ya(t,n,0,!0);break}t:{switch(s=t,c=l,c){case 0:case 1:throw Error(r(345));case 4:if((n&4194048)!==n&&(n&62914560)!==n)break;case 6:Ya(s,n,ii,!Ga);break t;case 2:Yn=null;break;case 3:case 5:break;default:throw Error(r(329))}if((n&62914560)===n&&(l=Mu+300-Tt(),10<l)){if(Ya(s,n,ii,!Ga),ds(s,0,!0)!==0)break t;qi=n,s.timeoutHandle=Yh(Xg.bind(null,s,a,Yn,Tu,xh,n,ii,Us,xr,Ga,c,"Throttled",-0,0),l);break t}Xg(s,a,Yn,Tu,xh,n,ii,Us,xr,Ga,c,null,-0,0)}}break}while(!0);Wi(t)}function Xg(t,n,a,s,l,c,m,b,z,W,et,ct,G,$){t.timeoutHandle=-1;var At=n.subtreeFlags,Vt=(c&335544064)===c;if(ct=null,(Vt||At&8192||(At&16785408)===16785408)&&(ct={stylesheets:null,count:0,imgCount:0,imgBytes:0,suspenseyImages:[],waitingForImages:!0,waitingForViewTransition:!1,unsuspend:Ii},ei=null,Pg(n,c,ct),Vt&&(At=ct,Vt=t.containerInfo,Vt=(Vt.nodeType===9?Vt:Vt.ownerDocument).__reactViewTransition,Vt!=null&&(At.count++,At.waitingForViewTransition=!0,At=Jo.bind(At),Vt.finished.then(At,At))),At=(c&62914560)===c?Mu-Tt():(c&4194048)===c?Fg-Tt():0,At=MM(ct,At),At!==null)){qi=c,t.cancelPendingCommit=At(Qg.bind(null,t,n,c,a,s,l,m,b,z,W,et,ct,null,G,$)),Ya(t,c,m,!W);return}Qg(t,n,c,a,s,l,m,b,z,W,et,ct)}function vx(t){for(var n=t;;){var a=n.tag;if((a===0||a===11||a===15)&&n.flags&16384&&(a=n.updateQueue,a!==null&&(a=a.stores,a!==null)))for(var s=0;s<a.length;s++){var l=a[s],c=l.getSnapshot;l=l.value;try{if(!$n(c(),l))return!1}catch{return!1}}if(a=n.child,n.subtreeFlags&16384&&a!==null)a.return=n,n=a;else{if(n===t)break;for(;n.sibling===null;){if(n.return===null||n.return===t)return!0;n=n.return}n.sibling.return=n.return,n=n.sibling}}return!0}function Ya(t,n,a,s){n=Ml(t,n),n&=~xu,n&=~Us,t.suspendedLanes|=n,t.pingedLanes&=~n,s&&(t.warmLanes|=n),s=t.expirationTimes;for(var l=n;0<l;){var c=31-Rn(l),m=1<<c;s[c]=-1,l&=~m}a!==0&&st(t,a,n)}function Au(){return(Ce&6)===0?(ko(0),!1):!0}function Th(){if(_e!==null){if(Ue===0)var t=_e.return;else t=_e,oa=Ss=null,Nf(t),hr=null,Co=0,t=_e;for(;t!==null;)hg(t.alternate,t),t=t.return;_e=null}}function Ar(t,n){var a=t.timeoutHandle;return a!==-1&&(t.timeoutHandle=-1,Vx(a)),a=t.cancelPendingCommit,a!==null&&(t.cancelPendingCommit=null,a()),qi=0,Th(),Fe=t,_e=a=sa(t.current,null),ve=n,Ue=0,ni=null,Ga=!1,yr=ba(t,n),yh=!1,xr=ii=xu=Us=Va=Qe=0,Yn=Xo=null,xh=!1,da=Ml(t,n),Ol(),a}function Yg(t,n){se=null,Mt.H=su,n===fr||n===kl?(n=Qm(),Ue=3):n===Sf?(n=Qm(),Ue=4):Ue=n===Wf?8:n!==null&&typeof n=="object"&&typeof n.then=="function"?6:1,ni=n,_e===null&&(Qe=1,ru(t,fi(n,t.current)))}function kg(){var t=yn.current;return t===null?!0:(ve&4194048)===ve?wn===null:(ve&62914560)===ve||(ve&536870912)!==0?t===wn:!1}function qg(){var t=Mt.H;return Mt.H=su,t===null?su:t}function Wg(){var t=Mt.A;return Mt.A=_x,t}function Ru(){Qe=4,Ga||(ve&4194048)!==ve&&yn.current!==null||(yr=!0),(Va&134217727)===0&&(Us&134217727)===0||Fe===null||Ya(Fe,ve,ii,!1)}function bh(t,n,a){var s=Ce;Ce|=2;var l=qg(),c=Wg();(Fe!==t||ve!==n)&&(Tu=null,Ar(t,n)),n=!1;var m=Qe;t:do try{if(Ue!==0&&_e!==null){var b=_e,z=ni;switch(Ue){case 8:Th(),m=6;break t;case 3:case 2:case 9:case 6:yn.current===null&&(n=!0);var W=Ue;if(Ue=0,ni=null,Rr(t,b,z,W),a&&yr){m=0;break t}break;default:W=Ue,Ue=0,ni=null,Rr(t,b,z,W)}}Sx(),m=Qe;break}catch(et){Yg(t,et)}while(!0);return n&&t.shellSuspendCounter++,oa=Ss=null,Ce=s,Mt.H=l,Mt.A=c,_e===null&&(Fe=null,ve=0,Ol()),m}function Sx(){for(;_e!==null;)jg(_e)}function yx(t,n){var a=Ce;Ce|=2;var s=qg(),l=Wg();Fe!==t||ve!==n?(Tu=null,Eu=Tt()+500,Ar(t,n)):yr=ba(t,n);t:do try{if(Ue!==0&&_e!==null){n=_e;var c=ni;e:switch(Ue){case 1:Ue=0,ni=null,Rr(t,n,c,1);break;case 2:case 9:if(Zm(c)){Ue=0,ni=null,Zg(n);break}n=function(){Ue!==2&&Ue!==9||Fe!==t||(Ue=7),Wi(t)},c.then(n,n);break t;case 3:Ue=7;break t;case 4:Ue=5;break t;case 7:Zm(c)?(Ue=0,ni=null,Zg(n)):(Ue=0,ni=null,Rr(t,n,c,7));break;case 5:var m=null;switch(_e.tag){case 26:m=_e.memoizedState;case 5:case 27:var b=_e;if(m?H0(m):b.stateNode.complete){Ue=0,ni=null;var z=b.sibling;if(z!==null)_e=z;else{var W=b.return;W!==null?(_e=W,Cu(W)):_e=null}break e}}Ue=0,ni=null,Rr(t,n,c,5);break;case 6:Ue=0,ni=null,Rr(t,n,c,6);break;case 8:Th(),Qe=6;break t;default:throw Error(r(462))}}xx();break}catch(et){Yg(t,et)}while(!0);return oa=Ss=null,Mt.H=s,Mt.A=l,Ce=a,_e!==null?0:(Fe=null,ve=0,Ol(),Qe)}function xx(){for(;_e!==null&&!Oe();)jg(_e)}function jg(t){var n=cg(t.alternate,t,da);t.memoizedProps=t.pendingProps,n===null?Cu(t):_e=n}function Zg(t){var n=t,a=n.alternate;switch(n.tag){case 15:case 0:n=ig(a,n,n.pendingProps,n.type,void 0,ve);break;case 11:n=ig(a,n,n.pendingProps,n.type.render,n.ref,ve);break;case 5:Nf(n);var s=n;s===dn&&(de?(Hl(s),s.tag===5&&s.stateNode!=null&&(He=s.stateNode)):(Hl(s),de=!0));default:hg(a,n),n=_e=Bm(n,da),n=cg(a,n,da)}t.memoizedProps=t.pendingProps,n===null?Cu(t):_e=n}function Rr(t,n,a,s){oa=Ss=null,Nf(n),hr=null,Co=0;var l=n.return;try{if(lx(t,l,n,a,ve)){Qe=1,ru(t,fi(a,t.current)),_e=null;return}}catch(c){if(l!==null)throw _e=l,c;Qe=1,ru(t,fi(a,t.current)),_e=null;return}n.flags&32768?(de||s===1?t=!0:yr||(ve&536870912)!==0?t=!1:(Ga=t=!0,(s===2||s===9||s===3||s===6)&&(s=yn.current,s!==null&&s.tag===13&&(s.flags|=16384))),Kg(n,t)):Cu(n)}function Cu(t){var n=t;do{if((n.flags&32768)!==0){Kg(n,Ga);return}t=n.return;var a=hx(n.alternate,n,da);if(a!==null){_e=a;return}if(n=n.sibling,n!==null){_e=n;return}_e=n=t}while(n!==null);Qe===0&&(Qe=5)}function Kg(t,n){do{var a=dx(t.alternate,t);if(a!==null){a.flags&=32767,_e=a;return}if(a=t.return,a!==null&&(a.flags|=32768,a.subtreeFlags=0,a.deletions=null),!n&&(t=t.sibling,t!==null)){_e=t;return}_e=t=a}while(t!==null);Qe=6,_e=null}function Qg(t,n,a,s,l,c,m,b,z,W,et,ct){t.cancelPendingCommit=null;do wu();while(je!==0);if((Ce&6)!==0)throw Error(r(327));if(n!==null){if(n===t.current)throw Error(r(177));t===Fe&&(_e=Fe=null,ve=0),Ns=n,Ri=t,qi=a,Eh=l,Hg=s,Mx(t,n,a,m,b,z,ct)}}function Mx(t,n,a,s,l,c,m){var b=n.lanes|n.childLanes;if(Mh=b,b|=rf,it(t,a,b,s,l,c),Er=null,(a&335544064)===a?(Tr=Ky(t),s=10262):(Tr=null,s=10256),(n.subtreeFlags&s)!==0||(n.flags&s)!==0?(t.callbackNode=null,t.callbackPriority=0,Cx(Ot,function(){return wh(),null})):(t.callbackNode=null,t.callbackPriority=0),pu=!1,s=(n.flags&13878)!==0,(n.subtreeFlags&13878)!==0||s){s=Mt.T,Mt.T=null,l=bt.p,bt.p=2,c=Ce,Ce|=4;try{px(t,n,a)}finally{Ce=c,bt.p=l,Mt.T=s}}je=1,pu?Mr=jx(m,t.containerInfo,Tr,Ah,Rh,Tx,Ch,wh,Ex):(Ah(),Rh(),Ch())}function Ex(t){if(je!==0){var n=Ri.onRecoverableError;n(t,{componentStack:null})}}function Tx(){je===3&&(je=0,Lg(Ns,Ri),je=4)}function Ah(){if(je===1){je=0;var t=Ri,n=Ns,a=qi,s=(n.flags&13878)!==0;if((n.subtreeFlags&13878)!==0||s){s=Mt.T,Mt.T=null;var l=bt.p;bt.p=2;var c=Ce;Ce|=4;try{Ho=gu=!1,Ug(n,t,a),a=Gh;var m=Cm(t.containerInfo),b=a.focusedElem,z=a.selectionRange;if(m!==b&&b&&b.ownerDocument&&Rm(b.ownerDocument.documentElement,b)){if(z!==null&&tf(b)){var W=z.start,et=z.end;if(et===void 0&&(et=W),"selectionStart"in b)b.selectionStart=W,b.selectionEnd=Math.min(et,b.value.length);else{var ct=b.ownerDocument||document,G=ct&&ct.defaultView||window;if(G.getSelection){var $=G.getSelection(),At=b.textContent.length,Vt=Math.min(z.start,At),re=z.end===void 0?Vt:Math.min(z.end,At);!$.extend&&Vt>re&&(m=re,re=Vt,Vt=m);var q=Am(b,Vt),I=Am(b,re);if(q&&I&&($.rangeCount!==1||$.anchorNode!==q.node||$.anchorOffset!==q.offset||$.focusNode!==I.node||$.focusOffset!==I.offset)){var K=ct.createRange();K.setStart(q.node,q.offset),$.removeAllRanges(),Vt>re?($.addRange(K),$.extend(I.node,I.offset)):(K.setEnd(I.node,I.offset),$.addRange(K))}}}}for(ct=[],$=b;$=$.parentNode;)$.nodeType===1&&ct.push({element:$,left:$.scrollLeft,top:$.scrollTop});for(typeof b.focus=="function"&&b.focus(),b=0;b<ct.length;b++){var ut=ct[b];ut.element.scrollLeft=ut.left,ut.element.scrollTop=ut.top}}Pr=!!Hh,Gh=Hh=null}finally{Ce=c,bt.p=l,Mt.T=s}}t.current=n,je=2}}function Rh(){if(je===2){je=0;var t=Ri,n=Ns,a=(n.flags&8772)!==0;if((n.subtreeFlags&8772)!==0||a){a=Mt.T,Mt.T=null;var s=bt.p;bt.p=2;var l=Ce;Ce|=4;try{bg(t,n.alternate,n)}finally{Ce=l,bt.p=s,Mt.T=a}}je=3}}function Ch(){if(je===4||je===3){je=0;var t=Mr;Mr=null,Y();var n=Ri,a=Ns,s=qi,l=Hg,c=(s&335544064)===s?10262:10256;if((a.subtreeFlags&c)!==0||(a.flags&c)!==0?je=5:(je=0,Ns=Ri=null,Jg(n,n.pendingLanes)),c=n.pendingLanes,c===0&&(Xa=null),Gt(s),a=a.stateNode,qe&&typeof qe.onCommitFiberRoot=="function")try{qe.onCommitFiberRoot(tn,a,void 0,(a.current.flags&128)===128)}catch{}if(l!==null){a=Mt.T,c=bt.p,bt.p=2,Mt.T=null;try{for(var m=n.onRecoverableError,b=0;b<l.length;b++){var z=l[b];m(z.value,{componentStack:z.stack})}}finally{Mt.T=a,bt.p=c}}if(l=Er,m=Tr,Tr=null,l!==null&&(Er=null,m===null&&(m=[]),t!==null))for(z=0;z<l.length;z++)a=(0,l[z])(m),a!==void 0&&t.finished.finally(a);(qi&3)!==0&&wu(),Wi(n),c=n.pendingLanes,(s&261930)!==0&&(c&42)!==0?n===bu?Yo++:(Yo=0,bu=n):(Yo=0,bu=null),ko(0)}}function Jg(t,n){(t.pooledCacheLanes&=n)===0&&(n=t.pooledCache,n!=null&&(t.pooledCache=null,bo(n)))}function wu(){return Mr!==null&&(Mr.skipTransition(),Mr=null),Ah(),Rh(),Ch(),wh()}function wh(){if(je!==5)return!1;var t=Ri,n=Mh;Mh=0;var a=Gt(qi),s=Mt.T,l=bt.p;try{bt.p=32>a?32:a,Mt.T=null,a=Eh,Eh=null;var c=Ri,m=qi;if(je=0,Ns=Ri=null,qi=0,(Ce&6)!==0)throw Error(r(331));var b=Ce;if(Ce|=4,Ig(c.current),Og(c,c.current,m,a),Ce=b,ko(0,!1),qe&&typeof qe.onPostCommitFiberRoot=="function")try{qe.onPostCommitFiberRoot(tn,c)}catch{}return!0}finally{bt.p=l,Mt.T=s,Jg(t,n)}}function $g(t,n,a){n=fi(a,n),n=qf(t.stateNode,n,2),t=Pa(t,n,2),t!==null&&(k(t,2),Wi(t))}function Ne(t,n,a){if(t.tag===3)$g(t,t,a);else for(;n!==null;){if(n.tag===3){$g(n,t,a);break}else if(n.tag===1){var s=n.stateNode;if(typeof n.type.getDerivedStateFromError=="function"||typeof s.componentDidCatch=="function"&&(Xa===null||!Xa.has(s))){t=fi(a,t),a=Z_(2),s=Pa(n,a,2),s!==null&&(K_(a,s,n,t),k(s,2),Wi(s));break}}n=n.return}}function Dh(t,n,a){var s=t.pingCache;if(s===null){s=t.pingCache=new gx;var l=new Set;s.set(n,l)}else l=s.get(n),l===void 0&&(l=new Set,s.set(n,l));l.has(a)||(yh=!0,l.add(a),t=bx.bind(null,t,n,a),n.then(t,t))}function bx(t,n,a){var s=t.pingCache;s!==null&&s.delete(n),t.pingedLanes|=t.suspendedLanes&a,t.warmLanes&=~a,Fe===t&&(ve&a)===a&&((Qe===4||Qe===3&&(ve&62914560)===ve&&300>Tt()-Mu)&&(Ce&2)===0?Ar(t,0):xu|=a,xr===ve&&(xr=0)),Wi(t)}function t0(t,n){n===0&&(n=El()),t=_s(t,n),t!==null&&(k(t,n),Wi(t))}function Ax(t){var n=t.memoizedState,a=0;n!==null&&(a=n.retryLane),t0(t,a)}function Rx(t,n){var a=0;switch(t.tag){case 31:case 13:var s=t.stateNode,l=t.memoizedState;l!==null&&(a=l.retryLane);break;case 19:s=t.stateNode;break;case 22:s=t.stateNode._retryCache;break;default:throw Error(r(314))}s!==null&&s.delete(n),t0(t,a)}function Cx(t,n){return pe(t,n)}var Cr=null,wr=null,Uh=!1,Du=!1,Nh=!1,ka=0;function Wi(t){t!==wr&&t.next===null&&(wr===null?Cr=wr=t:wr=wr.next=t),Du=!0,Uh||(Uh=!0,Dx())}function ko(t,n){if(!Nh&&Du){Nh=!0;do for(var a=!1,s=Cr;s!==null;){if(t!==0){var l=s.pendingLanes;if(l===0)var c=0;else{var m=s.suspendedLanes,b=s.pingedLanes;c=(1<<31-Rn(42|t)+1)-1,c&=l&~(m&~b),c=c&201326741?c&201326741|1:c?c|2:0}c!==0&&(a=!0,a0(s,c))}else c=ve,c=ds(s,s===Fe?c:0,s.cancelPendingCommit!==null||s.timeoutHandle!==-1),(c&3)===0||ba(s,c)||(a=!0,a0(s,c));s=s.next}while(a);Nh=!1}}function wx(){e0()}function e0(){Du=Uh=!1;var t=0;ka!==0&&Gx()&&(t=ka);for(var n=Tt(),a=null,s=Cr;s!==null;){var l=s.next,c=n0(s,n);c===0?(s.next=null,a===null?Cr=l:a.next=l,l===null&&(wr=a)):(a=s,(t!==0||(c&3)!==0)&&(Du=!0)),s=l}je!==0&&je!==5||ko(t),ka!==0&&(ka=0)}function n0(t,n){for(var a=t.suspendedLanes,s=t.pingedLanes,l=t.expirationTimes,c=t.pendingLanes&-62914561;0<c;){var m=31-Rn(c),b=1<<m,z=l[m];z===-1?((b&a)===0||(b&s)!==0)&&(l[m]=zc(b,n)):z<=n&&(t.expiredLanes|=b),c&=~b}if(n=Fe,a=ve,a=ds(t,t===n?a:0,t.cancelPendingCommit!==null||t.timeoutHandle!==-1),s=t.callbackNode,a===0||t===n&&(Ue===2||Ue===9)||t.cancelPendingCommit!==null)return s!==null&&s!==null&&ee(s),t.callbackNode=null,t.callbackPriority=0;if((a&3)===0||ba(t,a)){if(n=a&-a,n===t.callbackPriority)return n;switch(s!==null&&ee(s),Gt(a)){case 2:case 8:a=Lt;break;case 32:a=Ot;break;case 268435456:a=ke;break;default:a=Ot}return s=i0.bind(null,t),a=pe(a,s),t.callbackPriority=n,t.callbackNode=a,n}return s!==null&&s!==null&&ee(s),t.callbackPriority=2,t.callbackNode=null,2}function i0(t,n){if(je!==0&&je!==5)return t.callbackNode=null,t.callbackPriority=0,null;var a=t.callbackNode;if(wu()&&t.callbackNode!==a)return null;var s=ve;return s=ds(t,t===Fe?s:0,t.cancelPendingCommit!==null||t.timeoutHandle!==-1),s===0?null:(Vg(t,s,n),n0(t,Tt()),t.callbackNode!=null&&t.callbackNode===a?i0.bind(null,t):null)}function a0(t,n){if(wu())return null;Vg(t,n,!0)}function Dx(){Xx(function(){(Ce&6)!==0?pe(_t,wx):e0()})}function Lh(){if(ka===0){var t=Ms;t===0&&(t=fs,fs<<=1,(fs&261888)===0&&(fs=256)),ka=t}return ka}function s0(t){return t==null||typeof t=="symbol"||typeof t=="boolean"?null:typeof t=="function"?t:Al(t)}function Ux(t,n,a,s,l){if(n==="submit"&&a&&a.stateNode===l){var c=s0((l[ie]||null).action),m=s.submitter;m&&(n=(n=m[ie]||null)?s0(n.formAction):m.getAttribute("formAction"),n!==null&&(c=n,m=null));var b=new Dl("action","action",null,s,l);t.push({event:b,listeners:[{instance:null,listener:function(){if(s.defaultPrevented){if(ka!==0){var z=new FormData(l,m);Gf(a,{pending:!0,data:z,method:l.method,action:c},null,z)}}else typeof c=="function"&&(b.preventDefault(),z=new FormData(l,m),Gf(a,{pending:!0,data:z,method:l.method,action:c},c,z))},currentTarget:l}]})}}for(var Oh=0;Oh<sf.length;Oh++){var Ph=sf[Oh],Nx=Ph.toLowerCase(),Lx=Ph[0].toUpperCase()+Ph.slice(1);Ei(Nx,"on"+Lx)}Ei(Um,"onAnimationEnd"),Ei(Nm,"onAnimationIteration"),Ei(Lm,"onAnimationStart"),Ei("dblclick","onDoubleClick"),Ei("focusin","onFocus"),Ei("focusout","onBlur"),Ei(Vy,"onTransitionRun"),Ei(Xy,"onTransitionStart"),Ei(Yy,"onTransitionCancel"),Ei(Om,"onTransitionEnd"),ta("onMouseEnter",["mouseout","mouseover"]),ta("onMouseLeave",["mouseout","mouseover"]),ta("onPointerEnter",["pointerout","pointerover"]),ta("onPointerLeave",["pointerout","pointerover"]),$i("onChange","change click focusin focusout input keydown keyup selectionchange".split(" ")),$i("onSelect","focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" ")),$i("onBeforeInput",["compositionend","keypress","textInput","paste"]),$i("onCompositionEnd","compositionend focusout keydown keypress keyup mousedown".split(" ")),$i("onCompositionStart","compositionstart focusout keydown keypress keyup mousedown".split(" ")),$i("onCompositionUpdate","compositionupdate focusout keydown keypress keyup mousedown".split(" "));var qo="abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" "),Ox=new Set("beforetoggle cancel close invalid load scroll scrollend toggle".split(" ").concat(qo));function r0(t,n){n=(n&4)!==0;for(var a=0;a<t.length;a++){var s=t[a],l=s.event;s=s.listeners;t:{var c=void 0;if(n)for(var m=s.length-1;0<=m;m--){var b=s[m],z=b.instance,W=b.currentTarget;if(b=b.listener,z!==c&&l.isPropagationStopped())break t;c=b,l.currentTarget=W;try{c(l)}catch(et){Ll(et)}l.currentTarget=null,c=z}else for(m=0;m<s.length;m++){if(b=s[m],z=b.instance,W=b.currentTarget,b=b.listener,z!==c&&l.isPropagationStopped())break t;c=b,l.currentTarget=W;try{c(l)}catch(et){Ll(et)}l.currentTarget=null,c=z}}}}function ge(t,n){var a=n[Ve];a===void 0&&(a=n[Ve]=new Set);var s=t+"__bubble";a.has(s)||(o0(n,t,2,!1),a.add(s))}function zh(t,n,a){var s=0;n&&(s|=4),o0(a,t,s,n)}var Uu="_reactListening"+Math.random().toString(36).slice(2);function Ih(t){if(!t[Uu]){t[Uu]=!0,Ln.forEach(function(a){a!=="selectionchange"&&(Ox.has(a)||zh(a,!1,t),zh(a,!0,t))});var n=t.nodeType===9?t:t.ownerDocument;n===null||n[Uu]||(n[Uu]=!0,zh("selectionchange",!1,n))}}function o0(t,n,a,s){switch(K0(n)){case 2:var l=AM;break;case 8:l=RM;break;default:l=id}a=l.bind(null,n,a,t),l=void 0,!Yc||n!=="touchstart"&&n!=="touchmove"&&n!=="wheel"||(l=!0),s?l!==void 0?t.addEventListener(n,a,{capture:!0,passive:l}):t.addEventListener(n,a,!0):l!==void 0?t.addEventListener(n,a,{passive:l}):t.addEventListener(n,a,!1)}function Bh(t,n,a,s,l){var c=s;if((n&1)===0&&(n&2)===0&&s!==null)t:for(;;){if(s===null)return;var m=s.tag;if(m===3||m===4){var b=s.stateNode.containerInfo;if(b===l)break;if(m===4)for(m=s.return;m!==null;){var z=m.tag;if((z===3||z===4)&&m.stateNode.containerInfo===l)return;m=m.return}for(;b!==null;){if(m=Hn(b),m===null)return;if(z=m.tag,z===5||z===6||z===26||z===27){s=c=m;continue t}b=b.parentNode}}s=s.return}om(function(){var W=c,et=Vc(a),ct=[];t:{var G=Pm.get(t);if(G!==void 0){var $=Dl,At=t;switch(t){case"keypress":if(Cl(a)===0)break t;case"keydown":case"keyup":$=vy;break;case"focusin":At="focus",$=jc;break;case"focusout":At="blur",$=jc;break;case"beforeblur":case"afterblur":$=jc;break;case"click":if(a.button===2)break t;case"auxclick":case"dblclick":case"mousedown":case"mousemove":case"mouseup":case"mouseout":case"mouseover":case"contextmenu":$=cm;break;case"drag":case"dragend":case"dragenter":case"dragexit":case"dragleave":case"dragover":case"dragstart":case"drop":$=ry;break;case"touchcancel":case"touchend":case"touchmove":case"touchstart":$=Ey;break;case Um:case Nm:case Lm:$=uy;break;case Om:$=by;break;case"scroll":case"scrollend":$=ay;break;case"wheel":$=Ry;break;case"copy":case"cut":case"paste":$=fy;break;case"gotpointercapture":case"lostpointercapture":case"pointercancel":case"pointerdown":case"pointermove":case"pointerout":case"pointerover":case"pointerup":$=hm;break;case"submit":$=xy;break;case"toggle":case"beforetoggle":$=wy}var Vt=(n&4)!==0,re=!Vt&&(t==="scroll"||t==="scrollend"),q=Vt?G!==null?G+"Capture":null:G;Vt=[];for(var I=W,K;I!==null;){var ut=I;if(K=ut.stateNode,ut=ut.tag,ut!==5&&ut!==26&&ut!==27||K===null||q===null||(ut=po(I,q),ut!=null&&Vt.push(Wo(I,ut,K))),re)break;I=I.return}0<Vt.length&&(G=new $(G,At,null,a,et),ct.push({event:G,listeners:Vt}))}}if((n&7)===0){t:{if($=t==="mouseover"||t==="pointerover",G=t==="mouseout"||t==="pointerout",$&&a!==Gc&&(At=a.relatedTarget||a.fromElement)&&(Hn(At)||At[be]))break t;(G||$)&&(At=et.window===et?et:($=et.ownerDocument)?$.defaultView||$.parentWindow:window,G?($=a.relatedTarget||a.toElement,G=W,$=$?Hn($):null,$!==null&&(re=f($),Vt=$.tag,$!==re||Vt!==5&&Vt!==27&&Vt!==6)&&($=null)):(G=null,$=W),G!==$&&(Vt=cm,ut="onMouseLeave",q="onMouseEnter",I="mouse",(t==="pointerout"||t==="pointerover")&&(Vt=hm,ut="onPointerLeave",q="onPointerEnter",I="pointer"),re=G==null?At:Ji(G),K=$==null?At:Ji($),At=new Vt(ut,I+"leave",G,a,et),At.target=re,At.relatedTarget=K,ut=null,Hn(et)===W&&(Vt=new Vt(q,I+"enter",$,a,et),Vt.target=K,Vt.relatedTarget=re,ut=Vt),re=ut,Vt=G&&$?B(G,$,Px):null,G!==null&&l0(ct,At,G,Vt,!1),$!==null&&re!==null&&l0(ct,re,$,Vt,!0)))}t:{if(G=W?Ji(W):window,$=G.nodeName&&G.nodeName.toLowerCase(),$==="select"||$==="input"&&G.type==="file")var zt=ym;else if(vm(G))if(xm)zt=Fy;else{zt=Iy;var Se=zy}else $=G.nodeName,!$||$.toLowerCase()!=="input"||G.type!=="checkbox"&&G.type!=="radio"?W&&Hc(W.elementType)&&(zt=ym):zt=By;if(zt&&(zt=zt(t,W))){Sm(ct,zt,a,et);break t}Se&&Se(t,G,W)}switch(Se=W?Ji(W):window,t){case"focusin":(vm(Se)||Se.contentEditable==="true")&&(ir=Se,ef=W,Mo=null);break;case"focusout":Mo=ef=ir=null;break;case"mousedown":nf=!0;break;case"contextmenu":case"mouseup":case"dragend":nf=!1,wm(ct,a,et);break;case"selectionchange":if(Gy)break;case"keydown":case"keyup":wm(ct,a,et)}var Wt;if(Kc)t:{switch(t){case"compositionstart":var Jt="onCompositionStart";break t;case"compositionend":Jt="onCompositionEnd";break t;case"compositionupdate":Jt="onCompositionUpdate";break t}Jt=void 0}else nr?_m(t,a)&&(Jt="onCompositionEnd"):t==="keydown"&&a.keyCode===229&&(Jt="onCompositionStart");Jt&&(dm&&a.locale!=="ko"&&(nr||Jt!=="onCompositionStart"?Jt==="onCompositionEnd"&&nr&&(Wt=lm()):(Aa=et,kc="value"in Aa?Aa.value:Aa.textContent,nr=!0)),Se=Nu(W,Jt),0<Se.length&&(Jt=new fm(Jt,t,null,a,et),ct.push({event:Jt,listeners:Se}),Wt?Jt.data=Wt:(Wt=gm(a),Wt!==null&&(Jt.data=Wt)))),(Wt=Uy?Ny(t,a):Ly(t,a))&&(Jt=Nu(W,"onBeforeInput"),0<Jt.length&&(Se=new fm("onBeforeInput","beforeinput",null,a,et),ct.push({event:Se,listeners:Jt}),Se.data=Wt)),Ux(ct,t,W,a,et)}r0(ct,n)})}function Wo(t,n,a){return{instance:t,listener:n,currentTarget:a}}function Nu(t,n){for(var a=n+"Capture",s=[];t!==null;){var l=t,c=l.stateNode;if(l=l.tag,l!==5&&l!==26&&l!==27||c===null||(l=po(t,a),l!=null&&s.unshift(Wo(t,l,c)),l=po(t,n),l!=null&&s.push(Wo(t,l,c))),t.tag===3)return s;t=t.return}return[]}function Px(t){if(t===null)return null;do t=t.return;while(t&&t.tag!==5&&t.tag!==27);return t||null}function l0(t,n,a,s,l){for(var c=n._reactName,m=[];a!==null&&a!==s;){var b=a,z=b.alternate,W=b.stateNode;if(b=b.tag,z!==null&&z===s)break;b!==5&&b!==26&&b!==27||W===null||(z=W,l?(W=po(a,c),W!=null&&m.unshift(Wo(a,W,z))):l||(W=po(a,c),W!=null&&m.push(Wo(a,W,z)))),a=a.return}m.length!==0&&t.push({event:n,listeners:m})}var zx=/\r\n?/g,Ix=/\u0000|\uFFFD/g;function u0(t){return(typeof t=="string"?t:""+t).replace(zx,`
`).replace(Ix,"")}function c0(t,n){return n=u0(n),u0(t)===n}function Le(t,n,a,s,l,c){switch(a){case"children":if(typeof s=="string")n==="body"||n==="textarea"&&s===""||$s(t,s);else if(typeof s=="number"||typeof s=="bigint")n!=="body"&&$s(t,""+s);else return;break;case"className":bl(t,"class",s);break;case"tabIndex":bl(t,"tabindex",s);break;case"dir":case"role":case"viewBox":case"width":case"height":bl(t,a,s);break;case"style":sm(t,s,c);return;case"data":if(n!=="object"){bl(t,"data",s);break}case"src":case"href":if(s===""&&(n!=="a"||a!=="href")){t.removeAttribute(a);break}if(s==null||typeof s=="function"||typeof s=="symbol"||typeof s=="boolean"){t.removeAttribute(a);break}s=Al(s),t.setAttribute(a,s);break;case"action":case"formAction":if(typeof s=="function"){t.setAttribute(a,"javascript:throw new Error('A React form was unexpectedly submitted. If you called form.submit() manually, consider using form.requestSubmit() instead. If you\\'re trying to use event.stopPropagation() in a submit event handler, consider also calling event.preventDefault().')");break}else typeof c=="function"&&(a==="formAction"?(n!=="input"&&Le(t,n,"name",l.name,l,null),Le(t,n,"formEncType",l.formEncType,l,null),Le(t,n,"formMethod",l.formMethod,l,null),Le(t,n,"formTarget",l.formTarget,l,null)):(Le(t,n,"encType",l.encType,l,null),Le(t,n,"method",l.method,l,null),Le(t,n,"target",l.target,l,null)));if(s==null||typeof s=="symbol"||typeof s=="boolean"){t.removeAttribute(a);break}s=Al(s),t.setAttribute(a,s);break;case"onClick":s!=null&&(t.onclick=Ii);return;case"onScroll":s!=null&&ge("scroll",t);return;case"onScrollEnd":s!=null&&ge("scrollend",t);return;case"dangerouslySetInnerHTML":if(s!=null){if(typeof s!="object"||!("__html"in s))throw Error(r(61));if(a=s.__html,a!=null){if(l.children!=null)throw Error(r(60));c?.__html!==a&&(t.innerHTML=a)}}break;case"multiple":t.multiple=s&&typeof s!="function"&&typeof s!="symbol";break;case"muted":t.muted=s&&typeof s!="function"&&typeof s!="symbol";break;case"suppressContentEditableWarning":case"suppressHydrationWarning":case"defaultValue":case"defaultChecked":case"innerHTML":case"ref":break;case"autoFocus":break;case"xlinkHref":if(s==null||typeof s=="function"||typeof s=="boolean"||typeof s=="symbol"){t.removeAttribute("xlink:href");break}a=Al(s),t.setAttributeNS("http://www.w3.org/1999/xlink","xlink:href",a);break;case"contentEditable":case"spellCheck":case"draggable":case"value":case"autoReverse":case"externalResourcesRequired":case"focusable":case"preserveAlpha":s!=null&&typeof s!="function"&&typeof s!="symbol"?t.setAttribute(a,s):t.removeAttribute(a);break;case"inert":case"allowFullScreen":case"async":case"autoPlay":case"controls":case"credentialless":case"default":case"defer":case"disabled":case"disablePictureInPicture":case"disableRemotePlayback":case"formNoValidate":case"hidden":case"loop":case"noModule":case"noValidate":case"open":case"playsInline":case"readOnly":case"required":case"reversed":case"scoped":case"seamless":case"itemScope":s&&typeof s!="function"&&typeof s!="symbol"?t.setAttribute(a,""):t.removeAttribute(a);break;case"capture":case"download":s===!0?t.setAttribute(a,""):s!==!1&&s!=null&&typeof s!="function"&&typeof s!="symbol"?t.setAttribute(a,s):t.removeAttribute(a);break;case"cols":case"rows":case"size":case"span":s!=null&&typeof s!="function"&&typeof s!="symbol"&&!isNaN(s)&&1<=s?t.setAttribute(a,s):t.removeAttribute(a);break;case"rowSpan":case"start":s==null||typeof s=="function"||typeof s=="symbol"||isNaN(s)?t.removeAttribute(a):t.setAttribute(a,s);break;case"popover":ge("beforetoggle",t),ge("toggle",t),Tl(t,"popover",s);break;case"xlinkActuate":ea(t,"http://www.w3.org/1999/xlink","xlink:actuate",s);break;case"xlinkArcrole":ea(t,"http://www.w3.org/1999/xlink","xlink:arcrole",s);break;case"xlinkRole":ea(t,"http://www.w3.org/1999/xlink","xlink:role",s);break;case"xlinkShow":ea(t,"http://www.w3.org/1999/xlink","xlink:show",s);break;case"xlinkTitle":ea(t,"http://www.w3.org/1999/xlink","xlink:title",s);break;case"xlinkType":ea(t,"http://www.w3.org/1999/xlink","xlink:type",s);break;case"xmlBase":ea(t,"http://www.w3.org/XML/1998/namespace","xml:base",s);break;case"xmlLang":ea(t,"http://www.w3.org/XML/1998/namespace","xml:lang",s);break;case"xmlSpace":ea(t,"http://www.w3.org/XML/1998/namespace","xml:space",s);break;case"is":Tl(t,"is",s);break;case"innerText":case"textContent":return;default:if(!(2<a.length)||a[0]!=="o"&&a[0]!=="O"||a[1]!=="n"&&a[1]!=="N")a=ny.get(a)||a,Tl(t,a,s);else return}Re=!0}function Fh(t,n,a,s,l,c){switch(a){case"style":sm(t,s,c);return;case"dangerouslySetInnerHTML":if(s!=null){if(typeof s!="object"||!("__html"in s))throw Error(r(61));if(a=s.__html,a!=null){if(l.children!=null)throw Error(r(60));c?.__html!==a&&(t.innerHTML=a)}}break;case"children":if(typeof s=="string")$s(t,s);else if(typeof s=="number"||typeof s=="bigint")$s(t,""+s);else return;break;case"onScroll":s!=null&&ge("scroll",t);return;case"onScrollEnd":s!=null&&ge("scrollend",t);return;case"onClick":s!=null&&(t.onclick=Ii);return;case"suppressContentEditableWarning":case"suppressHydrationWarning":case"innerHTML":case"ref":return;case"innerText":case"textContent":return;default:if(!Qs.hasOwnProperty(a))t:{if(a[0]==="o"&&a[1]==="n"&&(l=a.endsWith("Capture"),c=a.slice(2,l?a.length-7:void 0),n=t[ie]||null,n=n!=null?n[a]:null,typeof n=="function"&&t.removeEventListener(c,n,l),typeof s=="function")){typeof n!="function"&&n!==null&&(a in t?t[a]=null:t.hasAttribute(a)&&t.removeAttribute(a)),t.addEventListener(c,s,l);break t}Re=!0,a in t?t[a]=s:s===!0?t.setAttribute(a,""):Tl(t,a,s)}return}Re=!0}function En(t,n,a){switch(n){case"div":case"span":case"svg":case"path":case"a":case"g":case"p":case"li":break;case"img":ge("error",t),ge("load",t);var s=!1,l=!1,c;for(c in a)if(a.hasOwnProperty(c)){var m=a[c];if(m!=null)switch(c){case"src":s=!0;break;case"srcSet":l=!0;break;case"children":case"dangerouslySetInnerHTML":throw Error(r(137,n));default:Le(t,n,c,m,a,null)}}l&&Le(t,n,"srcSet",a.srcSet,a,null),s&&Le(t,n,"src",a.src,a,null);return;case"input":ge("invalid",t);var b=c=m=l=null,z=null,W=null;for(s in a)if(a.hasOwnProperty(s)){var et=a[s];if(et!=null)switch(s){case"name":l=et;break;case"type":m=et;break;case"checked":z=et;break;case"defaultChecked":W=et;break;case"value":c=et;break;case"defaultValue":b=et;break;case"children":case"dangerouslySetInnerHTML":if(et!=null)throw Error(r(137,n));break;default:Le(t,n,s,et,a,null)}}em(t,c,b,z,W,m,l,!1);return;case"select":ge("invalid",t),s=m=c=null;for(l in a)if(a.hasOwnProperty(l)&&(b=a[l],b!=null))switch(l){case"value":c=b;break;case"defaultValue":m=b;break;case"multiple":s=b;default:Le(t,n,l,b,a,null)}n=c,a=m,t.multiple=!!s,n!=null?Js(t,!!s,n,!1):a!=null&&Js(t,!!s,a,!0);return;case"textarea":ge("invalid",t),c=l=s=null;for(m in a)if(a.hasOwnProperty(m)&&(b=a[m],b!=null))switch(m){case"value":s=b;break;case"defaultValue":l=b;break;case"children":c=b;break;case"dangerouslySetInnerHTML":if(b!=null)throw Error(r(91));break;default:Le(t,n,m,b,a,null)}im(t,s,l,c);return;case"option":for(z in a)a.hasOwnProperty(z)&&(s=a[z],s!=null)&&(z==="selected"?t.selected=s&&typeof s!="function"&&typeof s!="symbol":Le(t,n,z,s,a,null));return;case"dialog":ge("beforetoggle",t),ge("toggle",t),ge("cancel",t),ge("close",t);break;case"iframe":case"object":ge("load",t);break;case"video":case"audio":for(s=0;s<qo.length;s++)ge(qo[s],t);break;case"image":ge("error",t),ge("load",t);break;case"details":ge("toggle",t);break;case"embed":case"source":case"link":ge("error",t),ge("load",t);case"area":case"base":case"br":case"col":case"hr":case"keygen":case"meta":case"param":case"track":case"wbr":case"menuitem":for(W in a)if(a.hasOwnProperty(W)&&(s=a[W],s!=null))switch(W){case"children":case"dangerouslySetInnerHTML":throw Error(r(137,n));default:Le(t,n,W,s,a,null)}return;default:if(Hc(n)){for(et in a)a.hasOwnProperty(et)&&(s=a[et],s!==void 0&&Fh(t,n,et,s,a,void 0));return}}for(b in a)a.hasOwnProperty(b)&&(s=a[b],s!=null&&Le(t,n,b,s,a,null))}var Bx={};function Fx(t,n,a,s){switch(n){case"div":case"span":case"svg":case"path":case"a":case"g":case"p":case"li":break;case"input":var l=null,c=null,m=null,b=null,z=null,W=null,et=null;for($ in a){var ct=a[$];if(a.hasOwnProperty($)&&ct!=null)switch($){case"checked":break;case"value":break;case"defaultValue":z=ct;default:s.hasOwnProperty($)||Le(t,n,$,null,s,ct)}}for(var G in s){var $=s[G];if(ct=a[G],s.hasOwnProperty(G)&&($!=null||ct!=null))switch(G){case"type":$!==ct&&(Re=!0),c=$;break;case"name":$!==ct&&(Re=!0),l=$;break;case"checked":$!==ct&&(Re=!0),W=$;break;case"defaultChecked":$!==ct&&(Re=!0),et=$;break;case"value":$!==ct&&(Re=!0),m=$;break;case"defaultValue":$!==ct&&(Re=!0),b=$;break;case"children":case"dangerouslySetInnerHTML":if($!=null)throw Error(r(137,n));break;default:$!==ct&&Le(t,n,G,$,s,ct)}}Bc(t,m,b,z,W,et,c,l);return;case"select":$=m=b=G=null;for(c in a)if(z=a[c],a.hasOwnProperty(c)&&z!=null)switch(c){case"value":break;case"multiple":$=z;default:s.hasOwnProperty(c)||Le(t,n,c,null,s,z)}for(l in s)if(c=s[l],z=a[l],s.hasOwnProperty(l)&&(c!=null||z!=null))switch(l){case"value":c!==z&&(Re=!0),G=c;break;case"defaultValue":c!==z&&(Re=!0),b=c;break;case"multiple":c!==z&&(Re=!0),m=c;default:c!==z&&Le(t,n,l,c,s,z)}n=b,a=m,s=$,G!=null?Js(t,!!a,G,!1):!!s!=!!a&&(n!=null?Js(t,!!a,n,!0):Js(t,!!a,a?[]:"",!1));return;case"textarea":$=G=null;for(b in a)if(l=a[b],a.hasOwnProperty(b)&&l!=null&&!s.hasOwnProperty(b))switch(b){case"value":break;case"children":break;default:Le(t,n,b,null,s,l)}for(m in s)if(l=s[m],c=a[m],s.hasOwnProperty(m)&&(l!=null||c!=null))switch(m){case"value":l!==c&&(Re=!0),G=l;break;case"defaultValue":l!==c&&(Re=!0),$=l;break;case"children":break;case"dangerouslySetInnerHTML":if(l!=null)throw Error(r(91));break;default:l!==c&&Le(t,n,m,l,s,c)}nm(t,G,$);return;case"option":for(var At in a)G=a[At],a.hasOwnProperty(At)&&G!=null&&!s.hasOwnProperty(At)&&(At==="selected"?t.selected=!1:Le(t,n,At,null,s,G));for(z in s)G=s[z],$=a[z],s.hasOwnProperty(z)&&G!==$&&(G!=null||$!=null)&&(z==="selected"?(G!==$&&(Re=!0),t.selected=G&&typeof G!="function"&&typeof G!="symbol"):Le(t,n,z,G,s,$));return;case"img":case"link":case"area":case"base":case"br":case"col":case"embed":case"hr":case"keygen":case"meta":case"param":case"source":case"track":case"wbr":case"menuitem":for(var Vt in a)G=a[Vt],a.hasOwnProperty(Vt)&&G!=null&&!s.hasOwnProperty(Vt)&&Le(t,n,Vt,null,s,G);for(W in s)if(G=s[W],$=a[W],s.hasOwnProperty(W)&&G!==$&&(G!=null||$!=null))switch(W){case"children":case"dangerouslySetInnerHTML":if(G!=null)throw Error(r(137,n));break;default:Le(t,n,W,G,s,$)}return;default:if(Hc(n)){for(var re in a)G=a[re],a.hasOwnProperty(re)&&G!==void 0&&!s.hasOwnProperty(re)&&Fh(t,n,re,void 0,s,G);for(et in s)G=s[et],$=a[et],!s.hasOwnProperty(et)||G===$||G===void 0&&$===void 0||Fh(t,n,et,G,s,$);return}}for(var q in a)G=a[q],a.hasOwnProperty(q)&&G!=null&&!s.hasOwnProperty(q)&&Le(t,n,q,null,s,G);for(ct in s)G=s[ct],$=a[ct],!s.hasOwnProperty(ct)||G===$||G==null&&$==null||Le(t,n,ct,G,s,$)}function f0(t){switch(t){case"css":case"script":case"font":case"img":case"image":case"input":case"link":return!0;default:return!1}}function Hx(){if(typeof performance.getEntriesByType=="function"){for(var t=0,n=0,a=performance.getEntriesByType("resource"),s=0;s<a.length;s++){var l=a[s],c=l.transferSize,m=l.initiatorType,b=l.duration;if(c&&b&&f0(m)){for(m=0,b=l.responseEnd,s+=1;s<a.length;s++){var z=a[s],W=z.startTime;if(W>b)break;var et=z.transferSize,ct=z.initiatorType;et&&f0(ct)&&(z=z.responseEnd,m+=et*(z<b?1:(b-W)/(z-W)))}if(--s,n+=8*(c+m)/(l.duration/1e3),t++,10<t)break}}if(0<t)return n/t/1e6}return navigator.connection&&(t=navigator.connection.downlink,typeof t=="number")?t:5}var Hh=null,Gh=null;function jo(t){return t.nodeType===9?t:t.ownerDocument}function h0(t){switch(t){case"http://www.w3.org/2000/svg":return 1;case"http://www.w3.org/1998/Math/MathML":return 2;default:return 0}}function d0(t,n){if(t===0)switch(n){case"svg":return 1;case"math":return 2;default:return 0}return t===1&&n==="foreignObject"?0:t}function p0(t,n,a,s){return a=jo(a).createElement(t),a[Ut]=s,a[ie]=n,En(a,t,n),Be(a),a}function Vh(t,n){return t==="textarea"||t==="noscript"||typeof n.children=="string"||typeof n.children=="number"||typeof n.children=="bigint"||typeof n.dangerouslySetInnerHTML=="object"&&n.dangerouslySetInnerHTML!==null&&n.dangerouslySetInnerHTML.__html!=null}var Xh=null;function Gx(){var t=window.event;return t&&t.type==="popstate"?t===Xh?!1:(Xh=t,!0):(Xh=null,!1)}var Yh=typeof setTimeout=="function"?setTimeout:void 0,Vx=typeof clearTimeout=="function"?clearTimeout:void 0,m0=typeof Promise=="function"?Promise:void 0,_0=typeof requestAnimationFrame=="function"?requestAnimationFrame:Yh,Xx=typeof queueMicrotask=="function"?queueMicrotask:typeof m0<"u"?function(t){return m0.resolve(null).then(t).catch(Yx)}:Yh;function Yx(t){setTimeout(function(){throw t})}function qa(t){return t==="head"}function g0(t,n){var a=n,s=0;do{var l=a.nextSibling;if(t.removeChild(a),l&&l.nodeType===8)if(a=l.data,a==="/$"||a==="/&"){if(s===0){t.removeChild(l),zr(n);return}s--}else if(a==="$"||a==="$?"||a==="$~"||a==="$!"||a==="&")s++;else if(a==="html")Jh(t.ownerDocument.documentElement);else if(a==="head"){a=t.ownerDocument.head,Jh(a);for(var c=a.firstChild;c;){var m=c.nextSibling,b=c.nodeName;c[We]||b==="SCRIPT"||b==="STYLE"||b==="LINK"&&c.rel.toLowerCase()==="stylesheet"||a.removeChild(c),c=m}}else a==="body"&&Jh(t.ownerDocument.body);a=l}while(a);zr(n)}function v0(t,n){var a=t;t=0;do{var s=a.nextSibling;if(a.nodeType===1?n?(a._stashedDisplay=a.style.display,a.style.display="none"):(a.style.display=a._stashedDisplay||"",a.getAttribute("style")===""&&a.removeAttribute("style")):a.nodeType===3&&(n?(a._stashedText=a.nodeValue,a.nodeValue=""):a.nodeValue=a._stashedText||""),s&&s.nodeType===8)if(a=s.data,a==="/$"){if(t===0)break;t--}else a!=="$"&&a!=="$?"&&a!=="$~"&&a!=="$!"||t++;a=s}while(a)}function S0(t,n,a){if(n=CSS.escape(n)!==n?"r-"+btoa(n).replace(/=/g,""):n,t.style.viewTransitionName=n,a!=null&&(t.style.viewTransitionClass=a),a=getComputedStyle(t),a.display==="inline"){if(n=t.getClientRects(),n.length===1)var s=1;else for(var l=s=0;l<n.length;l++){var c=n[l];0<c.width&&0<c.height&&s++}s===1&&(t=t.style,t.display=n.length===1?"inline-block":"block",t.marginTop="-"+a.paddingTop,t.marginBottom="-"+a.paddingBottom)}}function y0(t,n){t=t.style,n=n.style;var a=n!=null?n.hasOwnProperty("viewTransitionName")?n.viewTransitionName:n.hasOwnProperty("view-transition-name")?n["view-transition-name"]:null:null;t.viewTransitionName=a==null||typeof a=="boolean"?"":(""+a).trim(),a=n!=null?n.hasOwnProperty("viewTransitionClass")?n.viewTransitionClass:n.hasOwnProperty("view-transition-class")?n["view-transition-class"]:null:null,t.viewTransitionClass=a==null||typeof a=="boolean"?"":(""+a).trim(),t.display==="inline-block"&&(n==null?t.display=t.margin="":(a=n.display,t.display=a==null||typeof a=="boolean"?"":a,a=n.margin,a!=null?t.margin=a:(a=n.hasOwnProperty("marginTop")?n.marginTop:n["margin-top"],t.marginTop=a==null||typeof a=="boolean"?"":a,n=n.hasOwnProperty("marginBottom")?n.marginBottom:n["margin-bottom"],t.marginBottom=n==null||typeof n=="boolean"?"":n)))}function kx(t,n,a){return a=a.ownerDocument.defaultView,{rect:t,abs:n.position==="absolute"||n.position==="fixed",clip:n.clipPath!=="none"||n.overflow!=="visible"||n.filter!=="none"||n.mask!=="none"||n.mask!=="none"||n.borderRadius!=="0px",view:0<=t.bottom&&0<=t.right&&t.top<=a.innerHeight&&t.left<=a.innerWidth}}function kh(t){var n=t.getBoundingClientRect(),a=getComputedStyle(t);return kx(n,a,t)}function qx(t){return t.documentElement.clientHeight}function Wx(t){this.addEventListener("load",t),this.addEventListener("error",t)}function jx(t,n,a,s,l,c,m,b,z){var W=n.nodeType===9?n:n.ownerDocument;try{var et=W.startViewTransition({update:function(){var G=W.defaultView,$=G.navigation&&G.navigation.transition,At=W.fonts.status;s();var Vt=[];if(At==="loaded"&&(qx(W),W.fonts.status==="loading"&&Vt.push(W.fonts.ready)),At=Vt.length,t!==null)for(var re=t.suspenseyImages,q=0,I=0;I<re.length;I++){var K=re[I];if(!K.complete){var ut=K.getBoundingClientRect();if(0<ut.bottom&&0<ut.right&&ut.top<G.innerHeight&&ut.left<G.innerWidth){if(q+=G0(K),q>Pu){Vt.length=At;break}K=new Promise(Wx.bind(K)),Vt.push(K)}}}if(0<Vt.length)return G=Promise.race([Promise.all(Vt),new Promise(function(zt){return setTimeout(zt,500)})]).then(l,l),($?Promise.allSettled([$.finished,G]):G).then(c,c);if(l(),$)return $.finished.then(c,c);c()},types:a});W.__reactViewTransition=et;var ct=[];return et.ready.then(function(){for(var G=W.documentElement.getAnimations({subtree:!0}),$=0;$<G.length;$++){var At=G[$],Vt=At.effect,re=Vt.pseudoElement;if(re!=null&&re.startsWith("::view-transition")){ct.push(At),At=Vt.getKeyframes();for(var q=re=void 0,I=!0,K=0;K<At.length;K++){var ut=At[K],zt=ut.width;if(re===void 0)re=zt;else if(re!==zt){I=!1;break}if(zt=ut.height,q===void 0)q=zt;else if(q!==zt){I=!1;break}delete ut.width,delete ut.height,ut.transform==="none"&&delete ut.transform}I&&re!==void 0&&q!==void 0&&(Vt.setKeyframes(At),I=getComputedStyle(Vt.target,Vt.pseudoElement),I.width!==re||I.height!==q)&&(I=At[0],I.width=re,I.height=q,I=At[At.length-1],I.width=re,I.height=q,Vt.setKeyframes(At))}}m()},function(G){W.__reactViewTransition===et&&(W.__reactViewTransition=null);try{typeof G=="object"&&G!==null&&G.name==="InvalidStateError"&&(G.message==="View transition was skipped because document visibility state is hidden."||G.message==="Skipping view transition because document visibility state has become hidden."||G.message==="Skipping view transition because viewport size changed."||G.message==="Transition was aborted because of invalid state")&&(G=null),G!==null&&z(G)}finally{s(),l(),m()}}),et.finished.finally(function(){for(var G=0;G<ct.length;G++)ct[G].cancel();W.__reactViewTransition===et&&(W.__reactViewTransition=null),b()}),et}catch{return s(),l(),m(),null}}function Ls(t,n){this._scope=document.documentElement,this._selector="::view-transition-"+t+"("+n+")"}Ls.prototype.animate=function(t,n){return n=typeof n=="number"?{duration:n}:O({},n),n.pseudoElement=this._selector,this._scope.animate(t,n)},Ls.prototype.getAnimations=function(){for(var t=this._scope,n=this._selector,a=t.getAnimations({subtree:!0}),s=[],l=0;l<a.length;l++){var c=a[l].effect;c!==null&&c.target===t&&c.pseudoElement===n&&s.push(a[l])}return s},Ls.prototype.getComputedStyle=function(){return getComputedStyle(this._scope,this._selector)};function x0(t){return{name:t,group:new Ls("group",t),imagePair:new Ls("image-pair",t),old:new Ls("old",t),new:new Ls("new",t)}}function si(t){this._fragmentFiber=t,this._observers=this._eventListeners=null}si.prototype.addEventListener=function(t,n,a){var s=null,l=null;if(!(a!=null&&typeof a!="boolean"&&(s=a.signal||null,s!==null&&s.aborted))){this._eventListeners===null&&(this._eventListeners=[]);var c=this._eventListeners;if(E0(c,t,n,a)===-1){var m=this,b=n;a!=null&&typeof a!="boolean"&&a.once===!0&&(b=function(z){m.removeEventListener(t,n,a),typeof n=="function"?n.call(this,z):n.handleEvent(z)}),s!==null&&(l=m.removeEventListener.bind(m,t,n,a),s.addEventListener("abort",l,{once:!0}),l=s.removeEventListener.bind(s,"abort",l)),s=Dr(a),c.push({type:t,listener:n,optionsOrUseCapture:a,attachedListener:b,cleanup:l}),_(this._fragmentFiber.child,!1,Zx,t,b,s)}this._eventListeners=c}};function Zx(t,n,a,s){return x(t).addEventListener(n,a,s),!1}si.prototype.removeEventListener=function(t,n,a){var s=this._eventListeners;if(s!==null&&(n=E0(s,t,n,a),n!==-1)){var l=s[n];a=l.attachedListener;var c=l.cleanup;l=Dr(l.optionsOrUseCapture),_(this._fragmentFiber.child,!1,Kx,t,a,l),s.splice(n,1),c!==null&&c()}};function Kx(t,n,a,s){return x(t).removeEventListener(n,a,s),!1}function Dr(t){return t!=null&&typeof t!="boolean"&&(t.once===!0||t.signal instanceof AbortSignal)?{capture:t.capture,passive:t.passive}:t}function M0(t){return t==null?"c=0":typeof t=="boolean"?"c="+(t?"1":"0"):"c="+(t.capture?"1":"0")}function E0(t,n,a,s){if(t.length===0)return-1;s=M0(s);for(var l=0;l<t.length;l++){var c=t[l];if(c.type===n&&c.listener===a&&M0(c.optionsOrUseCapture)===s)return l}return-1}si.prototype.dispatchEvent=function(t){var n=y(this._fragmentFiber);if(n===null)return!0;n=x(n);var a=this._eventListeners;if(a!==null&&0<a.length||!t.bubbles){var s=n.nodeType===9?n.createComment(""):document.createTextNode("");if(a)for(var l=0;l<a.length;l++){var c=a[l];s.addEventListener(c.type,c.attachedListener,Dr(c.optionsOrUseCapture))}if(n.appendChild(s),t=s.dispatchEvent(t),a)for(l=0;l<a.length;l++)c=a[l],s.removeEventListener(c.type,c.attachedListener,Dr(c.optionsOrUseCapture));return n.removeChild(s),t}return n.dispatchEvent(t)},si.prototype.focus=function(t){_(this._fragmentFiber.child,!0,T0,t,void 0,void 0)};function T0(t,n){return t.tag===6?!1:(t=x(t),lM(t,n))}si.prototype.focusLast=function(t){var n=[];_(this._fragmentFiber.child,!0,qh,n,void 0,void 0);for(var a=n.length-1;0<=a&&!T0(n[a],t);a--);};function qh(t,n){return n.push(t),!1}si.prototype.blur=function(){var t=y(this._fragmentFiber);t!==null&&(t=x(t),t=jo(t).activeElement,t!==null&&_(this._fragmentFiber.child,!1,Qx,t,void 0,void 0))};function Qx(t,n){return t.tag===6?!1:(t=x(t),t===n||t.contains(n)?(n.blur(),!0):!1)}si.prototype.observeUsing=function(t){this._observers===null&&(this._observers=new Set),this._observers.add(t),_(this._fragmentFiber.child,!1,Jx,t,void 0,void 0)};function Jx(t,n){return t.tag===6||(t=x(t),n.observe(t)),!1}si.prototype.unobserveUsing=function(t){var n=this._observers;if(n!==null&&n.has(t)){n.delete(t),_(this._fragmentFiber.child,!1,$x,t,void 0,void 0);for(var a=n=0;a<Ci.length;a++){var s=Ci[a];s.fragmentInstance===this&&s.observer===t?t.unobserve(s.instance):Ci[n++]=s}Ci.length=n}};function $x(t,n){return t.tag===6||(t=x(t),n.unobserve(t)),!1}var Ci=[],Wh=!1;function tM(t,n,a){Ci.push({fragmentInstance:t,observer:n,instance:a}),Wh||(Wh=!0,uM(function(){Wh=!1;var s=Ci;Ci=[];for(var l=0;l<s.length;l++){var c=s[l];c.observer.unobserve(c.instance)}}))}si.prototype.getClientRects=function(){var t=[];return _(this._fragmentFiber.child,!1,eM,t,void 0,void 0),t};function eM(t,n){if(t.tag===6){t=t.stateNode;var a=t.ownerDocument.createRange();a.selectNodeContents(t),n.push.apply(n,a.getClientRects())}else t=x(t),n.push.apply(n,t.getClientRects());return!1}si.prototype.getRootNode=function(t){var n=y(this._fragmentFiber);return n===null?this:x(n).getRootNode(t)},si.prototype.compareDocumentPosition=function(t){var n=y(this._fragmentFiber);if(n===null)return Node.DOCUMENT_POSITION_DISCONNECTED;var a=[];_(this._fragmentFiber.child,!1,qh,a,void 0,void 0);var s=x(n);if(a.length===0){if(a=s,M(this._fragmentFiber)){t:{for(n=this._fragmentFiber.return;n!==null;){if(n.tag===4){n=n.stateNode.containerInfo;break t}if(n.tag===3||n.tag===5||n.tag===27)break;n=n.return}n=null}n!=null&&(a=n)}n=this._fragmentFiber;var l=s=a.compareDocumentPosition(t);return a===t?l=Node.DOCUMENT_POSITION_CONTAINS:s&Node.DOCUMENT_POSITION_CONTAINED_BY&&(a=E(n)[1],a===null?l=Node.DOCUMENT_POSITION_PRECEDING:(t=x(a).compareDocumentPosition(t),l=t===0||t&Node.DOCUMENT_POSITION_FOLLOWING?Node.DOCUMENT_POSITION_FOLLOWING:Node.DOCUMENT_POSITION_PRECEDING)),l|=Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC}n=x(a[0]),l=x(a[a.length-1]);var c=M(this._fragmentFiber)?n.parentElement:s;if(c==null)return Node.DOCUMENT_POSITION_DISCONNECTED;s=c.compareDocumentPosition(n)&Node.DOCUMENT_POSITION_CONTAINED_BY,c=c.compareDocumentPosition(l)&Node.DOCUMENT_POSITION_CONTAINED_BY;var m=n.compareDocumentPosition(t),b=l.compareDocumentPosition(t),z=m&Node.DOCUMENT_POSITION_CONTAINED_BY||b&Node.DOCUMENT_POSITION_CONTAINED_BY;return b=s&&c&&m&Node.DOCUMENT_POSITION_FOLLOWING&&b&Node.DOCUMENT_POSITION_PRECEDING,n=s&&n===t||c&&l===t||z||b?Node.DOCUMENT_POSITION_CONTAINED_BY:!s&&n===t||!c&&l===t?Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC:m,n&Node.DOCUMENT_POSITION_DISCONNECTED||n&Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC||nM(n,this._fragmentFiber,a[0],a[a.length-1],t)?n:Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC};function nM(t,n,a,s,l){var c=Hn(l);if(t&Node.DOCUMENT_POSITION_CONTAINED_BY){if(a=!!c)t:{for(;c!==null;){if(c.tag===7&&(c===n||c.alternate===n)){a=!0;break t}c=c.return}a=!1}return a}if(t&Node.DOCUMENT_POSITION_CONTAINS){if(c===null)return c=l.ownerDocument,l===c||l===c.documentElement||l===c.body;t:{for(c=n,n=y(n);c!==null;){if(!(c.tag!==5&&c.tag!==3&&c.tag!==27||c!==n&&c.alternate!==n)){c=!0;break t}c=c.return}c=!1}return c}return t&Node.DOCUMENT_POSITION_PRECEDING?((n=!!c)&&!(n=c===a)&&(n=B(a,c,J),n===null?n=!1:(_(n,!0,U,c,a),c=S,S=null,n=c!==null)),n):t&Node.DOCUMENT_POSITION_FOLLOWING?((n=!!c)&&!(n=c===s)&&(n=B(s,c,J),n===null?n=!1:(_(n,!0,P,c,s),c=S,L=S=null,n=c!==null)),n):!1}function b0(t,n){var a=t.ownerDocument.createRange();a.selectNodeContents(t),t=a.getBoundingClientRect(),window.scrollTo(window.scrollX+t.left,n?window.scrollY+t.top:window.scrollY+t.bottom-window.innerHeight)}si.prototype.scrollIntoView=function(t){if(typeof t=="object")throw Error(r(566));var n=[];_(this._fragmentFiber.child,!1,qh,n,void 0,void 0);var a=t!==!1;if(n.length===0){var s=E(this._fragmentFiber);if(s=a?s[1]||s[0]||y(this._fragmentFiber):s[0]||s[1],s===null)return;if(s.tag===6){t=x(s),b0(t,a);return}if(s=x(s),s.nodeType!==9){if(s.nodeType===11){a="host"in s?s.host:null,a!==null&&a.scrollIntoView(t);return}s.scrollIntoView(t)}}for(s=a?n.length-1:0;s!==(a?-1:n.length);){var l=n[s];l.tag===6?(l=x(l),b0(l,a)):x(l).scrollIntoView(t),s+=a?-1:1}};function iM(t,n){return t=x(t),A0(t,n),!1}function A0(t,n){t.reactFragments==null&&(t.reactFragments=new Set),t.reactFragments.add(n)}function R0(t,n){var a=n._eventListeners;if(a!==null)for(var s=0;s<a.length;s++){var l=a[s];t.addEventListener(l.type,l.attachedListener,Dr(l.optionsOrUseCapture))}t.nodeType!==3&&(a=n._observers,a!==null&&a.forEach(function(c){for(var m=0,b=0;b<Ci.length;b++){var z=Ci[b];(z.fragmentInstance!==n||z.observer!==c||z.instance!==t)&&(Ci[m++]=z)}Ci.length=m,c.observe(t)}),A0(t,n))}function aM(t,n){var a=n._eventListeners;if(a!==null)for(var s=0;s<a.length;s++){var l=a[s];t.removeEventListener(l.type,l.attachedListener,Dr(l.optionsOrUseCapture))}t.nodeType!==3&&(a=n._observers,a!==null&&a.forEach(function(c){typeof c.rootMargin=="string"?tM(n,c,t):c.unobserve(t)}),t.reactFragments!=null&&t.reactFragments.delete(n))}function jh(t){var n=t.firstChild;for(n&&n.nodeType===10&&(n=n.nextSibling);n;){var a=n;switch(n=n.nextSibling,a.nodeName){case"HTML":case"HEAD":case"BODY":jh(a),Cn(a);continue;case"SCRIPT":case"STYLE":continue;case"LINK":if(a.rel.toLowerCase()==="stylesheet")continue}t.removeChild(a)}}function sM(t,n,a,s){for(;t.nodeType===1;){var l=a;if(t.nodeName.toLowerCase()!==n.toLowerCase()){if(!s&&(t.nodeName!=="INPUT"||t.type!=="hidden"))break}else if(s){if(!t[We])switch(n){case"meta":if(!t.hasAttribute("itemprop"))break;return t;case"link":if(c=t.getAttribute("rel"),c==="stylesheet"&&t.hasAttribute("data-precedence"))break;if(c!==l.rel||t.getAttribute("href")!==(l.href==null||l.href===""?null:l.href)||t.getAttribute("crossorigin")!==(l.crossOrigin==null?null:l.crossOrigin)||t.getAttribute("title")!==(l.title==null?null:l.title))break;return t;case"style":if(t.hasAttribute("data-precedence"))break;return t;case"script":if(c=t.getAttribute("src"),(c!==(l.src==null?null:l.src)||t.getAttribute("type")!==(l.type==null?null:l.type)||t.getAttribute("crossorigin")!==(l.crossOrigin==null?null:l.crossOrigin))&&c&&t.hasAttribute("async")&&!t.hasAttribute("itemprop"))break;return t;default:return t}}else if(n==="input"&&t.type==="hidden"){var c=l.name==null?null:""+l.name;if(l.type==="hidden"&&t.getAttribute("name")===c)return t}else return t;if(t=_i(t.nextSibling),t===null)break}return null}function rM(t,n,a){if(n==="")return null;for(;t.nodeType!==3;)if((t.nodeType!==1||t.nodeName!=="INPUT"||t.type!=="hidden")&&!a||(t=_i(t.nextSibling),t===null))return null;return t}function C0(t,n){for(;t.nodeType!==8;)if((t.nodeType!==1||t.nodeName!=="INPUT"||t.type!=="hidden")&&!n||(t=_i(t.nextSibling),t===null))return null;return t}function Zh(t){return t.data==="$?"||t.data==="$~"}function Kh(t){return t.data==="$!"||t.data==="$?"&&t.ownerDocument.readyState!=="loading"}function oM(t,n){var a=t.ownerDocument;if(t.data==="$~")t._reactRetry=n;else if(t.data!=="$?"||a.readyState!=="loading")n();else{var s=function(){n(),a.removeEventListener("DOMContentLoaded",s)};a.addEventListener("DOMContentLoaded",s),t._reactRetry=s}}function _i(t){for(;t!=null;t=t.nextSibling){var n=t.nodeType;if(n===1||n===3)break;if(n===8){if(n=t.data,n==="$"||n==="$!"||n==="$?"||n==="$~"||n==="&"||n==="F!"||n==="F")break;if(n==="/$"||n==="/&")return null}}return t}var Qh=null;function w0(t){t=t.nextSibling;for(var n=0;t;){if(t.nodeType===8){var a=t.data;if(a==="/$"||a==="/&"){if(n===0)return _i(t.nextSibling);n--}else a!=="$"&&a!=="$!"&&a!=="$?"&&a!=="$~"&&a!=="&"||n++}t=t.nextSibling}return null}function D0(t){t=t.previousSibling;for(var n=0;t;){if(t.nodeType===8){var a=t.data;if(a==="$"||a==="$!"||a==="$?"||a==="$~"||a==="&"){if(n===0)return t;n--}else a!=="/$"&&a!=="/&"||n++}t=t.previousSibling}return null}function lM(t,n){function a(){s=!0}if(t.ownerDocument.activeElement===t)return!0;var s=!1;try{t.ownerDocument.addEventListener("focus",a,!0),(t.focus||HTMLElement.prototype.focus).call(t,n)}finally{t.ownerDocument.removeEventListener("focus",a,!0)}return s}function uM(t){_0(function(){_0(function(n){return t(n)})})}function U0(t,n,a){switch(n=jo(a),t){case"html":if(t=n.documentElement,!t)throw Error(r(452));return t;case"head":if(t=n.head,!t)throw Error(r(453));return t;case"body":if(t=n.body,!t)throw Error(r(454));return t;default:throw Error(r(451))}}function N0(t,n,a){for(var s in a){var l=a[s];a.hasOwnProperty(s)&&l!=null&&Le(t,n,s,null,Bx,l)}a.dangerouslySetInnerHTML!=null&&(t.textContent=""),t.onclick===Ii&&(t.onclick=null),Cn(t)}function Jh(t){for(var n=t.attributes;n.length;)t.removeAttributeNode(n[0]);Cn(t)}var gi=new Map,L0=new Set;function Zo(t){if(typeof t.getRootNode=="function"){var n=t.getRootNode();if(n.nodeType===9||n.nodeType===11)return n}return t.nodeType===9?t:t.ownerDocument}var pa=bt.d;bt.d={f:cM,r:fM,D:hM,C:dM,L:pM,m:mM,X:gM,S:_M,M:vM};function cM(){var t=pa.f(),n=Au();return t||n}function fM(t){var n=en(t);n!==null&&n.tag===5&&n.type==="form"?P_(n):pa.r(t)}var Ur=typeof document>"u"?null:document;function O0(t,n,a){var s=Ur;if(s&&typeof n=="string"&&n){var l=ui(n);l='link[rel="'+t+'"][href="'+l+'"]',typeof a=="string"&&(l+='[crossorigin="'+a+'"]'),L0.has(l)||(L0.add(l),t={rel:t,crossOrigin:a,href:n},s.querySelector(l)===null&&(n=s.createElement("link"),En(n,"link",t),Be(n),s.head.appendChild(n)))}}function hM(t){pa.D(t),O0("dns-prefetch",t,null)}function dM(t,n){pa.C(t,n),O0("preconnect",t,n)}function pM(t,n,a){pa.L(t,n,a);var s=Ur;if(s&&t&&n){var l='link[rel="preload"][as="'+ui(n)+'"]';n==="image"&&a&&a.imageSrcSet?(l+='[imagesrcset="'+ui(a.imageSrcSet)+'"]',typeof a.imageSizes=="string"&&(l+='[imagesizes="'+ui(a.imageSizes)+'"]')):l+='[href="'+ui(t)+'"]';var c=l;switch(n){case"style":c=Nr(t);break;case"script":c=Lr(t)}if(!(gi.has(c)||(t=O({rel:"preload",href:n==="image"&&a&&a.imageSrcSet?void 0:t,as:n},a),gi.set(c,t),s.querySelector(l)!==null||n==="style"&&s.querySelector(Ko(c))||n==="script"&&s.querySelector(Qo(c))))){var m=s.createElement("link");En(m,"link",t),n==="style"&&(m[Me]=!0,m.onload=m.onerror=function(){Ks(m)}),Be(m),s.head.appendChild(m)}}}function mM(t,n){pa.m(t,n);var a=Ur;if(a&&t){var s=n&&typeof n.as=="string"?n.as:"script",l='link[rel="modulepreload"][as="'+ui(s)+'"][href="'+ui(t)+'"]',c=l;switch(s){case"audioworklet":case"paintworklet":case"serviceworker":case"sharedworker":case"worker":case"script":c=Lr(t)}if(!gi.has(c)&&(t=O({rel:"modulepreload",href:t},n),gi.set(c,t),a.querySelector(l)===null)){switch(s){case"audioworklet":case"paintworklet":case"serviceworker":case"sharedworker":case"worker":case"script":if(a.querySelector(Qo(c)))return}s=a.createElement("link"),En(s,"link",t),Be(s),a.head.appendChild(s)}}}function _M(t,n,a){pa.S(t,n,a);var s=Ur;if(s&&t){var l=Pe(s).hoistableStyles,c=Nr(t);n=n||"default";var m=l.get(c);if(!m){var b={loading:0,preload:null};if(m=s.querySelector(Ko(c)))b.loading=5;else{t=O({rel:"stylesheet",href:t,"data-precedence":n},a),(a=gi.get(c))&&$h(t,a);var z=m=s.createElement("link");Be(z),En(z,"link",t),z._p=new Promise(function(W,et){z.onload=W,z.onerror=et}),z.addEventListener("load",function(){b.loading|=1}),z.addEventListener("error",function(){b.loading|=2}),b.loading|=4,Lu(m,n,s)}m={type:"stylesheet",instance:m,count:1,state:b},l.set(c,m)}}}function gM(t,n){pa.X(t,n);var a=Ur;if(a&&t){var s=Pe(a).hoistableScripts,l=Lr(t),c=s.get(l);c||(c=a.querySelector(Qo(l)),c||(t=O({src:t,async:!0},n),(n=gi.get(l))&&td(t,n),c=a.createElement("script"),Be(c),En(c,"link",t),a.head.appendChild(c)),c={type:"script",instance:c,count:1,state:null},s.set(l,c))}}function vM(t,n){pa.M(t,n);var a=Ur;if(a&&t){var s=Pe(a).hoistableScripts,l=Lr(t),c=s.get(l);c||(c=a.querySelector(Qo(l)),c||(t=O({src:t,async:!0,type:"module"},n),(n=gi.get(l))&&td(t,n),c=a.createElement("script"),Be(c),En(c,"link",t),a.head.appendChild(c)),c={type:"script",instance:c,count:1,state:null},s.set(l,c))}}function P0(t,n,a,s){var l=(l=A.current)?Zo(l):null;if(!l)throw Error(r(446));switch(t){case"meta":case"title":return null;case"style":return typeof a.precedence=="string"&&typeof a.href=="string"?(a=Nr(a.href),n=Pe(l).hoistableStyles,s=n.get(a),s||(s={type:"style",instance:null,count:0,state:null},n.set(a,s)),s):{type:"void",instance:null,count:0,state:null};case"link":if(a.rel==="stylesheet"&&typeof a.href=="string"&&typeof a.precedence=="string"){t=Nr(a.href);var c=Pe(l).hoistableStyles,m=c.get(t);if(m||(l=l.ownerDocument||l,m={type:"stylesheet",instance:null,count:0,state:{loading:0,preload:null}},c.set(t,m),(c=l.querySelector(Ko(t)))?c._p||(m.instance=c,m.state.loading=5):(c=gi.get(t),c||(c={rel:"preload",as:"style",href:a.href,crossOrigin:a.crossOrigin,integrity:a.integrity,media:a.media,hrefLang:a.hrefLang,referrerPolicy:a.referrerPolicy},gi.set(t,c)),SM(l,t,c,m.state))),n&&s===null)throw Error(r(528,""));return m}if(n&&s!==null)throw Error(r(529,""));return null;case"script":return n=a.async,a=a.src,typeof a=="string"&&n&&typeof n!="function"&&typeof n!="symbol"?(a=Lr(a),n=Pe(l).hoistableScripts,s=n.get(a),s||(s={type:"script",instance:null,count:0,state:null},n.set(a,s)),s):{type:"void",instance:null,count:0,state:null};default:throw Error(r(444,t))}}function Nr(t){return'href="'+ui(t)+'"'}function Ko(t){return'link[rel="stylesheet"]['+t+"]"}function z0(t){return O({},t,{"data-precedence":t.precedence,precedence:null})}function SM(t,n,a,s){if(n=t.querySelector('link[rel="preload"][as="style"]['+n+"]")){if(n[Me]!==!0){s.loading=1;return}}else n=t.createElement("link"),n[Me]=!0,n.onload=n.onerror=Ks.bind(null,n),En(n,"link",a),Be(n),t.head.appendChild(n);s.preload=n,n.addEventListener("load",function(){return s.loading|=1}),n.addEventListener("error",function(){return s.loading|=2})}function Lr(t){return'[src="'+ui(t)+'"]'}function Qo(t){return"script[async]"+t}function I0(t,n,a){if(n.count++,n.instance===null)switch(n.type){case"style":var s=t.querySelector('style[data-href~="'+ui(a.href)+'"]');if(s)return n.instance=s,Be(s),s;var l=O({},a,{"data-href":a.href,"data-precedence":a.precedence,href:null,precedence:null});return s=(t.ownerDocument||t).createElement("style"),Be(s),En(s,"style",l),Lu(s,a.precedence,t),n.instance=s;case"stylesheet":l=Nr(a.href);var c=t.querySelector(Ko(l));if(c)return n.state.loading|=4,n.instance=c,Be(c),c;s=z0(a),(l=gi.get(l))&&$h(s,l),c=(t.ownerDocument||t).createElement("link"),Be(c);var m=c;return m._p=new Promise(function(b,z){m.onload=b,m.onerror=z}),En(c,"link",s),n.state.loading|=4,Lu(c,a.precedence,t),n.instance=c;case"script":return c=Lr(a.src),(l=t.querySelector(Qo(c)))?(n.instance=l,Be(l),l):(s=a,(l=gi.get(c))&&(s=O({},a),td(s,l)),t=t.ownerDocument||t,l=t.createElement("script"),Be(l),En(l,"link",s),t.head.appendChild(l),n.instance=l);case"void":return null;default:throw Error(r(443,n.type))}else n.type==="stylesheet"&&(n.state.loading&4)===0&&(s=n.instance,n.state.loading|=4,Lu(s,a.precedence,t));return n.instance}function Lu(t,n,a){for(var s=a.querySelectorAll('link[rel="stylesheet"][data-precedence],style[data-precedence]'),l=s.length?s[s.length-1]:null,c=l,m=0;m<s.length;m++){var b=s[m];if(b.dataset.precedence===n)c=b;else if(c!==l)break}c?c.parentNode.insertBefore(t,c.nextSibling):(n=a.nodeType===9?a.head:a,n.insertBefore(t,n.firstChild))}function $h(t,n){t.crossOrigin==null&&(t.crossOrigin=n.crossOrigin),t.referrerPolicy==null&&(t.referrerPolicy=n.referrerPolicy),t.title==null&&(t.title=n.title)}function td(t,n){t.crossOrigin==null&&(t.crossOrigin=n.crossOrigin),t.referrerPolicy==null&&(t.referrerPolicy=n.referrerPolicy),t.integrity==null&&(t.integrity=n.integrity)}var Ou=null;function B0(t,n,a){if(Ou===null){var s=new Map,l=Ou=new Map;l.set(a,s)}else l=Ou,s=l.get(a),s||(s=new Map,l.set(a,s));if(s.has(t))return s;for(s.set(t,null),a=a.getElementsByTagName(t),l=0;l<a.length;l++){var c=a[l];if(!(c[We]||c[Ut]||t==="link"&&c.getAttribute("rel")==="stylesheet")&&c.namespaceURI!=="http://www.w3.org/2000/svg"){var m=c.getAttribute(n)||"";m=t+m;var b=s.get(m);b?b.push(c):s.set(m,[c])}}return s}function ed(t,n,a){t=t.ownerDocument||t,t.head.insertBefore(a,n==="title"?t.querySelector("head > title"):null)}function yM(t,n,a){if(a===1||n.itemProp!=null)return!1;switch(t){case"meta":case"title":return!0;case"style":if(typeof n.precedence!="string"||typeof n.href!="string"||n.href==="")break;return!0;case"link":if(typeof n.rel!="string"||typeof n.href!="string"||n.href===""||n.onLoad||n.onError)break;return n.rel==="stylesheet"?(t=n.disabled,typeof n.precedence=="string"&&t==null):!0;case"script":if(n.async&&typeof n.async!="function"&&typeof n.async!="symbol"&&!n.onLoad&&!n.onError&&n.src&&typeof n.src=="string")return!0}return!1}function F0(t,n){return t==="img"&&n.src!=null&&n.src!==""&&n.onLoad==null&&n.loading!=="lazy"}function H0(t){return!(t.type==="stylesheet"&&(t.state.loading&3)===0)}function G0(t){return(t.width||100)*(t.height||100)*(typeof devicePixelRatio=="number"?devicePixelRatio:1)*.25}function V0(t,n){typeof n.decode=="function"&&(t.imgCount++,n.complete||(t.imgBytes+=G0(n),t.suspenseyImages.push(n)),t=EM.bind(t),n.decode().then(t,t))}function xM(t,n,a,s){if(a.type==="stylesheet"&&(typeof s.media!="string"||matchMedia(s.media).matches!==!1)&&(a.state.loading&4)===0){if(a.instance===null){var l=Nr(s.href),c=n.querySelector(Ko(l));if(c){n=c._p,n!==null&&typeof n=="object"&&typeof n.then=="function"&&(t.count++,t=Jo.bind(t),n.then(t,t)),a.state.loading|=4,a.instance=c,Be(c);return}c=n.ownerDocument||n,s=z0(s),(l=gi.get(l))&&$h(s,l),c=c.createElement("link"),Be(c);var m=c;m._p=new Promise(function(b,z){m.onload=b,m.onerror=z}),En(c,"link",s),a.instance=c}t.stylesheets===null&&(t.stylesheets=new Map),t.stylesheets.set(a,n),(n=a.state.preload)&&(a.state.loading&3)===0&&(t.count++,a=Jo.bind(t),n.addEventListener("load",a),n.addEventListener("error",a))}}var Pu=0;function MM(t,n){return t.stylesheets&&t.count===0&&Iu(t,t.stylesheets),0<t.count||0<t.imgCount?function(a){var s=setTimeout(function(){if(t.stylesheets&&Iu(t,t.stylesheets),t.unsuspend){var c=t.unsuspend;t.unsuspend=null,c()}},6e4+n);0<t.imgBytes&&Pu===0&&(Pu=62500*Hx());var l=setTimeout(function(){if(t.waitingForImages=!1,t.count===0&&(t.stylesheets&&Iu(t,t.stylesheets),t.unsuspend)){var c=t.unsuspend;t.unsuspend=null,c()}},(t.imgBytes>Pu?50:800)+n);return t.unsuspend=a,function(){t.unsuspend=null,clearTimeout(s),clearTimeout(l)}}:null}function X0(t){if(t.count===0&&(t.imgCount===0||!t.waitingForImages)){if(t.stylesheets)Iu(t,t.stylesheets);else if(t.unsuspend){var n=t.unsuspend;t.unsuspend=null,n()}}}function Jo(){this.count--,X0(this)}function EM(){this.imgCount--,X0(this)}var zu=null;function Iu(t,n){t.stylesheets=null,t.unsuspend!==null&&(t.count++,zu=new Map,n.forEach(TM,t),zu=null,Jo.call(t))}function TM(t,n){if(!(n.state.loading&4)){var a=zu.get(t);if(a)var s=a.get(null);else{a=new Map,zu.set(t,a);for(var l=t.querySelectorAll("link[data-precedence],style[data-precedence]"),c=0;c<l.length;c++){var m=l[c];(m.nodeName==="LINK"||m.getAttribute("media")!=="not all")&&(a.set(m.dataset.precedence,m),s=m)}s&&a.set(null,s)}l=n.instance,m=l.getAttribute("data-precedence"),c=a.get(m)||s,c===s&&a.set(null,l),a.set(m,l),this.count++,s=Jo.bind(this),l.addEventListener("load",s),l.addEventListener("error",s),c?c.parentNode.insertBefore(l,c.nextSibling):(t=t.nodeType===9?t.head:t,t.insertBefore(l,t.firstChild)),n.state.loading|=4}}var Or={$$typeof:ft,Provider:null,Consumer:null,_currentValue:F,_currentValue2:F,_threadCount:0};function bM(t,n,a,s,l,c,m,b,z){this.tag=1,this.containerInfo=t,this.pingCache=this.current=this.pendingChildren=null,this.timeoutHandle=-1,this.callbackNode=this.next=this.pendingContext=this.context=this.cancelPendingCommit=null,this.callbackPriority=0,this.expirationTimes=C(-1),this.entangledLanes=this.shellSuspendCounter=this.errorRecoveryDisabledLanes=this.expiredLanes=this.warmLanes=this.pingedLanes=this.suspendedLanes=this.pendingLanes=0,this.entanglements=C(0),this.hiddenUpdates=C(null),this.identifierPrefix=s,this.onUncaughtError=l,this.onCaughtError=c,this.onRecoverableError=m,this.pooledCache=null,this.pooledCacheLanes=0,this.formState=z,this.transitionTypes=null,this.incompleteTransitions=new Map}function Y0(t,n,a,s,l,c,m,b,z,W,et,ct){return t=new bM(t,n,a,m,z,W,et,ct,b),n=1,c===!0&&(n|=24),c=Gn(3,null,null,n),t.current=c,c.stateNode=t,n=_f(),n.refCount++,t.pooledCache=n,n.refCount++,c.memoizedState={element:s,isDehydrated:a,cache:n},yf(c),t}function k0(t){return t?(t=rr,t):rr}function q0(t,n,a,s,l,c){l=k0(l),s.context===null?s.context=l:s.pendingContext=l,s=Oa(n),s.payload={element:a},c=c===void 0?null:c,c!==null&&(s.callback=c),a=Pa(t,s,n),a!==null&&(kn(a,t,n),wo(a,t,n))}function W0(t,n){if(t=t.memoizedState,t!==null&&t.dehydrated!==null){var a=t.retryLane;t.retryLane=a!==0&&a<n?a:n}}function nd(t,n){W0(t,n),(t=t.alternate)&&W0(t,n)}function j0(t){if(t.tag===13||t.tag===31){var n=_s(t,67108864);n!==null&&kn(n,t,67108864),nd(t,67108864)}}function Z0(t){if(t.tag===13||t.tag===31){var n=ai();n=Nt(n);var a=_s(t,n);a!==null&&kn(a,t,n),nd(t,n)}}var Pr=!0;function AM(t,n,a,s){var l=Mt.T;Mt.T=null;var c=bt.p;try{bt.p=2,id(t,n,a,s)}finally{bt.p=c,Mt.T=l}}function RM(t,n,a,s){var l=Mt.T;Mt.T=null;var c=bt.p;try{bt.p=8,id(t,n,a,s)}finally{bt.p=c,Mt.T=l}}function id(t,n,a,s){if(Pr){var l=ad(s);if(l===null)Bh(t,n,s,Bu,a),Q0(t,s);else if(wM(l,t,n,a,s))s.stopPropagation();else if(Q0(t,s),n&4&&-1<CM.indexOf(t)){for(;l!==null;){var c=en(l);if(c!==null)switch(c.tag){case 3:if(c=c.stateNode,c.current.memoizedState.isDehydrated){var m=li(c.pendingLanes);if(m!==0){var b=c;for(b.pendingLanes|=2,b.entangledLanes|=2;m;){var z=1<<31-Rn(m);b.entanglements[1]|=z,m&=~z}Wi(c),(Ce&6)===0&&(Eu=Tt()+500,ko(0))}}break;case 31:case 13:b=_s(c,2),b!==null&&kn(b,c,2),Au(),nd(c,2)}if(c=ad(s),c===null&&Bh(t,n,s,Bu,a),c===l)break;l=c}l!==null&&s.stopPropagation()}else Bh(t,n,s,null,a)}}function ad(t){return t=Vc(t),sd(t)}var Bu=null;function sd(t){if(Bu=null,t=Hn(t),t!==null){var n=f(t);if(n===null)t=null;else{var a=n.tag;if(a===13){if(t=h(n),t!==null)return t;t=null}else if(a===31){if(t=d(n),t!==null)return t;t=null}else if(a===3){if(n.stateNode.current.memoizedState.isDehydrated)return n.tag===3?n.stateNode.containerInfo:null;t=null}else n!==t&&(t=null)}}return Bu=t,null}function K0(t){switch(t){case"beforetoggle":case"cancel":case"click":case"close":case"contextmenu":case"copy":case"cut":case"auxclick":case"dblclick":case"dragend":case"dragstart":case"drop":case"focusin":case"focusout":case"input":case"invalid":case"keydown":case"keypress":case"keyup":case"mousedown":case"mouseup":case"paste":case"pause":case"play":case"pointercancel":case"pointerdown":case"pointerup":case"ratechange":case"reset":case"seeked":case"submit":case"toggle":case"touchcancel":case"touchend":case"touchstart":case"volumechange":case"change":case"selectionchange":case"textInput":case"compositionstart":case"compositionend":case"compositionupdate":case"beforeblur":case"afterblur":case"beforeinput":case"blur":case"fullscreenchange":case"fullscreenerror":case"focus":case"hashchange":case"popstate":case"select":case"selectstart":return 2;case"drag":case"dragenter":case"dragexit":case"dragleave":case"dragover":case"mousemove":case"mouseout":case"mouseover":case"pointermove":case"pointerout":case"pointerover":case"resize":case"scroll":case"touchmove":case"wheel":case"mouseenter":case"mouseleave":case"pointerenter":case"pointerleave":return 8;case"message":switch(ot()){case _t:return 2;case Lt:return 8;case Ot:case xe:return 32;case ke:return 268435456;default:return 32}default:return 32}}var rd=!1,Wa=null,ja=null,Za=null,$o=new Map,tl=new Map,Ka=[],CM="mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset".split(" ");function Q0(t,n){switch(t){case"focusin":case"focusout":Wa=null;break;case"dragenter":case"dragleave":ja=null;break;case"mouseover":case"mouseout":Za=null;break;case"pointerover":case"pointerout":$o.delete(n.pointerId);break;case"gotpointercapture":case"lostpointercapture":tl.delete(n.pointerId)}}function el(t,n,a,s,l,c){return t===null||t.nativeEvent!==c?(t={blockedOn:n,domEventName:a,eventSystemFlags:s,nativeEvent:c,targetContainers:[l]},n!==null&&(n=en(n),n!==null&&j0(n)),t):(t.eventSystemFlags|=s,n=t.targetContainers,l!==null&&n.indexOf(l)===-1&&n.push(l),t)}function wM(t,n,a,s,l){switch(n){case"focusin":return Wa=el(Wa,t,n,a,s,l),!0;case"dragenter":return ja=el(ja,t,n,a,s,l),!0;case"mouseover":return Za=el(Za,t,n,a,s,l),!0;case"pointerover":var c=l.pointerId;return $o.set(c,el($o.get(c)||null,t,n,a,s,l)),!0;case"gotpointercapture":return c=l.pointerId,tl.set(c,el(tl.get(c)||null,t,n,a,s,l)),!0}return!1}function J0(t){var n=Hn(t.target);if(n!==null){var a=f(n);if(a!==null){if(n=a.tag,n===13){if(n=h(a),n!==null){t.blockedOn=n,Qt(t.priority,function(){Z0(a)});return}}else if(n===31){if(n=d(a),n!==null){t.blockedOn=n,Qt(t.priority,function(){Z0(a)});return}}else if(n===3&&a.stateNode.current.memoizedState.isDehydrated){t.blockedOn=a.tag===3?a.stateNode.containerInfo:null;return}}}t.blockedOn=null}function Fu(t){if(t.blockedOn!==null)return!1;for(var n=t.targetContainers;0<n.length;){var a=ad(t.nativeEvent);if(a===null){a=t.nativeEvent;var s=new a.constructor(a.type,a);Gc=s,a.target.dispatchEvent(s),Gc=null}else return n=en(a),n!==null&&j0(n),t.blockedOn=a,!1;n.shift()}return!0}function $0(t,n,a){Fu(t)&&a.delete(n)}function DM(){rd=!1,Wa!==null&&Fu(Wa)&&(Wa=null),ja!==null&&Fu(ja)&&(ja=null),Za!==null&&Fu(Za)&&(Za=null),$o.forEach($0),tl.forEach($0)}function Hu(t,n){t.blockedOn===n&&(t.blockedOn=null,rd||(rd=!0,o.unstable_scheduleCallback(o.unstable_NormalPriority,DM)))}var Gu=null;function tv(t){Gu!==t&&(Gu=t,o.unstable_scheduleCallback(o.unstable_NormalPriority,function(){Gu===t&&(Gu=null);for(var n=0;n<t.length;n+=3){var a=t[n],s=t[n+1],l=t[n+2];if(typeof s!="function"){if(sd(s||a)===null)continue;break}var c=en(a);c!==null&&(t.splice(n,3),n-=3,Gf(c,{pending:!0,data:l,method:a.method,action:s},s,l))}}))}function zr(t){function n(z){return Hu(z,t)}Wa!==null&&Hu(Wa,t),ja!==null&&Hu(ja,t),Za!==null&&Hu(Za,t),$o.forEach(n),tl.forEach(n);for(var a=0;a<Ka.length;a++){var s=Ka[a];s.blockedOn===t&&(s.blockedOn=null)}for(;0<Ka.length&&(a=Ka[0],a.blockedOn===null);)J0(a),a.blockedOn===null&&Ka.shift();if(a=(t.ownerDocument||t).$$reactFormReplay,a!=null)for(s=0;s<a.length;s+=3){var l=a[s],c=a[s+1],m=l[ie]||null;if(typeof c=="function")m||tv(a);else if(m){var b=null;if(c&&c.hasAttribute("formAction")){if(l=c,m=c[ie]||null)b=m.formAction;else if(sd(l)!==null)continue}else b=m.action;typeof b=="function"?a[s+1]=b:(a.splice(s,3),s-=3),tv(a)}}}function ev(){function t(c){c.canIntercept&&c.info==="react-transition"&&c.intercept({handler:function(){return new Promise(function(m){return l=m})},focusReset:"manual",scroll:"manual"})}function n(){l!==null&&(l(),l=null),s||setTimeout(a,20)}function a(){if(!s&&!navigation.transition){var c=navigation.currentEntry;c&&c.url!=null&&navigation.navigate(c.url,{state:c.getState(),info:"react-transition",history:"replace"})}}if(typeof navigation=="object"){var s=!1,l=null;return navigation.addEventListener("navigate",t),navigation.addEventListener("navigatesuccess",n),navigation.addEventListener("navigateerror",n),setTimeout(a,100),function(){s=!0,navigation.removeEventListener("navigate",t),navigation.removeEventListener("navigatesuccess",n),navigation.removeEventListener("navigateerror",n),l!==null&&(l(),l=null)}}}function od(t){this._internalRoot=t}Vu.prototype.render=od.prototype.render=function(t){var n=this._internalRoot;if(n===null)throw Error(r(409));var a=n.current,s=ai();q0(a,s,t,n,null,null)},Vu.prototype.unmount=od.prototype.unmount=function(){var t=this._internalRoot;if(t!==null){this._internalRoot=null;var n=t.containerInfo;q0(t.current,2,null,t,null,null),Au(),n[be]=null}};function Vu(t){this._internalRoot=t}Vu.prototype.unstable_scheduleHydration=function(t){if(t){var n=Yt();t={blockedOn:null,target:t,priority:n};for(var a=0;a<Ka.length&&n!==0&&n<Ka[a].priority;a++);Ka.splice(a,0,t),a===0&&J0(t)}};var nv=e.version;if(nv!=="19.3.1")throw Error(r(527,nv,"19.3.1"));bt.findDOMNode=function(t){var n=t._reactInternals;if(n===void 0)throw typeof t.render=="function"?Error(r(188)):(t=Object.keys(t).join(","),Error(r(268,t)));return t=g(n),t=t!==null?v(t):null,t=t===null?null:t.stateNode,t};var UM={bundleType:0,version:"19.3.1",rendererPackageName:"react-dom",currentDispatcherRef:Mt,reconcilerVersion:"19.3.1"};if(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__<"u"){var Xu=__REACT_DEVTOOLS_GLOBAL_HOOK__;if(!Xu.isDisabled&&Xu.supportsFiber)try{tn=Xu.inject(UM),qe=Xu}catch{}}return il.createRoot=function(t,n){if(!u(t))throw Error(r(299));var a=!1,s="",l=k_,c=q_,m=W_;return n!=null&&(n.unstable_strictMode===!0&&(a=!0),n.identifierPrefix!==void 0&&(s=n.identifierPrefix),n.onUncaughtError!==void 0&&(l=n.onUncaughtError),n.onCaughtError!==void 0&&(c=n.onCaughtError),n.onRecoverableError!==void 0&&(m=n.onRecoverableError)),n=Y0(t,1,!1,null,null,a,s,null,l,c,m,ev),t[be]=n.current,Ih(t),new od(n)},il.hydrateRoot=function(t,n,a){if(!u(t))throw Error(r(299));var s=!1,l="",c=k_,m=q_,b=W_,z=null;return a!=null&&(a.unstable_strictMode===!0&&(s=!0),a.identifierPrefix!==void 0&&(l=a.identifierPrefix),a.onUncaughtError!==void 0&&(c=a.onUncaughtError),a.onCaughtError!==void 0&&(m=a.onCaughtError),a.onRecoverableError!==void 0&&(b=a.onRecoverableError),a.formState!==void 0&&(z=a.formState)),n=Y0(t,1,!0,n,a??null,s,l,z,c,m,b,ev),n.context=k0(null),a=n.current,s=ai(),s=Nt(s),l=Oa(s),l.callback=null,Pa(a,l,s),a=s,n.current.lanes=a,k(n,a),Wi(n),t[be]=n.current,Ih(t),new Vu(n)},il.version="19.3.1",il}var hv;function GM(){if(hv)return cd.exports;hv=1;function o(){if(!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__>"u"||typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE!="function"))try{__REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(o)}catch(e){console.error(e)}}return o(),cd.exports=HM(),cd.exports}var VM=GM();const Pp="169",to={ROTATE:0,DOLLY:1,PAN:2},Jr={ROTATE:0,PAN:1,DOLLY_PAN:2,DOLLY_ROTATE:3},XM=0,dv=1,YM=2,_S=1,kM=2,ya=3,ls=0,Zn=1,Li=2,rs=0,eo=1,pv=2,mv=3,_v=4,qM=5,Gs=100,WM=101,jM=102,ZM=103,KM=104,QM=200,JM=201,$M=202,tE=203,Wd=204,jd=205,eE=206,nE=207,iE=208,aE=209,sE=210,rE=211,oE=212,lE=213,uE=214,Zd=0,Kd=1,Qd=2,ao=3,Jd=4,$d=5,tp=6,ep=7,gS=0,cE=1,fE=2,os=0,hE=1,dE=2,pE=3,mE=4,_E=5,gE=6,vE=7,vS=300,so=301,ro=302,np=303,ip=304,Uc=306,ap=1e3,Xs=1001,sp=1002,yi=1003,SE=1004,Yu=1005,Oi=1006,pd=1007,Ys=1008,Ea=1009,SS=1010,yS=1011,ml=1012,zp=1013,ks=1014,xa=1015,_l=1016,Ip=1017,Bp=1018,oo=1020,xS=35902,MS=1021,ES=1022,zi=1023,TS=1024,bS=1025,no=1026,lo=1027,AS=1028,Fp=1029,RS=1030,Hp=1031,Gp=1033,_c=33776,gc=33777,vc=33778,Sc=33779,rp=35840,op=35841,lp=35842,up=35843,cp=36196,fp=37492,hp=37496,dp=37808,pp=37809,mp=37810,_p=37811,gp=37812,vp=37813,Sp=37814,yp=37815,xp=37816,Mp=37817,Ep=37818,Tp=37819,bp=37820,Ap=37821,yc=36492,Rp=36494,Cp=36495,CS=36283,wp=36284,Dp=36285,Up=36286,yE=3200,xE=3201,ME=0,EE=1,ss="",ji="srgb",cs="srgb-linear",Vp="display-p3",Nc="display-p3-linear",Tc="linear",Xe="srgb",bc="rec709",Ac="p3",Ir=7680,gv=519,TE=512,bE=513,AE=514,wS=515,RE=516,CE=517,wE=518,DE=519,vv=35044,Sv="300 es",Ma=2e3,Rc=2001;class Zs{addEventListener(e,i){this._listeners===void 0&&(this._listeners={});const r=this._listeners;r[e]===void 0&&(r[e]=[]),r[e].indexOf(i)===-1&&r[e].push(i)}hasEventListener(e,i){if(this._listeners===void 0)return!1;const r=this._listeners;return r[e]!==void 0&&r[e].indexOf(i)!==-1}removeEventListener(e,i){if(this._listeners===void 0)return;const u=this._listeners[e];if(u!==void 0){const f=u.indexOf(i);f!==-1&&u.splice(f,1)}}dispatchEvent(e){if(this._listeners===void 0)return;const r=this._listeners[e.type];if(r!==void 0){e.target=this;const u=r.slice(0);for(let f=0,h=u.length;f<h;f++)u[f].call(this,e);e.target=null}}}const Dn=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],xc=Math.PI/180,Np=180/Math.PI;function gl(){const o=Math.random()*4294967295|0,e=Math.random()*4294967295|0,i=Math.random()*4294967295|0,r=Math.random()*4294967295|0;return(Dn[o&255]+Dn[o>>8&255]+Dn[o>>16&255]+Dn[o>>24&255]+"-"+Dn[e&255]+Dn[e>>8&255]+"-"+Dn[e>>16&15|64]+Dn[e>>24&255]+"-"+Dn[i&63|128]+Dn[i>>8&255]+"-"+Dn[i>>16&255]+Dn[i>>24&255]+Dn[r&255]+Dn[r>>8&255]+Dn[r>>16&255]+Dn[r>>24&255]).toLowerCase()}function Fn(o,e,i){return Math.max(e,Math.min(i,o))}function UE(o,e){return(o%e+e)%e}function md(o,e,i){return(1-i)*o+i*e}function al(o,e){switch(e.constructor){case Float32Array:return o;case Uint32Array:return o/4294967295;case Uint16Array:return o/65535;case Uint8Array:return o/255;case Int32Array:return Math.max(o/2147483647,-1);case Int16Array:return Math.max(o/32767,-1);case Int8Array:return Math.max(o/127,-1);default:throw new Error("Invalid component type.")}}function qn(o,e){switch(e.constructor){case Float32Array:return o;case Uint32Array:return Math.round(o*4294967295);case Uint16Array:return Math.round(o*65535);case Uint8Array:return Math.round(o*255);case Int32Array:return Math.round(o*2147483647);case Int16Array:return Math.round(o*32767);case Int8Array:return Math.round(o*127);default:throw new Error("Invalid component type.")}}const NE={DEG2RAD:xc};class ce{constructor(e=0,i=0){ce.prototype.isVector2=!0,this.x=e,this.y=i}get width(){return this.x}set width(e){this.x=e}get height(){return this.y}set height(e){this.y=e}set(e,i){return this.x=e,this.y=i,this}setScalar(e){return this.x=e,this.y=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setComponent(e,i){switch(e){case 0:this.x=i;break;case 1:this.y=i;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y)}copy(e){return this.x=e.x,this.y=e.y,this}add(e){return this.x+=e.x,this.y+=e.y,this}addScalar(e){return this.x+=e,this.y+=e,this}addVectors(e,i){return this.x=e.x+i.x,this.y=e.y+i.y,this}addScaledVector(e,i){return this.x+=e.x*i,this.y+=e.y*i,this}sub(e){return this.x-=e.x,this.y-=e.y,this}subScalar(e){return this.x-=e,this.y-=e,this}subVectors(e,i){return this.x=e.x-i.x,this.y=e.y-i.y,this}multiply(e){return this.x*=e.x,this.y*=e.y,this}multiplyScalar(e){return this.x*=e,this.y*=e,this}divide(e){return this.x/=e.x,this.y/=e.y,this}divideScalar(e){return this.multiplyScalar(1/e)}applyMatrix3(e){const i=this.x,r=this.y,u=e.elements;return this.x=u[0]*i+u[3]*r+u[6],this.y=u[1]*i+u[4]*r+u[7],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this}clamp(e,i){return this.x=Math.max(e.x,Math.min(i.x,this.x)),this.y=Math.max(e.y,Math.min(i.y,this.y)),this}clampScalar(e,i){return this.x=Math.max(e,Math.min(i,this.x)),this.y=Math.max(e,Math.min(i,this.y)),this}clampLength(e,i){const r=this.length();return this.divideScalar(r||1).multiplyScalar(Math.max(e,Math.min(i,r)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(e){return this.x*e.x+this.y*e.y}cross(e){return this.x*e.y-this.y*e.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(e){const i=Math.sqrt(this.lengthSq()*e.lengthSq());if(i===0)return Math.PI/2;const r=this.dot(e)/i;return Math.acos(Fn(r,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){const i=this.x-e.x,r=this.y-e.y;return i*i+r*r}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,i){return this.x+=(e.x-this.x)*i,this.y+=(e.y-this.y)*i,this}lerpVectors(e,i,r){return this.x=e.x+(i.x-e.x)*r,this.y=e.y+(i.y-e.y)*r,this}equals(e){return e.x===this.x&&e.y===this.y}fromArray(e,i=0){return this.x=e[i],this.y=e[i+1],this}toArray(e=[],i=0){return e[i]=this.x,e[i+1]=this.y,e}fromBufferAttribute(e,i){return this.x=e.getX(i),this.y=e.getY(i),this}rotateAround(e,i){const r=Math.cos(i),u=Math.sin(i),f=this.x-e.x,h=this.y-e.y;return this.x=f*r-h*u+e.x,this.y=f*u+h*r+e.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}}class he{constructor(e,i,r,u,f,h,d,p,g){he.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],e!==void 0&&this.set(e,i,r,u,f,h,d,p,g)}set(e,i,r,u,f,h,d,p,g){const v=this.elements;return v[0]=e,v[1]=u,v[2]=d,v[3]=i,v[4]=f,v[5]=p,v[6]=r,v[7]=h,v[8]=g,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(e){const i=this.elements,r=e.elements;return i[0]=r[0],i[1]=r[1],i[2]=r[2],i[3]=r[3],i[4]=r[4],i[5]=r[5],i[6]=r[6],i[7]=r[7],i[8]=r[8],this}extractBasis(e,i,r){return e.setFromMatrix3Column(this,0),i.setFromMatrix3Column(this,1),r.setFromMatrix3Column(this,2),this}setFromMatrix4(e){const i=e.elements;return this.set(i[0],i[4],i[8],i[1],i[5],i[9],i[2],i[6],i[10]),this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,i){const r=e.elements,u=i.elements,f=this.elements,h=r[0],d=r[3],p=r[6],g=r[1],v=r[4],_=r[7],y=r[2],M=r[5],E=r[8],R=u[0],x=u[3],S=u[6],L=u[1],U=u[4],P=u[7],J=u[2],B=u[5],O=u[8];return f[0]=h*R+d*L+p*J,f[3]=h*x+d*U+p*B,f[6]=h*S+d*P+p*O,f[1]=g*R+v*L+_*J,f[4]=g*x+v*U+_*B,f[7]=g*S+v*P+_*O,f[2]=y*R+M*L+E*J,f[5]=y*x+M*U+E*B,f[8]=y*S+M*P+E*O,this}multiplyScalar(e){const i=this.elements;return i[0]*=e,i[3]*=e,i[6]*=e,i[1]*=e,i[4]*=e,i[7]*=e,i[2]*=e,i[5]*=e,i[8]*=e,this}determinant(){const e=this.elements,i=e[0],r=e[1],u=e[2],f=e[3],h=e[4],d=e[5],p=e[6],g=e[7],v=e[8];return i*h*v-i*d*g-r*f*v+r*d*p+u*f*g-u*h*p}invert(){const e=this.elements,i=e[0],r=e[1],u=e[2],f=e[3],h=e[4],d=e[5],p=e[6],g=e[7],v=e[8],_=v*h-d*g,y=d*p-v*f,M=g*f-h*p,E=i*_+r*y+u*M;if(E===0)return this.set(0,0,0,0,0,0,0,0,0);const R=1/E;return e[0]=_*R,e[1]=(u*g-v*r)*R,e[2]=(d*r-u*h)*R,e[3]=y*R,e[4]=(v*i-u*p)*R,e[5]=(u*f-d*i)*R,e[6]=M*R,e[7]=(r*p-g*i)*R,e[8]=(h*i-r*f)*R,this}transpose(){let e;const i=this.elements;return e=i[1],i[1]=i[3],i[3]=e,e=i[2],i[2]=i[6],i[6]=e,e=i[5],i[5]=i[7],i[7]=e,this}getNormalMatrix(e){return this.setFromMatrix4(e).invert().transpose()}transposeIntoArray(e){const i=this.elements;return e[0]=i[0],e[1]=i[3],e[2]=i[6],e[3]=i[1],e[4]=i[4],e[5]=i[7],e[6]=i[2],e[7]=i[5],e[8]=i[8],this}setUvTransform(e,i,r,u,f,h,d){const p=Math.cos(f),g=Math.sin(f);return this.set(r*p,r*g,-r*(p*h+g*d)+h+e,-u*g,u*p,-u*(-g*h+p*d)+d+i,0,0,1),this}scale(e,i){return this.premultiply(_d.makeScale(e,i)),this}rotate(e){return this.premultiply(_d.makeRotation(-e)),this}translate(e,i){return this.premultiply(_d.makeTranslation(e,i)),this}makeTranslation(e,i){return e.isVector2?this.set(1,0,e.x,0,1,e.y,0,0,1):this.set(1,0,e,0,1,i,0,0,1),this}makeRotation(e){const i=Math.cos(e),r=Math.sin(e);return this.set(i,-r,0,r,i,0,0,0,1),this}makeScale(e,i){return this.set(e,0,0,0,i,0,0,0,1),this}equals(e){const i=this.elements,r=e.elements;for(let u=0;u<9;u++)if(i[u]!==r[u])return!1;return!0}fromArray(e,i=0){for(let r=0;r<9;r++)this.elements[r]=e[r+i];return this}toArray(e=[],i=0){const r=this.elements;return e[i]=r[0],e[i+1]=r[1],e[i+2]=r[2],e[i+3]=r[3],e[i+4]=r[4],e[i+5]=r[5],e[i+6]=r[6],e[i+7]=r[7],e[i+8]=r[8],e}clone(){return new this.constructor().fromArray(this.elements)}}const _d=new he;function DS(o){for(let e=o.length-1;e>=0;--e)if(o[e]>=65535)return!0;return!1}function Cc(o){return document.createElementNS("http://www.w3.org/1999/xhtml",o)}function LE(){const o=Cc("canvas");return o.style.display="block",o}const yv={};function Mc(o){o in yv||(yv[o]=!0,console.warn(o))}function OE(o,e,i){return new Promise(function(r,u){function f(){switch(o.clientWaitSync(e,o.SYNC_FLUSH_COMMANDS_BIT,0)){case o.WAIT_FAILED:u();break;case o.TIMEOUT_EXPIRED:setTimeout(f,i);break;default:r()}}setTimeout(f,i)})}function PE(o){const e=o.elements;e[2]=.5*e[2]+.5*e[3],e[6]=.5*e[6]+.5*e[7],e[10]=.5*e[10]+.5*e[11],e[14]=.5*e[14]+.5*e[15]}function zE(o){const e=o.elements;e[11]===-1?(e[10]=-e[10]-1,e[14]=-e[14]):(e[10]=-e[10],e[14]=-e[14]+1)}const xv=new he().set(.8224621,.177538,0,.0331941,.9668058,0,.0170827,.0723974,.9105199),Mv=new he().set(1.2249401,-.2249404,0,-.0420569,1.0420571,0,-.0196376,-.0786361,1.0982735),sl={[cs]:{transfer:Tc,primaries:bc,luminanceCoefficients:[.2126,.7152,.0722],toReference:o=>o,fromReference:o=>o},[ji]:{transfer:Xe,primaries:bc,luminanceCoefficients:[.2126,.7152,.0722],toReference:o=>o.convertSRGBToLinear(),fromReference:o=>o.convertLinearToSRGB()},[Nc]:{transfer:Tc,primaries:Ac,luminanceCoefficients:[.2289,.6917,.0793],toReference:o=>o.applyMatrix3(Mv),fromReference:o=>o.applyMatrix3(xv)},[Vp]:{transfer:Xe,primaries:Ac,luminanceCoefficients:[.2289,.6917,.0793],toReference:o=>o.convertSRGBToLinear().applyMatrix3(Mv),fromReference:o=>o.applyMatrix3(xv).convertLinearToSRGB()}},IE=new Set([cs,Nc]),De={enabled:!0,_workingColorSpace:cs,get workingColorSpace(){return this._workingColorSpace},set workingColorSpace(o){if(!IE.has(o))throw new Error(`Unsupported working color space, "${o}".`);this._workingColorSpace=o},convert:function(o,e,i){if(this.enabled===!1||e===i||!e||!i)return o;const r=sl[e].toReference,u=sl[i].fromReference;return u(r(o))},fromWorkingColorSpace:function(o,e){return this.convert(o,this._workingColorSpace,e)},toWorkingColorSpace:function(o,e){return this.convert(o,e,this._workingColorSpace)},getPrimaries:function(o){return sl[o].primaries},getTransfer:function(o){return o===ss?Tc:sl[o].transfer},getLuminanceCoefficients:function(o,e=this._workingColorSpace){return o.fromArray(sl[e].luminanceCoefficients)}};function io(o){return o<.04045?o*.0773993808:Math.pow(o*.9478672986+.0521327014,2.4)}function gd(o){return o<.0031308?o*12.92:1.055*Math.pow(o,.41666)-.055}let Br;class BE{static getDataURL(e){if(/^data:/i.test(e.src)||typeof HTMLCanvasElement>"u")return e.src;let i;if(e instanceof HTMLCanvasElement)i=e;else{Br===void 0&&(Br=Cc("canvas")),Br.width=e.width,Br.height=e.height;const r=Br.getContext("2d");e instanceof ImageData?r.putImageData(e,0,0):r.drawImage(e,0,0,e.width,e.height),i=Br}return i.width>2048||i.height>2048?(console.warn("THREE.ImageUtils.getDataURL: Image converted to jpg for performance reasons",e),i.toDataURL("image/jpeg",.6)):i.toDataURL("image/png")}static sRGBToLinear(e){if(typeof HTMLImageElement<"u"&&e instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&e instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&e instanceof ImageBitmap){const i=Cc("canvas");i.width=e.width,i.height=e.height;const r=i.getContext("2d");r.drawImage(e,0,0,e.width,e.height);const u=r.getImageData(0,0,e.width,e.height),f=u.data;for(let h=0;h<f.length;h++)f[h]=io(f[h]/255)*255;return r.putImageData(u,0,0),i}else if(e.data){const i=e.data.slice(0);for(let r=0;r<i.length;r++)i instanceof Uint8Array||i instanceof Uint8ClampedArray?i[r]=Math.floor(io(i[r]/255)*255):i[r]=io(i[r]);return{data:i,width:e.width,height:e.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),e}}let FE=0;class US{constructor(e=null){this.isSource=!0,Object.defineProperty(this,"id",{value:FE++}),this.uuid=gl(),this.data=e,this.dataReady=!0,this.version=0}set needsUpdate(e){e===!0&&this.version++}toJSON(e){const i=e===void 0||typeof e=="string";if(!i&&e.images[this.uuid]!==void 0)return e.images[this.uuid];const r={uuid:this.uuid,url:""},u=this.data;if(u!==null){let f;if(Array.isArray(u)){f=[];for(let h=0,d=u.length;h<d;h++)u[h].isDataTexture?f.push(vd(u[h].image)):f.push(vd(u[h]))}else f=vd(u);r.url=f}return i||(e.images[this.uuid]=r),r}}function vd(o){return typeof HTMLImageElement<"u"&&o instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&o instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&o instanceof ImageBitmap?BE.getDataURL(o):o.data?{data:Array.from(o.data),width:o.width,height:o.height,type:o.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}let HE=0;class Kn extends Zs{constructor(e=Kn.DEFAULT_IMAGE,i=Kn.DEFAULT_MAPPING,r=Xs,u=Xs,f=Oi,h=Ys,d=zi,p=Ea,g=Kn.DEFAULT_ANISOTROPY,v=ss){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:HE++}),this.uuid=gl(),this.name="",this.source=new US(e),this.mipmaps=[],this.mapping=i,this.channel=0,this.wrapS=r,this.wrapT=u,this.magFilter=f,this.minFilter=h,this.anisotropy=g,this.format=d,this.internalFormat=null,this.type=p,this.offset=new ce(0,0),this.repeat=new ce(1,1),this.center=new ce(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new he,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=v,this.userData={},this.version=0,this.onUpdate=null,this.isRenderTargetTexture=!1,this.pmremVersion=0}get image(){return this.source.data}set image(e=null){this.source.data=e}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(e){return this.name=e.name,this.source=e.source,this.mipmaps=e.mipmaps.slice(0),this.mapping=e.mapping,this.channel=e.channel,this.wrapS=e.wrapS,this.wrapT=e.wrapT,this.magFilter=e.magFilter,this.minFilter=e.minFilter,this.anisotropy=e.anisotropy,this.format=e.format,this.internalFormat=e.internalFormat,this.type=e.type,this.offset.copy(e.offset),this.repeat.copy(e.repeat),this.center.copy(e.center),this.rotation=e.rotation,this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrix.copy(e.matrix),this.generateMipmaps=e.generateMipmaps,this.premultiplyAlpha=e.premultiplyAlpha,this.flipY=e.flipY,this.unpackAlignment=e.unpackAlignment,this.colorSpace=e.colorSpace,this.userData=JSON.parse(JSON.stringify(e.userData)),this.needsUpdate=!0,this}toJSON(e){const i=e===void 0||typeof e=="string";if(!i&&e.textures[this.uuid]!==void 0)return e.textures[this.uuid];const r={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(e).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(r.userData=this.userData),i||(e.textures[this.uuid]=r),r}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(e){if(this.mapping!==vS)return e;if(e.applyMatrix3(this.matrix),e.x<0||e.x>1)switch(this.wrapS){case ap:e.x=e.x-Math.floor(e.x);break;case Xs:e.x=e.x<0?0:1;break;case sp:Math.abs(Math.floor(e.x)%2)===1?e.x=Math.ceil(e.x)-e.x:e.x=e.x-Math.floor(e.x);break}if(e.y<0||e.y>1)switch(this.wrapT){case ap:e.y=e.y-Math.floor(e.y);break;case Xs:e.y=e.y<0?0:1;break;case sp:Math.abs(Math.floor(e.y)%2)===1?e.y=Math.ceil(e.y)-e.y:e.y=e.y-Math.floor(e.y);break}return this.flipY&&(e.y=1-e.y),e}set needsUpdate(e){e===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(e){e===!0&&this.pmremVersion++}}Kn.DEFAULT_IMAGE=null;Kn.DEFAULT_MAPPING=vS;Kn.DEFAULT_ANISOTROPY=1;class Je{constructor(e=0,i=0,r=0,u=1){Je.prototype.isVector4=!0,this.x=e,this.y=i,this.z=r,this.w=u}get width(){return this.z}set width(e){this.z=e}get height(){return this.w}set height(e){this.w=e}set(e,i,r,u){return this.x=e,this.y=i,this.z=r,this.w=u,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this.w=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setW(e){return this.w=e,this}setComponent(e,i){switch(e){case 0:this.x=i;break;case 1:this.y=i;break;case 2:this.z=i;break;case 3:this.w=i;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this.w=e.w!==void 0?e.w:1,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this.w+=e.w,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this.w+=e,this}addVectors(e,i){return this.x=e.x+i.x,this.y=e.y+i.y,this.z=e.z+i.z,this.w=e.w+i.w,this}addScaledVector(e,i){return this.x+=e.x*i,this.y+=e.y*i,this.z+=e.z*i,this.w+=e.w*i,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this.w-=e.w,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this.w-=e,this}subVectors(e,i){return this.x=e.x-i.x,this.y=e.y-i.y,this.z=e.z-i.z,this.w=e.w-i.w,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this.w*=e.w,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this.w*=e,this}applyMatrix4(e){const i=this.x,r=this.y,u=this.z,f=this.w,h=e.elements;return this.x=h[0]*i+h[4]*r+h[8]*u+h[12]*f,this.y=h[1]*i+h[5]*r+h[9]*u+h[13]*f,this.z=h[2]*i+h[6]*r+h[10]*u+h[14]*f,this.w=h[3]*i+h[7]*r+h[11]*u+h[15]*f,this}divideScalar(e){return this.multiplyScalar(1/e)}setAxisAngleFromQuaternion(e){this.w=2*Math.acos(e.w);const i=Math.sqrt(1-e.w*e.w);return i<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=e.x/i,this.y=e.y/i,this.z=e.z/i),this}setAxisAngleFromRotationMatrix(e){let i,r,u,f;const p=e.elements,g=p[0],v=p[4],_=p[8],y=p[1],M=p[5],E=p[9],R=p[2],x=p[6],S=p[10];if(Math.abs(v-y)<.01&&Math.abs(_-R)<.01&&Math.abs(E-x)<.01){if(Math.abs(v+y)<.1&&Math.abs(_+R)<.1&&Math.abs(E+x)<.1&&Math.abs(g+M+S-3)<.1)return this.set(1,0,0,0),this;i=Math.PI;const U=(g+1)/2,P=(M+1)/2,J=(S+1)/2,B=(v+y)/4,O=(_+R)/4,V=(E+x)/4;return U>P&&U>J?U<.01?(r=0,u=.707106781,f=.707106781):(r=Math.sqrt(U),u=B/r,f=O/r):P>J?P<.01?(r=.707106781,u=0,f=.707106781):(u=Math.sqrt(P),r=B/u,f=V/u):J<.01?(r=.707106781,u=.707106781,f=0):(f=Math.sqrt(J),r=O/f,u=V/f),this.set(r,u,f,i),this}let L=Math.sqrt((x-E)*(x-E)+(_-R)*(_-R)+(y-v)*(y-v));return Math.abs(L)<.001&&(L=1),this.x=(x-E)/L,this.y=(_-R)/L,this.z=(y-v)/L,this.w=Math.acos((g+M+S-1)/2),this}setFromMatrixPosition(e){const i=e.elements;return this.x=i[12],this.y=i[13],this.z=i[14],this.w=i[15],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this.w=Math.min(this.w,e.w),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this.w=Math.max(this.w,e.w),this}clamp(e,i){return this.x=Math.max(e.x,Math.min(i.x,this.x)),this.y=Math.max(e.y,Math.min(i.y,this.y)),this.z=Math.max(e.z,Math.min(i.z,this.z)),this.w=Math.max(e.w,Math.min(i.w,this.w)),this}clampScalar(e,i){return this.x=Math.max(e,Math.min(i,this.x)),this.y=Math.max(e,Math.min(i,this.y)),this.z=Math.max(e,Math.min(i,this.z)),this.w=Math.max(e,Math.min(i,this.w)),this}clampLength(e,i){const r=this.length();return this.divideScalar(r||1).multiplyScalar(Math.max(e,Math.min(i,r)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z+this.w*e.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,i){return this.x+=(e.x-this.x)*i,this.y+=(e.y-this.y)*i,this.z+=(e.z-this.z)*i,this.w+=(e.w-this.w)*i,this}lerpVectors(e,i,r){return this.x=e.x+(i.x-e.x)*r,this.y=e.y+(i.y-e.y)*r,this.z=e.z+(i.z-e.z)*r,this.w=e.w+(i.w-e.w)*r,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z&&e.w===this.w}fromArray(e,i=0){return this.x=e[i],this.y=e[i+1],this.z=e[i+2],this.w=e[i+3],this}toArray(e=[],i=0){return e[i]=this.x,e[i+1]=this.y,e[i+2]=this.z,e[i+3]=this.w,e}fromBufferAttribute(e,i){return this.x=e.getX(i),this.y=e.getY(i),this.z=e.getZ(i),this.w=e.getW(i),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}}class GE extends Zs{constructor(e=1,i=1,r={}){super(),this.isRenderTarget=!0,this.width=e,this.height=i,this.depth=1,this.scissor=new Je(0,0,e,i),this.scissorTest=!1,this.viewport=new Je(0,0,e,i);const u={width:e,height:i,depth:1};r=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:Oi,depthBuffer:!0,stencilBuffer:!1,resolveDepthBuffer:!0,resolveStencilBuffer:!0,depthTexture:null,samples:0,count:1},r);const f=new Kn(u,r.mapping,r.wrapS,r.wrapT,r.magFilter,r.minFilter,r.format,r.type,r.anisotropy,r.colorSpace);f.flipY=!1,f.generateMipmaps=r.generateMipmaps,f.internalFormat=r.internalFormat,this.textures=[];const h=r.count;for(let d=0;d<h;d++)this.textures[d]=f.clone(),this.textures[d].isRenderTargetTexture=!0;this.depthBuffer=r.depthBuffer,this.stencilBuffer=r.stencilBuffer,this.resolveDepthBuffer=r.resolveDepthBuffer,this.resolveStencilBuffer=r.resolveStencilBuffer,this.depthTexture=r.depthTexture,this.samples=r.samples}get texture(){return this.textures[0]}set texture(e){this.textures[0]=e}setSize(e,i,r=1){if(this.width!==e||this.height!==i||this.depth!==r){this.width=e,this.height=i,this.depth=r;for(let u=0,f=this.textures.length;u<f;u++)this.textures[u].image.width=e,this.textures[u].image.height=i,this.textures[u].image.depth=r;this.dispose()}this.viewport.set(0,0,e,i),this.scissor.set(0,0,e,i)}clone(){return new this.constructor().copy(this)}copy(e){this.width=e.width,this.height=e.height,this.depth=e.depth,this.scissor.copy(e.scissor),this.scissorTest=e.scissorTest,this.viewport.copy(e.viewport),this.textures.length=0;for(let r=0,u=e.textures.length;r<u;r++)this.textures[r]=e.textures[r].clone(),this.textures[r].isRenderTargetTexture=!0;const i=Object.assign({},e.texture.image);return this.texture.source=new US(i),this.depthBuffer=e.depthBuffer,this.stencilBuffer=e.stencilBuffer,this.resolveDepthBuffer=e.resolveDepthBuffer,this.resolveStencilBuffer=e.resolveStencilBuffer,e.depthTexture!==null&&(this.depthTexture=e.depthTexture.clone()),this.samples=e.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}}class qs extends GE{constructor(e=1,i=1,r={}){super(e,i,r),this.isWebGLRenderTarget=!0}}class NS extends Kn{constructor(e=null,i=1,r=1,u=1){super(null),this.isDataArrayTexture=!0,this.image={data:e,width:i,height:r,depth:u},this.magFilter=yi,this.minFilter=yi,this.wrapR=Xs,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}addLayerUpdate(e){this.layerUpdates.add(e)}clearLayerUpdates(){this.layerUpdates.clear()}}class VE extends Kn{constructor(e=null,i=1,r=1,u=1){super(null),this.isData3DTexture=!0,this.image={data:e,width:i,height:r,depth:u},this.magFilter=yi,this.minFilter=yi,this.wrapR=Xs,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}}class Ws{constructor(e=0,i=0,r=0,u=1){this.isQuaternion=!0,this._x=e,this._y=i,this._z=r,this._w=u}static slerpFlat(e,i,r,u,f,h,d){let p=r[u+0],g=r[u+1],v=r[u+2],_=r[u+3];const y=f[h+0],M=f[h+1],E=f[h+2],R=f[h+3];if(d===0){e[i+0]=p,e[i+1]=g,e[i+2]=v,e[i+3]=_;return}if(d===1){e[i+0]=y,e[i+1]=M,e[i+2]=E,e[i+3]=R;return}if(_!==R||p!==y||g!==M||v!==E){let x=1-d;const S=p*y+g*M+v*E+_*R,L=S>=0?1:-1,U=1-S*S;if(U>Number.EPSILON){const J=Math.sqrt(U),B=Math.atan2(J,S*L);x=Math.sin(x*B)/J,d=Math.sin(d*B)/J}const P=d*L;if(p=p*x+y*P,g=g*x+M*P,v=v*x+E*P,_=_*x+R*P,x===1-d){const J=1/Math.sqrt(p*p+g*g+v*v+_*_);p*=J,g*=J,v*=J,_*=J}}e[i]=p,e[i+1]=g,e[i+2]=v,e[i+3]=_}static multiplyQuaternionsFlat(e,i,r,u,f,h){const d=r[u],p=r[u+1],g=r[u+2],v=r[u+3],_=f[h],y=f[h+1],M=f[h+2],E=f[h+3];return e[i]=d*E+v*_+p*M-g*y,e[i+1]=p*E+v*y+g*_-d*M,e[i+2]=g*E+v*M+d*y-p*_,e[i+3]=v*E-d*_-p*y-g*M,e}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get w(){return this._w}set w(e){this._w=e,this._onChangeCallback()}set(e,i,r,u){return this._x=e,this._y=i,this._z=r,this._w=u,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(e){return this._x=e.x,this._y=e.y,this._z=e.z,this._w=e.w,this._onChangeCallback(),this}setFromEuler(e,i=!0){const r=e._x,u=e._y,f=e._z,h=e._order,d=Math.cos,p=Math.sin,g=d(r/2),v=d(u/2),_=d(f/2),y=p(r/2),M=p(u/2),E=p(f/2);switch(h){case"XYZ":this._x=y*v*_+g*M*E,this._y=g*M*_-y*v*E,this._z=g*v*E+y*M*_,this._w=g*v*_-y*M*E;break;case"YXZ":this._x=y*v*_+g*M*E,this._y=g*M*_-y*v*E,this._z=g*v*E-y*M*_,this._w=g*v*_+y*M*E;break;case"ZXY":this._x=y*v*_-g*M*E,this._y=g*M*_+y*v*E,this._z=g*v*E+y*M*_,this._w=g*v*_-y*M*E;break;case"ZYX":this._x=y*v*_-g*M*E,this._y=g*M*_+y*v*E,this._z=g*v*E-y*M*_,this._w=g*v*_+y*M*E;break;case"YZX":this._x=y*v*_+g*M*E,this._y=g*M*_+y*v*E,this._z=g*v*E-y*M*_,this._w=g*v*_-y*M*E;break;case"XZY":this._x=y*v*_-g*M*E,this._y=g*M*_-y*v*E,this._z=g*v*E+y*M*_,this._w=g*v*_+y*M*E;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+h)}return i===!0&&this._onChangeCallback(),this}setFromAxisAngle(e,i){const r=i/2,u=Math.sin(r);return this._x=e.x*u,this._y=e.y*u,this._z=e.z*u,this._w=Math.cos(r),this._onChangeCallback(),this}setFromRotationMatrix(e){const i=e.elements,r=i[0],u=i[4],f=i[8],h=i[1],d=i[5],p=i[9],g=i[2],v=i[6],_=i[10],y=r+d+_;if(y>0){const M=.5/Math.sqrt(y+1);this._w=.25/M,this._x=(v-p)*M,this._y=(f-g)*M,this._z=(h-u)*M}else if(r>d&&r>_){const M=2*Math.sqrt(1+r-d-_);this._w=(v-p)/M,this._x=.25*M,this._y=(u+h)/M,this._z=(f+g)/M}else if(d>_){const M=2*Math.sqrt(1+d-r-_);this._w=(f-g)/M,this._x=(u+h)/M,this._y=.25*M,this._z=(p+v)/M}else{const M=2*Math.sqrt(1+_-r-d);this._w=(h-u)/M,this._x=(f+g)/M,this._y=(p+v)/M,this._z=.25*M}return this._onChangeCallback(),this}setFromUnitVectors(e,i){let r=e.dot(i)+1;return r<Number.EPSILON?(r=0,Math.abs(e.x)>Math.abs(e.z)?(this._x=-e.y,this._y=e.x,this._z=0,this._w=r):(this._x=0,this._y=-e.z,this._z=e.y,this._w=r)):(this._x=e.y*i.z-e.z*i.y,this._y=e.z*i.x-e.x*i.z,this._z=e.x*i.y-e.y*i.x,this._w=r),this.normalize()}angleTo(e){return 2*Math.acos(Math.abs(Fn(this.dot(e),-1,1)))}rotateTowards(e,i){const r=this.angleTo(e);if(r===0)return this;const u=Math.min(1,i/r);return this.slerp(e,u),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(e){return this._x*e._x+this._y*e._y+this._z*e._z+this._w*e._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let e=this.length();return e===0?(this._x=0,this._y=0,this._z=0,this._w=1):(e=1/e,this._x=this._x*e,this._y=this._y*e,this._z=this._z*e,this._w=this._w*e),this._onChangeCallback(),this}multiply(e){return this.multiplyQuaternions(this,e)}premultiply(e){return this.multiplyQuaternions(e,this)}multiplyQuaternions(e,i){const r=e._x,u=e._y,f=e._z,h=e._w,d=i._x,p=i._y,g=i._z,v=i._w;return this._x=r*v+h*d+u*g-f*p,this._y=u*v+h*p+f*d-r*g,this._z=f*v+h*g+r*p-u*d,this._w=h*v-r*d-u*p-f*g,this._onChangeCallback(),this}slerp(e,i){if(i===0)return this;if(i===1)return this.copy(e);const r=this._x,u=this._y,f=this._z,h=this._w;let d=h*e._w+r*e._x+u*e._y+f*e._z;if(d<0?(this._w=-e._w,this._x=-e._x,this._y=-e._y,this._z=-e._z,d=-d):this.copy(e),d>=1)return this._w=h,this._x=r,this._y=u,this._z=f,this;const p=1-d*d;if(p<=Number.EPSILON){const M=1-i;return this._w=M*h+i*this._w,this._x=M*r+i*this._x,this._y=M*u+i*this._y,this._z=M*f+i*this._z,this.normalize(),this}const g=Math.sqrt(p),v=Math.atan2(g,d),_=Math.sin((1-i)*v)/g,y=Math.sin(i*v)/g;return this._w=h*_+this._w*y,this._x=r*_+this._x*y,this._y=u*_+this._y*y,this._z=f*_+this._z*y,this._onChangeCallback(),this}slerpQuaternions(e,i,r){return this.copy(e).slerp(i,r)}random(){const e=2*Math.PI*Math.random(),i=2*Math.PI*Math.random(),r=Math.random(),u=Math.sqrt(1-r),f=Math.sqrt(r);return this.set(u*Math.sin(e),u*Math.cos(e),f*Math.sin(i),f*Math.cos(i))}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._w===this._w}fromArray(e,i=0){return this._x=e[i],this._y=e[i+1],this._z=e[i+2],this._w=e[i+3],this._onChangeCallback(),this}toArray(e=[],i=0){return e[i]=this._x,e[i+1]=this._y,e[i+2]=this._z,e[i+3]=this._w,e}fromBufferAttribute(e,i){return this._x=e.getX(i),this._y=e.getY(i),this._z=e.getZ(i),this._w=e.getW(i),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}}class Q{constructor(e=0,i=0,r=0){Q.prototype.isVector3=!0,this.x=e,this.y=i,this.z=r}set(e,i,r){return r===void 0&&(r=this.z),this.x=e,this.y=i,this.z=r,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setComponent(e,i){switch(e){case 0:this.x=i;break;case 1:this.y=i;break;case 2:this.z=i;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this}addVectors(e,i){return this.x=e.x+i.x,this.y=e.y+i.y,this.z=e.z+i.z,this}addScaledVector(e,i){return this.x+=e.x*i,this.y+=e.y*i,this.z+=e.z*i,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this}subVectors(e,i){return this.x=e.x-i.x,this.y=e.y-i.y,this.z=e.z-i.z,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this}multiplyVectors(e,i){return this.x=e.x*i.x,this.y=e.y*i.y,this.z=e.z*i.z,this}applyEuler(e){return this.applyQuaternion(Ev.setFromEuler(e))}applyAxisAngle(e,i){return this.applyQuaternion(Ev.setFromAxisAngle(e,i))}applyMatrix3(e){const i=this.x,r=this.y,u=this.z,f=e.elements;return this.x=f[0]*i+f[3]*r+f[6]*u,this.y=f[1]*i+f[4]*r+f[7]*u,this.z=f[2]*i+f[5]*r+f[8]*u,this}applyNormalMatrix(e){return this.applyMatrix3(e).normalize()}applyMatrix4(e){const i=this.x,r=this.y,u=this.z,f=e.elements,h=1/(f[3]*i+f[7]*r+f[11]*u+f[15]);return this.x=(f[0]*i+f[4]*r+f[8]*u+f[12])*h,this.y=(f[1]*i+f[5]*r+f[9]*u+f[13])*h,this.z=(f[2]*i+f[6]*r+f[10]*u+f[14])*h,this}applyQuaternion(e){const i=this.x,r=this.y,u=this.z,f=e.x,h=e.y,d=e.z,p=e.w,g=2*(h*u-d*r),v=2*(d*i-f*u),_=2*(f*r-h*i);return this.x=i+p*g+h*_-d*v,this.y=r+p*v+d*g-f*_,this.z=u+p*_+f*v-h*g,this}project(e){return this.applyMatrix4(e.matrixWorldInverse).applyMatrix4(e.projectionMatrix)}unproject(e){return this.applyMatrix4(e.projectionMatrixInverse).applyMatrix4(e.matrixWorld)}transformDirection(e){const i=this.x,r=this.y,u=this.z,f=e.elements;return this.x=f[0]*i+f[4]*r+f[8]*u,this.y=f[1]*i+f[5]*r+f[9]*u,this.z=f[2]*i+f[6]*r+f[10]*u,this.normalize()}divide(e){return this.x/=e.x,this.y/=e.y,this.z/=e.z,this}divideScalar(e){return this.multiplyScalar(1/e)}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this}clamp(e,i){return this.x=Math.max(e.x,Math.min(i.x,this.x)),this.y=Math.max(e.y,Math.min(i.y,this.y)),this.z=Math.max(e.z,Math.min(i.z,this.z)),this}clampScalar(e,i){return this.x=Math.max(e,Math.min(i,this.x)),this.y=Math.max(e,Math.min(i,this.y)),this.z=Math.max(e,Math.min(i,this.z)),this}clampLength(e,i){const r=this.length();return this.divideScalar(r||1).multiplyScalar(Math.max(e,Math.min(i,r)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,i){return this.x+=(e.x-this.x)*i,this.y+=(e.y-this.y)*i,this.z+=(e.z-this.z)*i,this}lerpVectors(e,i,r){return this.x=e.x+(i.x-e.x)*r,this.y=e.y+(i.y-e.y)*r,this.z=e.z+(i.z-e.z)*r,this}cross(e){return this.crossVectors(this,e)}crossVectors(e,i){const r=e.x,u=e.y,f=e.z,h=i.x,d=i.y,p=i.z;return this.x=u*p-f*d,this.y=f*h-r*p,this.z=r*d-u*h,this}projectOnVector(e){const i=e.lengthSq();if(i===0)return this.set(0,0,0);const r=e.dot(this)/i;return this.copy(e).multiplyScalar(r)}projectOnPlane(e){return Sd.copy(this).projectOnVector(e),this.sub(Sd)}reflect(e){return this.sub(Sd.copy(e).multiplyScalar(2*this.dot(e)))}angleTo(e){const i=Math.sqrt(this.lengthSq()*e.lengthSq());if(i===0)return Math.PI/2;const r=this.dot(e)/i;return Math.acos(Fn(r,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){const i=this.x-e.x,r=this.y-e.y,u=this.z-e.z;return i*i+r*r+u*u}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)+Math.abs(this.z-e.z)}setFromSpherical(e){return this.setFromSphericalCoords(e.radius,e.phi,e.theta)}setFromSphericalCoords(e,i,r){const u=Math.sin(i)*e;return this.x=u*Math.sin(r),this.y=Math.cos(i)*e,this.z=u*Math.cos(r),this}setFromCylindrical(e){return this.setFromCylindricalCoords(e.radius,e.theta,e.y)}setFromCylindricalCoords(e,i,r){return this.x=e*Math.sin(i),this.y=r,this.z=e*Math.cos(i),this}setFromMatrixPosition(e){const i=e.elements;return this.x=i[12],this.y=i[13],this.z=i[14],this}setFromMatrixScale(e){const i=this.setFromMatrixColumn(e,0).length(),r=this.setFromMatrixColumn(e,1).length(),u=this.setFromMatrixColumn(e,2).length();return this.x=i,this.y=r,this.z=u,this}setFromMatrixColumn(e,i){return this.fromArray(e.elements,i*4)}setFromMatrix3Column(e,i){return this.fromArray(e.elements,i*3)}setFromEuler(e){return this.x=e._x,this.y=e._y,this.z=e._z,this}setFromColor(e){return this.x=e.r,this.y=e.g,this.z=e.b,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z}fromArray(e,i=0){return this.x=e[i],this.y=e[i+1],this.z=e[i+2],this}toArray(e=[],i=0){return e[i]=this.x,e[i+1]=this.y,e[i+2]=this.z,e}fromBufferAttribute(e,i){return this.x=e.getX(i),this.y=e.getY(i),this.z=e.getZ(i),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){const e=Math.random()*Math.PI*2,i=Math.random()*2-1,r=Math.sqrt(1-i*i);return this.x=r*Math.cos(e),this.y=i,this.z=r*Math.sin(e),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}}const Sd=new Q,Ev=new Ws;class vl{constructor(e=new Q(1/0,1/0,1/0),i=new Q(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=e,this.max=i}set(e,i){return this.min.copy(e),this.max.copy(i),this}setFromArray(e){this.makeEmpty();for(let i=0,r=e.length;i<r;i+=3)this.expandByPoint(Di.fromArray(e,i));return this}setFromBufferAttribute(e){this.makeEmpty();for(let i=0,r=e.count;i<r;i++)this.expandByPoint(Di.fromBufferAttribute(e,i));return this}setFromPoints(e){this.makeEmpty();for(let i=0,r=e.length;i<r;i++)this.expandByPoint(e[i]);return this}setFromCenterAndSize(e,i){const r=Di.copy(i).multiplyScalar(.5);return this.min.copy(e).sub(r),this.max.copy(e).add(r),this}setFromObject(e,i=!1){return this.makeEmpty(),this.expandByObject(e,i)}clone(){return new this.constructor().copy(this)}copy(e){return this.min.copy(e.min),this.max.copy(e.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(e){return this.isEmpty()?e.set(0,0,0):e.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(e){return this.isEmpty()?e.set(0,0,0):e.subVectors(this.max,this.min)}expandByPoint(e){return this.min.min(e),this.max.max(e),this}expandByVector(e){return this.min.sub(e),this.max.add(e),this}expandByScalar(e){return this.min.addScalar(-e),this.max.addScalar(e),this}expandByObject(e,i=!1){e.updateWorldMatrix(!1,!1);const r=e.geometry;if(r!==void 0){const f=r.getAttribute("position");if(i===!0&&f!==void 0&&e.isInstancedMesh!==!0)for(let h=0,d=f.count;h<d;h++)e.isMesh===!0?e.getVertexPosition(h,Di):Di.fromBufferAttribute(f,h),Di.applyMatrix4(e.matrixWorld),this.expandByPoint(Di);else e.boundingBox!==void 0?(e.boundingBox===null&&e.computeBoundingBox(),ku.copy(e.boundingBox)):(r.boundingBox===null&&r.computeBoundingBox(),ku.copy(r.boundingBox)),ku.applyMatrix4(e.matrixWorld),this.union(ku)}const u=e.children;for(let f=0,h=u.length;f<h;f++)this.expandByObject(u[f],i);return this}containsPoint(e){return e.x>=this.min.x&&e.x<=this.max.x&&e.y>=this.min.y&&e.y<=this.max.y&&e.z>=this.min.z&&e.z<=this.max.z}containsBox(e){return this.min.x<=e.min.x&&e.max.x<=this.max.x&&this.min.y<=e.min.y&&e.max.y<=this.max.y&&this.min.z<=e.min.z&&e.max.z<=this.max.z}getParameter(e,i){return i.set((e.x-this.min.x)/(this.max.x-this.min.x),(e.y-this.min.y)/(this.max.y-this.min.y),(e.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(e){return e.max.x>=this.min.x&&e.min.x<=this.max.x&&e.max.y>=this.min.y&&e.min.y<=this.max.y&&e.max.z>=this.min.z&&e.min.z<=this.max.z}intersectsSphere(e){return this.clampPoint(e.center,Di),Di.distanceToSquared(e.center)<=e.radius*e.radius}intersectsPlane(e){let i,r;return e.normal.x>0?(i=e.normal.x*this.min.x,r=e.normal.x*this.max.x):(i=e.normal.x*this.max.x,r=e.normal.x*this.min.x),e.normal.y>0?(i+=e.normal.y*this.min.y,r+=e.normal.y*this.max.y):(i+=e.normal.y*this.max.y,r+=e.normal.y*this.min.y),e.normal.z>0?(i+=e.normal.z*this.min.z,r+=e.normal.z*this.max.z):(i+=e.normal.z*this.max.z,r+=e.normal.z*this.min.z),i<=-e.constant&&r>=-e.constant}intersectsTriangle(e){if(this.isEmpty())return!1;this.getCenter(rl),qu.subVectors(this.max,rl),Fr.subVectors(e.a,rl),Hr.subVectors(e.b,rl),Gr.subVectors(e.c,rl),Ja.subVectors(Hr,Fr),$a.subVectors(Gr,Hr),Os.subVectors(Fr,Gr);let i=[0,-Ja.z,Ja.y,0,-$a.z,$a.y,0,-Os.z,Os.y,Ja.z,0,-Ja.x,$a.z,0,-$a.x,Os.z,0,-Os.x,-Ja.y,Ja.x,0,-$a.y,$a.x,0,-Os.y,Os.x,0];return!yd(i,Fr,Hr,Gr,qu)||(i=[1,0,0,0,1,0,0,0,1],!yd(i,Fr,Hr,Gr,qu))?!1:(Wu.crossVectors(Ja,$a),i=[Wu.x,Wu.y,Wu.z],yd(i,Fr,Hr,Gr,qu))}clampPoint(e,i){return i.copy(e).clamp(this.min,this.max)}distanceToPoint(e){return this.clampPoint(e,Di).distanceTo(e)}getBoundingSphere(e){return this.isEmpty()?e.makeEmpty():(this.getCenter(e.center),e.radius=this.getSize(Di).length()*.5),e}intersect(e){return this.min.max(e.min),this.max.min(e.max),this.isEmpty()&&this.makeEmpty(),this}union(e){return this.min.min(e.min),this.max.max(e.max),this}applyMatrix4(e){return this.isEmpty()?this:(ma[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(e),ma[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(e),ma[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(e),ma[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(e),ma[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(e),ma[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(e),ma[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(e),ma[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(e),this.setFromPoints(ma),this)}translate(e){return this.min.add(e),this.max.add(e),this}equals(e){return e.min.equals(this.min)&&e.max.equals(this.max)}}const ma=[new Q,new Q,new Q,new Q,new Q,new Q,new Q,new Q],Di=new Q,ku=new vl,Fr=new Q,Hr=new Q,Gr=new Q,Ja=new Q,$a=new Q,Os=new Q,rl=new Q,qu=new Q,Wu=new Q,Ps=new Q;function yd(o,e,i,r,u){for(let f=0,h=o.length-3;f<=h;f+=3){Ps.fromArray(o,f);const d=u.x*Math.abs(Ps.x)+u.y*Math.abs(Ps.y)+u.z*Math.abs(Ps.z),p=e.dot(Ps),g=i.dot(Ps),v=r.dot(Ps);if(Math.max(-Math.max(p,g,v),Math.min(p,g,v))>d)return!1}return!0}const XE=new vl,ol=new Q,xd=new Q;class Lc{constructor(e=new Q,i=-1){this.isSphere=!0,this.center=e,this.radius=i}set(e,i){return this.center.copy(e),this.radius=i,this}setFromPoints(e,i){const r=this.center;i!==void 0?r.copy(i):XE.setFromPoints(e).getCenter(r);let u=0;for(let f=0,h=e.length;f<h;f++)u=Math.max(u,r.distanceToSquared(e[f]));return this.radius=Math.sqrt(u),this}copy(e){return this.center.copy(e.center),this.radius=e.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(e){return e.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(e){return e.distanceTo(this.center)-this.radius}intersectsSphere(e){const i=this.radius+e.radius;return e.center.distanceToSquared(this.center)<=i*i}intersectsBox(e){return e.intersectsSphere(this)}intersectsPlane(e){return Math.abs(e.distanceToPoint(this.center))<=this.radius}clampPoint(e,i){const r=this.center.distanceToSquared(e);return i.copy(e),r>this.radius*this.radius&&(i.sub(this.center).normalize(),i.multiplyScalar(this.radius).add(this.center)),i}getBoundingBox(e){return this.isEmpty()?(e.makeEmpty(),e):(e.set(this.center,this.center),e.expandByScalar(this.radius),e)}applyMatrix4(e){return this.center.applyMatrix4(e),this.radius=this.radius*e.getMaxScaleOnAxis(),this}translate(e){return this.center.add(e),this}expandByPoint(e){if(this.isEmpty())return this.center.copy(e),this.radius=0,this;ol.subVectors(e,this.center);const i=ol.lengthSq();if(i>this.radius*this.radius){const r=Math.sqrt(i),u=(r-this.radius)*.5;this.center.addScaledVector(ol,u/r),this.radius+=u}return this}union(e){return e.isEmpty()?this:this.isEmpty()?(this.copy(e),this):(this.center.equals(e.center)===!0?this.radius=Math.max(this.radius,e.radius):(xd.subVectors(e.center,this.center).setLength(e.radius),this.expandByPoint(ol.copy(e.center).add(xd)),this.expandByPoint(ol.copy(e.center).sub(xd))),this)}equals(e){return e.center.equals(this.center)&&e.radius===this.radius}clone(){return new this.constructor().copy(this)}}const _a=new Q,Md=new Q,ju=new Q,ts=new Q,Ed=new Q,Zu=new Q,Td=new Q;class Xp{constructor(e=new Q,i=new Q(0,0,-1)){this.origin=e,this.direction=i}set(e,i){return this.origin.copy(e),this.direction.copy(i),this}copy(e){return this.origin.copy(e.origin),this.direction.copy(e.direction),this}at(e,i){return i.copy(this.origin).addScaledVector(this.direction,e)}lookAt(e){return this.direction.copy(e).sub(this.origin).normalize(),this}recast(e){return this.origin.copy(this.at(e,_a)),this}closestPointToPoint(e,i){i.subVectors(e,this.origin);const r=i.dot(this.direction);return r<0?i.copy(this.origin):i.copy(this.origin).addScaledVector(this.direction,r)}distanceToPoint(e){return Math.sqrt(this.distanceSqToPoint(e))}distanceSqToPoint(e){const i=_a.subVectors(e,this.origin).dot(this.direction);return i<0?this.origin.distanceToSquared(e):(_a.copy(this.origin).addScaledVector(this.direction,i),_a.distanceToSquared(e))}distanceSqToSegment(e,i,r,u){Md.copy(e).add(i).multiplyScalar(.5),ju.copy(i).sub(e).normalize(),ts.copy(this.origin).sub(Md);const f=e.distanceTo(i)*.5,h=-this.direction.dot(ju),d=ts.dot(this.direction),p=-ts.dot(ju),g=ts.lengthSq(),v=Math.abs(1-h*h);let _,y,M,E;if(v>0)if(_=h*p-d,y=h*d-p,E=f*v,_>=0)if(y>=-E)if(y<=E){const R=1/v;_*=R,y*=R,M=_*(_+h*y+2*d)+y*(h*_+y+2*p)+g}else y=f,_=Math.max(0,-(h*y+d)),M=-_*_+y*(y+2*p)+g;else y=-f,_=Math.max(0,-(h*y+d)),M=-_*_+y*(y+2*p)+g;else y<=-E?(_=Math.max(0,-(-h*f+d)),y=_>0?-f:Math.min(Math.max(-f,-p),f),M=-_*_+y*(y+2*p)+g):y<=E?(_=0,y=Math.min(Math.max(-f,-p),f),M=y*(y+2*p)+g):(_=Math.max(0,-(h*f+d)),y=_>0?f:Math.min(Math.max(-f,-p),f),M=-_*_+y*(y+2*p)+g);else y=h>0?-f:f,_=Math.max(0,-(h*y+d)),M=-_*_+y*(y+2*p)+g;return r&&r.copy(this.origin).addScaledVector(this.direction,_),u&&u.copy(Md).addScaledVector(ju,y),M}intersectSphere(e,i){_a.subVectors(e.center,this.origin);const r=_a.dot(this.direction),u=_a.dot(_a)-r*r,f=e.radius*e.radius;if(u>f)return null;const h=Math.sqrt(f-u),d=r-h,p=r+h;return p<0?null:d<0?this.at(p,i):this.at(d,i)}intersectsSphere(e){return this.distanceSqToPoint(e.center)<=e.radius*e.radius}distanceToPlane(e){const i=e.normal.dot(this.direction);if(i===0)return e.distanceToPoint(this.origin)===0?0:null;const r=-(this.origin.dot(e.normal)+e.constant)/i;return r>=0?r:null}intersectPlane(e,i){const r=this.distanceToPlane(e);return r===null?null:this.at(r,i)}intersectsPlane(e){const i=e.distanceToPoint(this.origin);return i===0||e.normal.dot(this.direction)*i<0}intersectBox(e,i){let r,u,f,h,d,p;const g=1/this.direction.x,v=1/this.direction.y,_=1/this.direction.z,y=this.origin;return g>=0?(r=(e.min.x-y.x)*g,u=(e.max.x-y.x)*g):(r=(e.max.x-y.x)*g,u=(e.min.x-y.x)*g),v>=0?(f=(e.min.y-y.y)*v,h=(e.max.y-y.y)*v):(f=(e.max.y-y.y)*v,h=(e.min.y-y.y)*v),r>h||f>u||((f>r||isNaN(r))&&(r=f),(h<u||isNaN(u))&&(u=h),_>=0?(d=(e.min.z-y.z)*_,p=(e.max.z-y.z)*_):(d=(e.max.z-y.z)*_,p=(e.min.z-y.z)*_),r>p||d>u)||((d>r||r!==r)&&(r=d),(p<u||u!==u)&&(u=p),u<0)?null:this.at(r>=0?r:u,i)}intersectsBox(e){return this.intersectBox(e,_a)!==null}intersectTriangle(e,i,r,u,f){Ed.subVectors(i,e),Zu.subVectors(r,e),Td.crossVectors(Ed,Zu);let h=this.direction.dot(Td),d;if(h>0){if(u)return null;d=1}else if(h<0)d=-1,h=-h;else return null;ts.subVectors(this.origin,e);const p=d*this.direction.dot(Zu.crossVectors(ts,Zu));if(p<0)return null;const g=d*this.direction.dot(Ed.cross(ts));if(g<0||p+g>h)return null;const v=-d*ts.dot(Td);return v<0?null:this.at(v/h,f)}applyMatrix4(e){return this.origin.applyMatrix4(e),this.direction.transformDirection(e),this}equals(e){return e.origin.equals(this.origin)&&e.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}}class Ze{constructor(e,i,r,u,f,h,d,p,g,v,_,y,M,E,R,x){Ze.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],e!==void 0&&this.set(e,i,r,u,f,h,d,p,g,v,_,y,M,E,R,x)}set(e,i,r,u,f,h,d,p,g,v,_,y,M,E,R,x){const S=this.elements;return S[0]=e,S[4]=i,S[8]=r,S[12]=u,S[1]=f,S[5]=h,S[9]=d,S[13]=p,S[2]=g,S[6]=v,S[10]=_,S[14]=y,S[3]=M,S[7]=E,S[11]=R,S[15]=x,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new Ze().fromArray(this.elements)}copy(e){const i=this.elements,r=e.elements;return i[0]=r[0],i[1]=r[1],i[2]=r[2],i[3]=r[3],i[4]=r[4],i[5]=r[5],i[6]=r[6],i[7]=r[7],i[8]=r[8],i[9]=r[9],i[10]=r[10],i[11]=r[11],i[12]=r[12],i[13]=r[13],i[14]=r[14],i[15]=r[15],this}copyPosition(e){const i=this.elements,r=e.elements;return i[12]=r[12],i[13]=r[13],i[14]=r[14],this}setFromMatrix3(e){const i=e.elements;return this.set(i[0],i[3],i[6],0,i[1],i[4],i[7],0,i[2],i[5],i[8],0,0,0,0,1),this}extractBasis(e,i,r){return e.setFromMatrixColumn(this,0),i.setFromMatrixColumn(this,1),r.setFromMatrixColumn(this,2),this}makeBasis(e,i,r){return this.set(e.x,i.x,r.x,0,e.y,i.y,r.y,0,e.z,i.z,r.z,0,0,0,0,1),this}extractRotation(e){const i=this.elements,r=e.elements,u=1/Vr.setFromMatrixColumn(e,0).length(),f=1/Vr.setFromMatrixColumn(e,1).length(),h=1/Vr.setFromMatrixColumn(e,2).length();return i[0]=r[0]*u,i[1]=r[1]*u,i[2]=r[2]*u,i[3]=0,i[4]=r[4]*f,i[5]=r[5]*f,i[6]=r[6]*f,i[7]=0,i[8]=r[8]*h,i[9]=r[9]*h,i[10]=r[10]*h,i[11]=0,i[12]=0,i[13]=0,i[14]=0,i[15]=1,this}makeRotationFromEuler(e){const i=this.elements,r=e.x,u=e.y,f=e.z,h=Math.cos(r),d=Math.sin(r),p=Math.cos(u),g=Math.sin(u),v=Math.cos(f),_=Math.sin(f);if(e.order==="XYZ"){const y=h*v,M=h*_,E=d*v,R=d*_;i[0]=p*v,i[4]=-p*_,i[8]=g,i[1]=M+E*g,i[5]=y-R*g,i[9]=-d*p,i[2]=R-y*g,i[6]=E+M*g,i[10]=h*p}else if(e.order==="YXZ"){const y=p*v,M=p*_,E=g*v,R=g*_;i[0]=y+R*d,i[4]=E*d-M,i[8]=h*g,i[1]=h*_,i[5]=h*v,i[9]=-d,i[2]=M*d-E,i[6]=R+y*d,i[10]=h*p}else if(e.order==="ZXY"){const y=p*v,M=p*_,E=g*v,R=g*_;i[0]=y-R*d,i[4]=-h*_,i[8]=E+M*d,i[1]=M+E*d,i[5]=h*v,i[9]=R-y*d,i[2]=-h*g,i[6]=d,i[10]=h*p}else if(e.order==="ZYX"){const y=h*v,M=h*_,E=d*v,R=d*_;i[0]=p*v,i[4]=E*g-M,i[8]=y*g+R,i[1]=p*_,i[5]=R*g+y,i[9]=M*g-E,i[2]=-g,i[6]=d*p,i[10]=h*p}else if(e.order==="YZX"){const y=h*p,M=h*g,E=d*p,R=d*g;i[0]=p*v,i[4]=R-y*_,i[8]=E*_+M,i[1]=_,i[5]=h*v,i[9]=-d*v,i[2]=-g*v,i[6]=M*_+E,i[10]=y-R*_}else if(e.order==="XZY"){const y=h*p,M=h*g,E=d*p,R=d*g;i[0]=p*v,i[4]=-_,i[8]=g*v,i[1]=y*_+R,i[5]=h*v,i[9]=M*_-E,i[2]=E*_-M,i[6]=d*v,i[10]=R*_+y}return i[3]=0,i[7]=0,i[11]=0,i[12]=0,i[13]=0,i[14]=0,i[15]=1,this}makeRotationFromQuaternion(e){return this.compose(YE,e,kE)}lookAt(e,i,r){const u=this.elements;return ri.subVectors(e,i),ri.lengthSq()===0&&(ri.z=1),ri.normalize(),es.crossVectors(r,ri),es.lengthSq()===0&&(Math.abs(r.z)===1?ri.x+=1e-4:ri.z+=1e-4,ri.normalize(),es.crossVectors(r,ri)),es.normalize(),Ku.crossVectors(ri,es),u[0]=es.x,u[4]=Ku.x,u[8]=ri.x,u[1]=es.y,u[5]=Ku.y,u[9]=ri.y,u[2]=es.z,u[6]=Ku.z,u[10]=ri.z,this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,i){const r=e.elements,u=i.elements,f=this.elements,h=r[0],d=r[4],p=r[8],g=r[12],v=r[1],_=r[5],y=r[9],M=r[13],E=r[2],R=r[6],x=r[10],S=r[14],L=r[3],U=r[7],P=r[11],J=r[15],B=u[0],O=u[4],V=u[8],gt=u[12],T=u[1],w=u[5],nt=u[9],rt=u[13],lt=u[2],ft=u[6],H=u[10],at=u[14],Z=u[3],yt=u[7],St=u[11],Pt=u[15];return f[0]=h*B+d*T+p*lt+g*Z,f[4]=h*O+d*w+p*ft+g*yt,f[8]=h*V+d*nt+p*H+g*St,f[12]=h*gt+d*rt+p*at+g*Pt,f[1]=v*B+_*T+y*lt+M*Z,f[5]=v*O+_*w+y*ft+M*yt,f[9]=v*V+_*nt+y*H+M*St,f[13]=v*gt+_*rt+y*at+M*Pt,f[2]=E*B+R*T+x*lt+S*Z,f[6]=E*O+R*w+x*ft+S*yt,f[10]=E*V+R*nt+x*H+S*St,f[14]=E*gt+R*rt+x*at+S*Pt,f[3]=L*B+U*T+P*lt+J*Z,f[7]=L*O+U*w+P*ft+J*yt,f[11]=L*V+U*nt+P*H+J*St,f[15]=L*gt+U*rt+P*at+J*Pt,this}multiplyScalar(e){const i=this.elements;return i[0]*=e,i[4]*=e,i[8]*=e,i[12]*=e,i[1]*=e,i[5]*=e,i[9]*=e,i[13]*=e,i[2]*=e,i[6]*=e,i[10]*=e,i[14]*=e,i[3]*=e,i[7]*=e,i[11]*=e,i[15]*=e,this}determinant(){const e=this.elements,i=e[0],r=e[4],u=e[8],f=e[12],h=e[1],d=e[5],p=e[9],g=e[13],v=e[2],_=e[6],y=e[10],M=e[14],E=e[3],R=e[7],x=e[11],S=e[15];return E*(+f*p*_-u*g*_-f*d*y+r*g*y+u*d*M-r*p*M)+R*(+i*p*M-i*g*y+f*h*y-u*h*M+u*g*v-f*p*v)+x*(+i*g*_-i*d*M-f*h*_+r*h*M+f*d*v-r*g*v)+S*(-u*d*v-i*p*_+i*d*y+u*h*_-r*h*y+r*p*v)}transpose(){const e=this.elements;let i;return i=e[1],e[1]=e[4],e[4]=i,i=e[2],e[2]=e[8],e[8]=i,i=e[6],e[6]=e[9],e[9]=i,i=e[3],e[3]=e[12],e[12]=i,i=e[7],e[7]=e[13],e[13]=i,i=e[11],e[11]=e[14],e[14]=i,this}setPosition(e,i,r){const u=this.elements;return e.isVector3?(u[12]=e.x,u[13]=e.y,u[14]=e.z):(u[12]=e,u[13]=i,u[14]=r),this}invert(){const e=this.elements,i=e[0],r=e[1],u=e[2],f=e[3],h=e[4],d=e[5],p=e[6],g=e[7],v=e[8],_=e[9],y=e[10],M=e[11],E=e[12],R=e[13],x=e[14],S=e[15],L=_*x*g-R*y*g+R*p*M-d*x*M-_*p*S+d*y*S,U=E*y*g-v*x*g-E*p*M+h*x*M+v*p*S-h*y*S,P=v*R*g-E*_*g+E*d*M-h*R*M-v*d*S+h*_*S,J=E*_*p-v*R*p-E*d*y+h*R*y+v*d*x-h*_*x,B=i*L+r*U+u*P+f*J;if(B===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);const O=1/B;return e[0]=L*O,e[1]=(R*y*f-_*x*f-R*u*M+r*x*M+_*u*S-r*y*S)*O,e[2]=(d*x*f-R*p*f+R*u*g-r*x*g-d*u*S+r*p*S)*O,e[3]=(_*p*f-d*y*f-_*u*g+r*y*g+d*u*M-r*p*M)*O,e[4]=U*O,e[5]=(v*x*f-E*y*f+E*u*M-i*x*M-v*u*S+i*y*S)*O,e[6]=(E*p*f-h*x*f-E*u*g+i*x*g+h*u*S-i*p*S)*O,e[7]=(h*y*f-v*p*f+v*u*g-i*y*g-h*u*M+i*p*M)*O,e[8]=P*O,e[9]=(E*_*f-v*R*f-E*r*M+i*R*M+v*r*S-i*_*S)*O,e[10]=(h*R*f-E*d*f+E*r*g-i*R*g-h*r*S+i*d*S)*O,e[11]=(v*d*f-h*_*f-v*r*g+i*_*g+h*r*M-i*d*M)*O,e[12]=J*O,e[13]=(v*R*u-E*_*u+E*r*y-i*R*y-v*r*x+i*_*x)*O,e[14]=(E*d*u-h*R*u-E*r*p+i*R*p+h*r*x-i*d*x)*O,e[15]=(h*_*u-v*d*u+v*r*p-i*_*p-h*r*y+i*d*y)*O,this}scale(e){const i=this.elements,r=e.x,u=e.y,f=e.z;return i[0]*=r,i[4]*=u,i[8]*=f,i[1]*=r,i[5]*=u,i[9]*=f,i[2]*=r,i[6]*=u,i[10]*=f,i[3]*=r,i[7]*=u,i[11]*=f,this}getMaxScaleOnAxis(){const e=this.elements,i=e[0]*e[0]+e[1]*e[1]+e[2]*e[2],r=e[4]*e[4]+e[5]*e[5]+e[6]*e[6],u=e[8]*e[8]+e[9]*e[9]+e[10]*e[10];return Math.sqrt(Math.max(i,r,u))}makeTranslation(e,i,r){return e.isVector3?this.set(1,0,0,e.x,0,1,0,e.y,0,0,1,e.z,0,0,0,1):this.set(1,0,0,e,0,1,0,i,0,0,1,r,0,0,0,1),this}makeRotationX(e){const i=Math.cos(e),r=Math.sin(e);return this.set(1,0,0,0,0,i,-r,0,0,r,i,0,0,0,0,1),this}makeRotationY(e){const i=Math.cos(e),r=Math.sin(e);return this.set(i,0,r,0,0,1,0,0,-r,0,i,0,0,0,0,1),this}makeRotationZ(e){const i=Math.cos(e),r=Math.sin(e);return this.set(i,-r,0,0,r,i,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(e,i){const r=Math.cos(i),u=Math.sin(i),f=1-r,h=e.x,d=e.y,p=e.z,g=f*h,v=f*d;return this.set(g*h+r,g*d-u*p,g*p+u*d,0,g*d+u*p,v*d+r,v*p-u*h,0,g*p-u*d,v*p+u*h,f*p*p+r,0,0,0,0,1),this}makeScale(e,i,r){return this.set(e,0,0,0,0,i,0,0,0,0,r,0,0,0,0,1),this}makeShear(e,i,r,u,f,h){return this.set(1,r,f,0,e,1,h,0,i,u,1,0,0,0,0,1),this}compose(e,i,r){const u=this.elements,f=i._x,h=i._y,d=i._z,p=i._w,g=f+f,v=h+h,_=d+d,y=f*g,M=f*v,E=f*_,R=h*v,x=h*_,S=d*_,L=p*g,U=p*v,P=p*_,J=r.x,B=r.y,O=r.z;return u[0]=(1-(R+S))*J,u[1]=(M+P)*J,u[2]=(E-U)*J,u[3]=0,u[4]=(M-P)*B,u[5]=(1-(y+S))*B,u[6]=(x+L)*B,u[7]=0,u[8]=(E+U)*O,u[9]=(x-L)*O,u[10]=(1-(y+R))*O,u[11]=0,u[12]=e.x,u[13]=e.y,u[14]=e.z,u[15]=1,this}decompose(e,i,r){const u=this.elements;let f=Vr.set(u[0],u[1],u[2]).length();const h=Vr.set(u[4],u[5],u[6]).length(),d=Vr.set(u[8],u[9],u[10]).length();this.determinant()<0&&(f=-f),e.x=u[12],e.y=u[13],e.z=u[14],Ui.copy(this);const g=1/f,v=1/h,_=1/d;return Ui.elements[0]*=g,Ui.elements[1]*=g,Ui.elements[2]*=g,Ui.elements[4]*=v,Ui.elements[5]*=v,Ui.elements[6]*=v,Ui.elements[8]*=_,Ui.elements[9]*=_,Ui.elements[10]*=_,i.setFromRotationMatrix(Ui),r.x=f,r.y=h,r.z=d,this}makePerspective(e,i,r,u,f,h,d=Ma){const p=this.elements,g=2*f/(i-e),v=2*f/(r-u),_=(i+e)/(i-e),y=(r+u)/(r-u);let M,E;if(d===Ma)M=-(h+f)/(h-f),E=-2*h*f/(h-f);else if(d===Rc)M=-h/(h-f),E=-h*f/(h-f);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+d);return p[0]=g,p[4]=0,p[8]=_,p[12]=0,p[1]=0,p[5]=v,p[9]=y,p[13]=0,p[2]=0,p[6]=0,p[10]=M,p[14]=E,p[3]=0,p[7]=0,p[11]=-1,p[15]=0,this}makeOrthographic(e,i,r,u,f,h,d=Ma){const p=this.elements,g=1/(i-e),v=1/(r-u),_=1/(h-f),y=(i+e)*g,M=(r+u)*v;let E,R;if(d===Ma)E=(h+f)*_,R=-2*_;else if(d===Rc)E=f*_,R=-1*_;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+d);return p[0]=2*g,p[4]=0,p[8]=0,p[12]=-y,p[1]=0,p[5]=2*v,p[9]=0,p[13]=-M,p[2]=0,p[6]=0,p[10]=R,p[14]=-E,p[3]=0,p[7]=0,p[11]=0,p[15]=1,this}equals(e){const i=this.elements,r=e.elements;for(let u=0;u<16;u++)if(i[u]!==r[u])return!1;return!0}fromArray(e,i=0){for(let r=0;r<16;r++)this.elements[r]=e[r+i];return this}toArray(e=[],i=0){const r=this.elements;return e[i]=r[0],e[i+1]=r[1],e[i+2]=r[2],e[i+3]=r[3],e[i+4]=r[4],e[i+5]=r[5],e[i+6]=r[6],e[i+7]=r[7],e[i+8]=r[8],e[i+9]=r[9],e[i+10]=r[10],e[i+11]=r[11],e[i+12]=r[12],e[i+13]=r[13],e[i+14]=r[14],e[i+15]=r[15],e}}const Vr=new Q,Ui=new Ze,YE=new Q(0,0,0),kE=new Q(1,1,1),es=new Q,Ku=new Q,ri=new Q,Tv=new Ze,bv=new Ws;class Ta{constructor(e=0,i=0,r=0,u=Ta.DEFAULT_ORDER){this.isEuler=!0,this._x=e,this._y=i,this._z=r,this._order=u}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get order(){return this._order}set order(e){this._order=e,this._onChangeCallback()}set(e,i,r,u=this._order){return this._x=e,this._y=i,this._z=r,this._order=u,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(e){return this._x=e._x,this._y=e._y,this._z=e._z,this._order=e._order,this._onChangeCallback(),this}setFromRotationMatrix(e,i=this._order,r=!0){const u=e.elements,f=u[0],h=u[4],d=u[8],p=u[1],g=u[5],v=u[9],_=u[2],y=u[6],M=u[10];switch(i){case"XYZ":this._y=Math.asin(Fn(d,-1,1)),Math.abs(d)<.9999999?(this._x=Math.atan2(-v,M),this._z=Math.atan2(-h,f)):(this._x=Math.atan2(y,g),this._z=0);break;case"YXZ":this._x=Math.asin(-Fn(v,-1,1)),Math.abs(v)<.9999999?(this._y=Math.atan2(d,M),this._z=Math.atan2(p,g)):(this._y=Math.atan2(-_,f),this._z=0);break;case"ZXY":this._x=Math.asin(Fn(y,-1,1)),Math.abs(y)<.9999999?(this._y=Math.atan2(-_,M),this._z=Math.atan2(-h,g)):(this._y=0,this._z=Math.atan2(p,f));break;case"ZYX":this._y=Math.asin(-Fn(_,-1,1)),Math.abs(_)<.9999999?(this._x=Math.atan2(y,M),this._z=Math.atan2(p,f)):(this._x=0,this._z=Math.atan2(-h,g));break;case"YZX":this._z=Math.asin(Fn(p,-1,1)),Math.abs(p)<.9999999?(this._x=Math.atan2(-v,g),this._y=Math.atan2(-_,f)):(this._x=0,this._y=Math.atan2(d,M));break;case"XZY":this._z=Math.asin(-Fn(h,-1,1)),Math.abs(h)<.9999999?(this._x=Math.atan2(y,g),this._y=Math.atan2(d,f)):(this._x=Math.atan2(-v,M),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+i)}return this._order=i,r===!0&&this._onChangeCallback(),this}setFromQuaternion(e,i,r){return Tv.makeRotationFromQuaternion(e),this.setFromRotationMatrix(Tv,i,r)}setFromVector3(e,i=this._order){return this.set(e.x,e.y,e.z,i)}reorder(e){return bv.setFromEuler(this),this.setFromQuaternion(bv,e)}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._order===this._order}fromArray(e){return this._x=e[0],this._y=e[1],this._z=e[2],e[3]!==void 0&&(this._order=e[3]),this._onChangeCallback(),this}toArray(e=[],i=0){return e[i]=this._x,e[i+1]=this._y,e[i+2]=this._z,e[i+3]=this._order,e}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}}Ta.DEFAULT_ORDER="XYZ";class LS{constructor(){this.mask=1}set(e){this.mask=(1<<e|0)>>>0}enable(e){this.mask|=1<<e|0}enableAll(){this.mask=-1}toggle(e){this.mask^=1<<e|0}disable(e){this.mask&=~(1<<e|0)}disableAll(){this.mask=0}test(e){return(this.mask&e.mask)!==0}isEnabled(e){return(this.mask&(1<<e|0))!==0}}let qE=0;const Av=new Q,Xr=new Ws,ga=new Ze,Qu=new Q,ll=new Q,WE=new Q,jE=new Ws,Rv=new Q(1,0,0),Cv=new Q(0,1,0),wv=new Q(0,0,1),Dv={type:"added"},ZE={type:"removed"},Yr={type:"childadded",child:null},bd={type:"childremoved",child:null};class bn extends Zs{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:qE++}),this.uuid=gl(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=bn.DEFAULT_UP.clone();const e=new Q,i=new Ta,r=new Ws,u=new Q(1,1,1);function f(){r.setFromEuler(i,!1)}function h(){i.setFromQuaternion(r,void 0,!1)}i._onChange(f),r._onChange(h),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:e},rotation:{configurable:!0,enumerable:!0,value:i},quaternion:{configurable:!0,enumerable:!0,value:r},scale:{configurable:!0,enumerable:!0,value:u},modelViewMatrix:{value:new Ze},normalMatrix:{value:new he}}),this.matrix=new Ze,this.matrixWorld=new Ze,this.matrixAutoUpdate=bn.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=bn.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new LS,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(e){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(e),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(e){return this.quaternion.premultiply(e),this}setRotationFromAxisAngle(e,i){this.quaternion.setFromAxisAngle(e,i)}setRotationFromEuler(e){this.quaternion.setFromEuler(e,!0)}setRotationFromMatrix(e){this.quaternion.setFromRotationMatrix(e)}setRotationFromQuaternion(e){this.quaternion.copy(e)}rotateOnAxis(e,i){return Xr.setFromAxisAngle(e,i),this.quaternion.multiply(Xr),this}rotateOnWorldAxis(e,i){return Xr.setFromAxisAngle(e,i),this.quaternion.premultiply(Xr),this}rotateX(e){return this.rotateOnAxis(Rv,e)}rotateY(e){return this.rotateOnAxis(Cv,e)}rotateZ(e){return this.rotateOnAxis(wv,e)}translateOnAxis(e,i){return Av.copy(e).applyQuaternion(this.quaternion),this.position.add(Av.multiplyScalar(i)),this}translateX(e){return this.translateOnAxis(Rv,e)}translateY(e){return this.translateOnAxis(Cv,e)}translateZ(e){return this.translateOnAxis(wv,e)}localToWorld(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(this.matrixWorld)}worldToLocal(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(ga.copy(this.matrixWorld).invert())}lookAt(e,i,r){e.isVector3?Qu.copy(e):Qu.set(e,i,r);const u=this.parent;this.updateWorldMatrix(!0,!1),ll.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?ga.lookAt(ll,Qu,this.up):ga.lookAt(Qu,ll,this.up),this.quaternion.setFromRotationMatrix(ga),u&&(ga.extractRotation(u.matrixWorld),Xr.setFromRotationMatrix(ga),this.quaternion.premultiply(Xr.invert()))}add(e){if(arguments.length>1){for(let i=0;i<arguments.length;i++)this.add(arguments[i]);return this}return e===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",e),this):(e&&e.isObject3D?(e.removeFromParent(),e.parent=this,this.children.push(e),e.dispatchEvent(Dv),Yr.child=e,this.dispatchEvent(Yr),Yr.child=null):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",e),this)}remove(e){if(arguments.length>1){for(let r=0;r<arguments.length;r++)this.remove(arguments[r]);return this}const i=this.children.indexOf(e);return i!==-1&&(e.parent=null,this.children.splice(i,1),e.dispatchEvent(ZE),bd.child=e,this.dispatchEvent(bd),bd.child=null),this}removeFromParent(){const e=this.parent;return e!==null&&e.remove(this),this}clear(){return this.remove(...this.children)}attach(e){return this.updateWorldMatrix(!0,!1),ga.copy(this.matrixWorld).invert(),e.parent!==null&&(e.parent.updateWorldMatrix(!0,!1),ga.multiply(e.parent.matrixWorld)),e.applyMatrix4(ga),e.removeFromParent(),e.parent=this,this.children.push(e),e.updateWorldMatrix(!1,!0),e.dispatchEvent(Dv),Yr.child=e,this.dispatchEvent(Yr),Yr.child=null,this}getObjectById(e){return this.getObjectByProperty("id",e)}getObjectByName(e){return this.getObjectByProperty("name",e)}getObjectByProperty(e,i){if(this[e]===i)return this;for(let r=0,u=this.children.length;r<u;r++){const h=this.children[r].getObjectByProperty(e,i);if(h!==void 0)return h}}getObjectsByProperty(e,i,r=[]){this[e]===i&&r.push(this);const u=this.children;for(let f=0,h=u.length;f<h;f++)u[f].getObjectsByProperty(e,i,r);return r}getWorldPosition(e){return this.updateWorldMatrix(!0,!1),e.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(ll,e,WE),e}getWorldScale(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(ll,jE,e),e}getWorldDirection(e){this.updateWorldMatrix(!0,!1);const i=this.matrixWorld.elements;return e.set(i[8],i[9],i[10]).normalize()}raycast(){}traverse(e){e(this);const i=this.children;for(let r=0,u=i.length;r<u;r++)i[r].traverse(e)}traverseVisible(e){if(this.visible===!1)return;e(this);const i=this.children;for(let r=0,u=i.length;r<u;r++)i[r].traverseVisible(e)}traverseAncestors(e){const i=this.parent;i!==null&&(e(i),i.traverseAncestors(e))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(e){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||e)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,e=!0);const i=this.children;for(let r=0,u=i.length;r<u;r++)i[r].updateMatrixWorld(e)}updateWorldMatrix(e,i){const r=this.parent;if(e===!0&&r!==null&&r.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),i===!0){const u=this.children;for(let f=0,h=u.length;f<h;f++)u[f].updateWorldMatrix(!1,!0)}}toJSON(e){const i=e===void 0||typeof e=="string",r={};i&&(e={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},r.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});const u={};u.uuid=this.uuid,u.type=this.type,this.name!==""&&(u.name=this.name),this.castShadow===!0&&(u.castShadow=!0),this.receiveShadow===!0&&(u.receiveShadow=!0),this.visible===!1&&(u.visible=!1),this.frustumCulled===!1&&(u.frustumCulled=!1),this.renderOrder!==0&&(u.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(u.userData=this.userData),u.layers=this.layers.mask,u.matrix=this.matrix.toArray(),u.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(u.matrixAutoUpdate=!1),this.isInstancedMesh&&(u.type="InstancedMesh",u.count=this.count,u.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(u.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(u.type="BatchedMesh",u.perObjectFrustumCulled=this.perObjectFrustumCulled,u.sortObjects=this.sortObjects,u.drawRanges=this._drawRanges,u.reservedRanges=this._reservedRanges,u.visibility=this._visibility,u.active=this._active,u.bounds=this._bounds.map(d=>({boxInitialized:d.boxInitialized,boxMin:d.box.min.toArray(),boxMax:d.box.max.toArray(),sphereInitialized:d.sphereInitialized,sphereRadius:d.sphere.radius,sphereCenter:d.sphere.center.toArray()})),u.maxInstanceCount=this._maxInstanceCount,u.maxVertexCount=this._maxVertexCount,u.maxIndexCount=this._maxIndexCount,u.geometryInitialized=this._geometryInitialized,u.geometryCount=this._geometryCount,u.matricesTexture=this._matricesTexture.toJSON(e),this._colorsTexture!==null&&(u.colorsTexture=this._colorsTexture.toJSON(e)),this.boundingSphere!==null&&(u.boundingSphere={center:u.boundingSphere.center.toArray(),radius:u.boundingSphere.radius}),this.boundingBox!==null&&(u.boundingBox={min:u.boundingBox.min.toArray(),max:u.boundingBox.max.toArray()}));function f(d,p){return d[p.uuid]===void 0&&(d[p.uuid]=p.toJSON(e)),p.uuid}if(this.isScene)this.background&&(this.background.isColor?u.background=this.background.toJSON():this.background.isTexture&&(u.background=this.background.toJSON(e).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(u.environment=this.environment.toJSON(e).uuid);else if(this.isMesh||this.isLine||this.isPoints){u.geometry=f(e.geometries,this.geometry);const d=this.geometry.parameters;if(d!==void 0&&d.shapes!==void 0){const p=d.shapes;if(Array.isArray(p))for(let g=0,v=p.length;g<v;g++){const _=p[g];f(e.shapes,_)}else f(e.shapes,p)}}if(this.isSkinnedMesh&&(u.bindMode=this.bindMode,u.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(f(e.skeletons,this.skeleton),u.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){const d=[];for(let p=0,g=this.material.length;p<g;p++)d.push(f(e.materials,this.material[p]));u.material=d}else u.material=f(e.materials,this.material);if(this.children.length>0){u.children=[];for(let d=0;d<this.children.length;d++)u.children.push(this.children[d].toJSON(e).object)}if(this.animations.length>0){u.animations=[];for(let d=0;d<this.animations.length;d++){const p=this.animations[d];u.animations.push(f(e.animations,p))}}if(i){const d=h(e.geometries),p=h(e.materials),g=h(e.textures),v=h(e.images),_=h(e.shapes),y=h(e.skeletons),M=h(e.animations),E=h(e.nodes);d.length>0&&(r.geometries=d),p.length>0&&(r.materials=p),g.length>0&&(r.textures=g),v.length>0&&(r.images=v),_.length>0&&(r.shapes=_),y.length>0&&(r.skeletons=y),M.length>0&&(r.animations=M),E.length>0&&(r.nodes=E)}return r.object=u,r;function h(d){const p=[];for(const g in d){const v=d[g];delete v.metadata,p.push(v)}return p}}clone(e){return new this.constructor().copy(this,e)}copy(e,i=!0){if(this.name=e.name,this.up.copy(e.up),this.position.copy(e.position),this.rotation.order=e.rotation.order,this.quaternion.copy(e.quaternion),this.scale.copy(e.scale),this.matrix.copy(e.matrix),this.matrixWorld.copy(e.matrixWorld),this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrixWorldAutoUpdate=e.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=e.matrixWorldNeedsUpdate,this.layers.mask=e.layers.mask,this.visible=e.visible,this.castShadow=e.castShadow,this.receiveShadow=e.receiveShadow,this.frustumCulled=e.frustumCulled,this.renderOrder=e.renderOrder,this.animations=e.animations.slice(),this.userData=JSON.parse(JSON.stringify(e.userData)),i===!0)for(let r=0;r<e.children.length;r++){const u=e.children[r];this.add(u.clone())}return this}}bn.DEFAULT_UP=new Q(0,1,0);bn.DEFAULT_MATRIX_AUTO_UPDATE=!0;bn.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;const Ni=new Q,va=new Q,Ad=new Q,Sa=new Q,kr=new Q,qr=new Q,Uv=new Q,Rd=new Q,Cd=new Q,wd=new Q,Dd=new Je,Ud=new Je,Nd=new Je;class Pi{constructor(e=new Q,i=new Q,r=new Q){this.a=e,this.b=i,this.c=r}static getNormal(e,i,r,u){u.subVectors(r,i),Ni.subVectors(e,i),u.cross(Ni);const f=u.lengthSq();return f>0?u.multiplyScalar(1/Math.sqrt(f)):u.set(0,0,0)}static getBarycoord(e,i,r,u,f){Ni.subVectors(u,i),va.subVectors(r,i),Ad.subVectors(e,i);const h=Ni.dot(Ni),d=Ni.dot(va),p=Ni.dot(Ad),g=va.dot(va),v=va.dot(Ad),_=h*g-d*d;if(_===0)return f.set(0,0,0),null;const y=1/_,M=(g*p-d*v)*y,E=(h*v-d*p)*y;return f.set(1-M-E,E,M)}static containsPoint(e,i,r,u){return this.getBarycoord(e,i,r,u,Sa)===null?!1:Sa.x>=0&&Sa.y>=0&&Sa.x+Sa.y<=1}static getInterpolation(e,i,r,u,f,h,d,p){return this.getBarycoord(e,i,r,u,Sa)===null?(p.x=0,p.y=0,"z"in p&&(p.z=0),"w"in p&&(p.w=0),null):(p.setScalar(0),p.addScaledVector(f,Sa.x),p.addScaledVector(h,Sa.y),p.addScaledVector(d,Sa.z),p)}static getInterpolatedAttribute(e,i,r,u,f,h){return Dd.setScalar(0),Ud.setScalar(0),Nd.setScalar(0),Dd.fromBufferAttribute(e,i),Ud.fromBufferAttribute(e,r),Nd.fromBufferAttribute(e,u),h.setScalar(0),h.addScaledVector(Dd,f.x),h.addScaledVector(Ud,f.y),h.addScaledVector(Nd,f.z),h}static isFrontFacing(e,i,r,u){return Ni.subVectors(r,i),va.subVectors(e,i),Ni.cross(va).dot(u)<0}set(e,i,r){return this.a.copy(e),this.b.copy(i),this.c.copy(r),this}setFromPointsAndIndices(e,i,r,u){return this.a.copy(e[i]),this.b.copy(e[r]),this.c.copy(e[u]),this}setFromAttributeAndIndices(e,i,r,u){return this.a.fromBufferAttribute(e,i),this.b.fromBufferAttribute(e,r),this.c.fromBufferAttribute(e,u),this}clone(){return new this.constructor().copy(this)}copy(e){return this.a.copy(e.a),this.b.copy(e.b),this.c.copy(e.c),this}getArea(){return Ni.subVectors(this.c,this.b),va.subVectors(this.a,this.b),Ni.cross(va).length()*.5}getMidpoint(e){return e.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(e){return Pi.getNormal(this.a,this.b,this.c,e)}getPlane(e){return e.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(e,i){return Pi.getBarycoord(e,this.a,this.b,this.c,i)}getInterpolation(e,i,r,u,f){return Pi.getInterpolation(e,this.a,this.b,this.c,i,r,u,f)}containsPoint(e){return Pi.containsPoint(e,this.a,this.b,this.c)}isFrontFacing(e){return Pi.isFrontFacing(this.a,this.b,this.c,e)}intersectsBox(e){return e.intersectsTriangle(this)}closestPointToPoint(e,i){const r=this.a,u=this.b,f=this.c;let h,d;kr.subVectors(u,r),qr.subVectors(f,r),Rd.subVectors(e,r);const p=kr.dot(Rd),g=qr.dot(Rd);if(p<=0&&g<=0)return i.copy(r);Cd.subVectors(e,u);const v=kr.dot(Cd),_=qr.dot(Cd);if(v>=0&&_<=v)return i.copy(u);const y=p*_-v*g;if(y<=0&&p>=0&&v<=0)return h=p/(p-v),i.copy(r).addScaledVector(kr,h);wd.subVectors(e,f);const M=kr.dot(wd),E=qr.dot(wd);if(E>=0&&M<=E)return i.copy(f);const R=M*g-p*E;if(R<=0&&g>=0&&E<=0)return d=g/(g-E),i.copy(r).addScaledVector(qr,d);const x=v*E-M*_;if(x<=0&&_-v>=0&&M-E>=0)return Uv.subVectors(f,u),d=(_-v)/(_-v+(M-E)),i.copy(u).addScaledVector(Uv,d);const S=1/(x+R+y);return h=R*S,d=y*S,i.copy(r).addScaledVector(kr,h).addScaledVector(qr,d)}equals(e){return e.a.equals(this.a)&&e.b.equals(this.b)&&e.c.equals(this.c)}}const OS={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},ns={h:0,s:0,l:0},Ju={h:0,s:0,l:0};function Ld(o,e,i){return i<0&&(i+=1),i>1&&(i-=1),i<1/6?o+(e-o)*6*i:i<1/2?e:i<2/3?o+(e-o)*6*(2/3-i):o}class ye{constructor(e,i,r){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(e,i,r)}set(e,i,r){if(i===void 0&&r===void 0){const u=e;u&&u.isColor?this.copy(u):typeof u=="number"?this.setHex(u):typeof u=="string"&&this.setStyle(u)}else this.setRGB(e,i,r);return this}setScalar(e){return this.r=e,this.g=e,this.b=e,this}setHex(e,i=ji){return e=Math.floor(e),this.r=(e>>16&255)/255,this.g=(e>>8&255)/255,this.b=(e&255)/255,De.toWorkingColorSpace(this,i),this}setRGB(e,i,r,u=De.workingColorSpace){return this.r=e,this.g=i,this.b=r,De.toWorkingColorSpace(this,u),this}setHSL(e,i,r,u=De.workingColorSpace){if(e=UE(e,1),i=Fn(i,0,1),r=Fn(r,0,1),i===0)this.r=this.g=this.b=r;else{const f=r<=.5?r*(1+i):r+i-r*i,h=2*r-f;this.r=Ld(h,f,e+1/3),this.g=Ld(h,f,e),this.b=Ld(h,f,e-1/3)}return De.toWorkingColorSpace(this,u),this}setStyle(e,i=ji){function r(f){f!==void 0&&parseFloat(f)<1&&console.warn("THREE.Color: Alpha component of "+e+" will be ignored.")}let u;if(u=/^(\w+)\(([^\)]*)\)/.exec(e)){let f;const h=u[1],d=u[2];switch(h){case"rgb":case"rgba":if(f=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(d))return r(f[4]),this.setRGB(Math.min(255,parseInt(f[1],10))/255,Math.min(255,parseInt(f[2],10))/255,Math.min(255,parseInt(f[3],10))/255,i);if(f=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(d))return r(f[4]),this.setRGB(Math.min(100,parseInt(f[1],10))/100,Math.min(100,parseInt(f[2],10))/100,Math.min(100,parseInt(f[3],10))/100,i);break;case"hsl":case"hsla":if(f=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(d))return r(f[4]),this.setHSL(parseFloat(f[1])/360,parseFloat(f[2])/100,parseFloat(f[3])/100,i);break;default:console.warn("THREE.Color: Unknown color model "+e)}}else if(u=/^\#([A-Fa-f\d]+)$/.exec(e)){const f=u[1],h=f.length;if(h===3)return this.setRGB(parseInt(f.charAt(0),16)/15,parseInt(f.charAt(1),16)/15,parseInt(f.charAt(2),16)/15,i);if(h===6)return this.setHex(parseInt(f,16),i);console.warn("THREE.Color: Invalid hex color "+e)}else if(e&&e.length>0)return this.setColorName(e,i);return this}setColorName(e,i=ji){const r=OS[e.toLowerCase()];return r!==void 0?this.setHex(r,i):console.warn("THREE.Color: Unknown color "+e),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(e){return this.r=e.r,this.g=e.g,this.b=e.b,this}copySRGBToLinear(e){return this.r=io(e.r),this.g=io(e.g),this.b=io(e.b),this}copyLinearToSRGB(e){return this.r=gd(e.r),this.g=gd(e.g),this.b=gd(e.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(e=ji){return De.fromWorkingColorSpace(Un.copy(this),e),Math.round(Fn(Un.r*255,0,255))*65536+Math.round(Fn(Un.g*255,0,255))*256+Math.round(Fn(Un.b*255,0,255))}getHexString(e=ji){return("000000"+this.getHex(e).toString(16)).slice(-6)}getHSL(e,i=De.workingColorSpace){De.fromWorkingColorSpace(Un.copy(this),i);const r=Un.r,u=Un.g,f=Un.b,h=Math.max(r,u,f),d=Math.min(r,u,f);let p,g;const v=(d+h)/2;if(d===h)p=0,g=0;else{const _=h-d;switch(g=v<=.5?_/(h+d):_/(2-h-d),h){case r:p=(u-f)/_+(u<f?6:0);break;case u:p=(f-r)/_+2;break;case f:p=(r-u)/_+4;break}p/=6}return e.h=p,e.s=g,e.l=v,e}getRGB(e,i=De.workingColorSpace){return De.fromWorkingColorSpace(Un.copy(this),i),e.r=Un.r,e.g=Un.g,e.b=Un.b,e}getStyle(e=ji){De.fromWorkingColorSpace(Un.copy(this),e);const i=Un.r,r=Un.g,u=Un.b;return e!==ji?`color(${e} ${i.toFixed(3)} ${r.toFixed(3)} ${u.toFixed(3)})`:`rgb(${Math.round(i*255)},${Math.round(r*255)},${Math.round(u*255)})`}offsetHSL(e,i,r){return this.getHSL(ns),this.setHSL(ns.h+e,ns.s+i,ns.l+r)}add(e){return this.r+=e.r,this.g+=e.g,this.b+=e.b,this}addColors(e,i){return this.r=e.r+i.r,this.g=e.g+i.g,this.b=e.b+i.b,this}addScalar(e){return this.r+=e,this.g+=e,this.b+=e,this}sub(e){return this.r=Math.max(0,this.r-e.r),this.g=Math.max(0,this.g-e.g),this.b=Math.max(0,this.b-e.b),this}multiply(e){return this.r*=e.r,this.g*=e.g,this.b*=e.b,this}multiplyScalar(e){return this.r*=e,this.g*=e,this.b*=e,this}lerp(e,i){return this.r+=(e.r-this.r)*i,this.g+=(e.g-this.g)*i,this.b+=(e.b-this.b)*i,this}lerpColors(e,i,r){return this.r=e.r+(i.r-e.r)*r,this.g=e.g+(i.g-e.g)*r,this.b=e.b+(i.b-e.b)*r,this}lerpHSL(e,i){this.getHSL(ns),e.getHSL(Ju);const r=md(ns.h,Ju.h,i),u=md(ns.s,Ju.s,i),f=md(ns.l,Ju.l,i);return this.setHSL(r,u,f),this}setFromVector3(e){return this.r=e.x,this.g=e.y,this.b=e.z,this}applyMatrix3(e){const i=this.r,r=this.g,u=this.b,f=e.elements;return this.r=f[0]*i+f[3]*r+f[6]*u,this.g=f[1]*i+f[4]*r+f[7]*u,this.b=f[2]*i+f[5]*r+f[8]*u,this}equals(e){return e.r===this.r&&e.g===this.g&&e.b===this.b}fromArray(e,i=0){return this.r=e[i],this.g=e[i+1],this.b=e[i+2],this}toArray(e=[],i=0){return e[i]=this.r,e[i+1]=this.g,e[i+2]=this.b,e}fromBufferAttribute(e,i){return this.r=e.getX(i),this.g=e.getY(i),this.b=e.getZ(i),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}}const Un=new ye;ye.NAMES=OS;let KE=0;class Sl extends Zs{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:KE++}),this.uuid=gl(),this.name="",this.type="Material",this.blending=eo,this.side=ls,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=Wd,this.blendDst=jd,this.blendEquation=Gs,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new ye(0,0,0),this.blendAlpha=0,this.depthFunc=ao,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=gv,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=Ir,this.stencilZFail=Ir,this.stencilZPass=Ir,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(e){this._alphaTest>0!=e>0&&this.version++,this._alphaTest=e}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(e){if(e!==void 0)for(const i in e){const r=e[i];if(r===void 0){console.warn(`THREE.Material: parameter '${i}' has value of undefined.`);continue}const u=this[i];if(u===void 0){console.warn(`THREE.Material: '${i}' is not a property of THREE.${this.type}.`);continue}u&&u.isColor?u.set(r):u&&u.isVector3&&r&&r.isVector3?u.copy(r):this[i]=r}}toJSON(e){const i=e===void 0||typeof e=="string";i&&(e={textures:{},images:{}});const r={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};r.uuid=this.uuid,r.type=this.type,this.name!==""&&(r.name=this.name),this.color&&this.color.isColor&&(r.color=this.color.getHex()),this.roughness!==void 0&&(r.roughness=this.roughness),this.metalness!==void 0&&(r.metalness=this.metalness),this.sheen!==void 0&&(r.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(r.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(r.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(r.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&this.emissiveIntensity!==1&&(r.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(r.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(r.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(r.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(r.shininess=this.shininess),this.clearcoat!==void 0&&(r.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(r.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(r.clearcoatMap=this.clearcoatMap.toJSON(e).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(r.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(e).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(r.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(e).uuid,r.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.dispersion!==void 0&&(r.dispersion=this.dispersion),this.iridescence!==void 0&&(r.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(r.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(r.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(r.iridescenceMap=this.iridescenceMap.toJSON(e).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(r.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(e).uuid),this.anisotropy!==void 0&&(r.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(r.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(r.anisotropyMap=this.anisotropyMap.toJSON(e).uuid),this.map&&this.map.isTexture&&(r.map=this.map.toJSON(e).uuid),this.matcap&&this.matcap.isTexture&&(r.matcap=this.matcap.toJSON(e).uuid),this.alphaMap&&this.alphaMap.isTexture&&(r.alphaMap=this.alphaMap.toJSON(e).uuid),this.lightMap&&this.lightMap.isTexture&&(r.lightMap=this.lightMap.toJSON(e).uuid,r.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(r.aoMap=this.aoMap.toJSON(e).uuid,r.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(r.bumpMap=this.bumpMap.toJSON(e).uuid,r.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(r.normalMap=this.normalMap.toJSON(e).uuid,r.normalMapType=this.normalMapType,r.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(r.displacementMap=this.displacementMap.toJSON(e).uuid,r.displacementScale=this.displacementScale,r.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(r.roughnessMap=this.roughnessMap.toJSON(e).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(r.metalnessMap=this.metalnessMap.toJSON(e).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(r.emissiveMap=this.emissiveMap.toJSON(e).uuid),this.specularMap&&this.specularMap.isTexture&&(r.specularMap=this.specularMap.toJSON(e).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(r.specularIntensityMap=this.specularIntensityMap.toJSON(e).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(r.specularColorMap=this.specularColorMap.toJSON(e).uuid),this.envMap&&this.envMap.isTexture&&(r.envMap=this.envMap.toJSON(e).uuid,this.combine!==void 0&&(r.combine=this.combine)),this.envMapRotation!==void 0&&(r.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(r.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(r.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(r.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(r.gradientMap=this.gradientMap.toJSON(e).uuid),this.transmission!==void 0&&(r.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(r.transmissionMap=this.transmissionMap.toJSON(e).uuid),this.thickness!==void 0&&(r.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(r.thicknessMap=this.thicknessMap.toJSON(e).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(r.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(r.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(r.size=this.size),this.shadowSide!==null&&(r.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(r.sizeAttenuation=this.sizeAttenuation),this.blending!==eo&&(r.blending=this.blending),this.side!==ls&&(r.side=this.side),this.vertexColors===!0&&(r.vertexColors=!0),this.opacity<1&&(r.opacity=this.opacity),this.transparent===!0&&(r.transparent=!0),this.blendSrc!==Wd&&(r.blendSrc=this.blendSrc),this.blendDst!==jd&&(r.blendDst=this.blendDst),this.blendEquation!==Gs&&(r.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(r.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(r.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(r.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(r.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(r.blendAlpha=this.blendAlpha),this.depthFunc!==ao&&(r.depthFunc=this.depthFunc),this.depthTest===!1&&(r.depthTest=this.depthTest),this.depthWrite===!1&&(r.depthWrite=this.depthWrite),this.colorWrite===!1&&(r.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(r.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==gv&&(r.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(r.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(r.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==Ir&&(r.stencilFail=this.stencilFail),this.stencilZFail!==Ir&&(r.stencilZFail=this.stencilZFail),this.stencilZPass!==Ir&&(r.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(r.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(r.rotation=this.rotation),this.polygonOffset===!0&&(r.polygonOffset=!0),this.polygonOffsetFactor!==0&&(r.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(r.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(r.linewidth=this.linewidth),this.dashSize!==void 0&&(r.dashSize=this.dashSize),this.gapSize!==void 0&&(r.gapSize=this.gapSize),this.scale!==void 0&&(r.scale=this.scale),this.dithering===!0&&(r.dithering=!0),this.alphaTest>0&&(r.alphaTest=this.alphaTest),this.alphaHash===!0&&(r.alphaHash=!0),this.alphaToCoverage===!0&&(r.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(r.premultipliedAlpha=!0),this.forceSinglePass===!0&&(r.forceSinglePass=!0),this.wireframe===!0&&(r.wireframe=!0),this.wireframeLinewidth>1&&(r.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(r.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(r.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(r.flatShading=!0),this.visible===!1&&(r.visible=!1),this.toneMapped===!1&&(r.toneMapped=!1),this.fog===!1&&(r.fog=!1),Object.keys(this.userData).length>0&&(r.userData=this.userData);function u(f){const h=[];for(const d in f){const p=f[d];delete p.metadata,h.push(p)}return h}if(i){const f=u(e.textures),h=u(e.images);f.length>0&&(r.textures=f),h.length>0&&(r.images=h)}return r}clone(){return new this.constructor().copy(this)}copy(e){this.name=e.name,this.blending=e.blending,this.side=e.side,this.vertexColors=e.vertexColors,this.opacity=e.opacity,this.transparent=e.transparent,this.blendSrc=e.blendSrc,this.blendDst=e.blendDst,this.blendEquation=e.blendEquation,this.blendSrcAlpha=e.blendSrcAlpha,this.blendDstAlpha=e.blendDstAlpha,this.blendEquationAlpha=e.blendEquationAlpha,this.blendColor.copy(e.blendColor),this.blendAlpha=e.blendAlpha,this.depthFunc=e.depthFunc,this.depthTest=e.depthTest,this.depthWrite=e.depthWrite,this.stencilWriteMask=e.stencilWriteMask,this.stencilFunc=e.stencilFunc,this.stencilRef=e.stencilRef,this.stencilFuncMask=e.stencilFuncMask,this.stencilFail=e.stencilFail,this.stencilZFail=e.stencilZFail,this.stencilZPass=e.stencilZPass,this.stencilWrite=e.stencilWrite;const i=e.clippingPlanes;let r=null;if(i!==null){const u=i.length;r=new Array(u);for(let f=0;f!==u;++f)r[f]=i[f].clone()}return this.clippingPlanes=r,this.clipIntersection=e.clipIntersection,this.clipShadows=e.clipShadows,this.shadowSide=e.shadowSide,this.colorWrite=e.colorWrite,this.precision=e.precision,this.polygonOffset=e.polygonOffset,this.polygonOffsetFactor=e.polygonOffsetFactor,this.polygonOffsetUnits=e.polygonOffsetUnits,this.dithering=e.dithering,this.alphaTest=e.alphaTest,this.alphaHash=e.alphaHash,this.alphaToCoverage=e.alphaToCoverage,this.premultipliedAlpha=e.premultipliedAlpha,this.forceSinglePass=e.forceSinglePass,this.visible=e.visible,this.toneMapped=e.toneMapped,this.userData=JSON.parse(JSON.stringify(e.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(e){e===!0&&this.version++}onBuild(){console.warn("Material: onBuild() has been removed.")}}class js extends Sl{constructor(e){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new ye(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Ta,this.combine=gS,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.lightMap=e.lightMap,this.lightMapIntensity=e.lightMapIntensity,this.aoMap=e.aoMap,this.aoMapIntensity=e.aoMapIntensity,this.specularMap=e.specularMap,this.alphaMap=e.alphaMap,this.envMap=e.envMap,this.envMapRotation.copy(e.envMapRotation),this.combine=e.combine,this.reflectivity=e.reflectivity,this.refractionRatio=e.refractionRatio,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.wireframeLinecap=e.wireframeLinecap,this.wireframeLinejoin=e.wireframeLinejoin,this.fog=e.fog,this}}const on=new Q,$u=new ce;class xi{constructor(e,i,r=!1){if(Array.isArray(e))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,this.name="",this.array=e,this.itemSize=i,this.count=e!==void 0?e.length/i:0,this.normalized=r,this.usage=vv,this.updateRanges=[],this.gpuType=xa,this.version=0}onUploadCallback(){}set needsUpdate(e){e===!0&&this.version++}setUsage(e){return this.usage=e,this}addUpdateRange(e,i){this.updateRanges.push({start:e,count:i})}clearUpdateRanges(){this.updateRanges.length=0}copy(e){return this.name=e.name,this.array=new e.array.constructor(e.array),this.itemSize=e.itemSize,this.count=e.count,this.normalized=e.normalized,this.usage=e.usage,this.gpuType=e.gpuType,this}copyAt(e,i,r){e*=this.itemSize,r*=i.itemSize;for(let u=0,f=this.itemSize;u<f;u++)this.array[e+u]=i.array[r+u];return this}copyArray(e){return this.array.set(e),this}applyMatrix3(e){if(this.itemSize===2)for(let i=0,r=this.count;i<r;i++)$u.fromBufferAttribute(this,i),$u.applyMatrix3(e),this.setXY(i,$u.x,$u.y);else if(this.itemSize===3)for(let i=0,r=this.count;i<r;i++)on.fromBufferAttribute(this,i),on.applyMatrix3(e),this.setXYZ(i,on.x,on.y,on.z);return this}applyMatrix4(e){for(let i=0,r=this.count;i<r;i++)on.fromBufferAttribute(this,i),on.applyMatrix4(e),this.setXYZ(i,on.x,on.y,on.z);return this}applyNormalMatrix(e){for(let i=0,r=this.count;i<r;i++)on.fromBufferAttribute(this,i),on.applyNormalMatrix(e),this.setXYZ(i,on.x,on.y,on.z);return this}transformDirection(e){for(let i=0,r=this.count;i<r;i++)on.fromBufferAttribute(this,i),on.transformDirection(e),this.setXYZ(i,on.x,on.y,on.z);return this}set(e,i=0){return this.array.set(e,i),this}getComponent(e,i){let r=this.array[e*this.itemSize+i];return this.normalized&&(r=al(r,this.array)),r}setComponent(e,i,r){return this.normalized&&(r=qn(r,this.array)),this.array[e*this.itemSize+i]=r,this}getX(e){let i=this.array[e*this.itemSize];return this.normalized&&(i=al(i,this.array)),i}setX(e,i){return this.normalized&&(i=qn(i,this.array)),this.array[e*this.itemSize]=i,this}getY(e){let i=this.array[e*this.itemSize+1];return this.normalized&&(i=al(i,this.array)),i}setY(e,i){return this.normalized&&(i=qn(i,this.array)),this.array[e*this.itemSize+1]=i,this}getZ(e){let i=this.array[e*this.itemSize+2];return this.normalized&&(i=al(i,this.array)),i}setZ(e,i){return this.normalized&&(i=qn(i,this.array)),this.array[e*this.itemSize+2]=i,this}getW(e){let i=this.array[e*this.itemSize+3];return this.normalized&&(i=al(i,this.array)),i}setW(e,i){return this.normalized&&(i=qn(i,this.array)),this.array[e*this.itemSize+3]=i,this}setXY(e,i,r){return e*=this.itemSize,this.normalized&&(i=qn(i,this.array),r=qn(r,this.array)),this.array[e+0]=i,this.array[e+1]=r,this}setXYZ(e,i,r,u){return e*=this.itemSize,this.normalized&&(i=qn(i,this.array),r=qn(r,this.array),u=qn(u,this.array)),this.array[e+0]=i,this.array[e+1]=r,this.array[e+2]=u,this}setXYZW(e,i,r,u,f){return e*=this.itemSize,this.normalized&&(i=qn(i,this.array),r=qn(r,this.array),u=qn(u,this.array),f=qn(f,this.array)),this.array[e+0]=i,this.array[e+1]=r,this.array[e+2]=u,this.array[e+3]=f,this}onUpload(e){return this.onUploadCallback=e,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){const e={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(e.name=this.name),this.usage!==vv&&(e.usage=this.usage),e}}class PS extends xi{constructor(e,i,r){super(new Uint16Array(e),i,r)}}class zS extends xi{constructor(e,i,r){super(new Uint32Array(e),i,r)}}class gn extends xi{constructor(e,i,r){super(new Float32Array(e),i,r)}}let QE=0;const vi=new Ze,Od=new bn,Wr=new Q,oi=new vl,ul=new vl,_n=new Q;class Qn extends Zs{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:QE++}),this.uuid=gl(),this.name="",this.type="BufferGeometry",this.index=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(e){return Array.isArray(e)?this.index=new(DS(e)?zS:PS)(e,1):this.index=e,this}getAttribute(e){return this.attributes[e]}setAttribute(e,i){return this.attributes[e]=i,this}deleteAttribute(e){return delete this.attributes[e],this}hasAttribute(e){return this.attributes[e]!==void 0}addGroup(e,i,r=0){this.groups.push({start:e,count:i,materialIndex:r})}clearGroups(){this.groups=[]}setDrawRange(e,i){this.drawRange.start=e,this.drawRange.count=i}applyMatrix4(e){const i=this.attributes.position;i!==void 0&&(i.applyMatrix4(e),i.needsUpdate=!0);const r=this.attributes.normal;if(r!==void 0){const f=new he().getNormalMatrix(e);r.applyNormalMatrix(f),r.needsUpdate=!0}const u=this.attributes.tangent;return u!==void 0&&(u.transformDirection(e),u.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(e){return vi.makeRotationFromQuaternion(e),this.applyMatrix4(vi),this}rotateX(e){return vi.makeRotationX(e),this.applyMatrix4(vi),this}rotateY(e){return vi.makeRotationY(e),this.applyMatrix4(vi),this}rotateZ(e){return vi.makeRotationZ(e),this.applyMatrix4(vi),this}translate(e,i,r){return vi.makeTranslation(e,i,r),this.applyMatrix4(vi),this}scale(e,i,r){return vi.makeScale(e,i,r),this.applyMatrix4(vi),this}lookAt(e){return Od.lookAt(e),Od.updateMatrix(),this.applyMatrix4(Od.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(Wr).negate(),this.translate(Wr.x,Wr.y,Wr.z),this}setFromPoints(e){const i=[];for(let r=0,u=e.length;r<u;r++){const f=e[r];i.push(f.x,f.y,f.z||0)}return this.setAttribute("position",new gn(i,3)),this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new vl);const e=this.attributes.position,i=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new Q(-1/0,-1/0,-1/0),new Q(1/0,1/0,1/0));return}if(e!==void 0){if(this.boundingBox.setFromBufferAttribute(e),i)for(let r=0,u=i.length;r<u;r++){const f=i[r];oi.setFromBufferAttribute(f),this.morphTargetsRelative?(_n.addVectors(this.boundingBox.min,oi.min),this.boundingBox.expandByPoint(_n),_n.addVectors(this.boundingBox.max,oi.max),this.boundingBox.expandByPoint(_n)):(this.boundingBox.expandByPoint(oi.min),this.boundingBox.expandByPoint(oi.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new Lc);const e=this.attributes.position,i=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new Q,1/0);return}if(e){const r=this.boundingSphere.center;if(oi.setFromBufferAttribute(e),i)for(let f=0,h=i.length;f<h;f++){const d=i[f];ul.setFromBufferAttribute(d),this.morphTargetsRelative?(_n.addVectors(oi.min,ul.min),oi.expandByPoint(_n),_n.addVectors(oi.max,ul.max),oi.expandByPoint(_n)):(oi.expandByPoint(ul.min),oi.expandByPoint(ul.max))}oi.getCenter(r);let u=0;for(let f=0,h=e.count;f<h;f++)_n.fromBufferAttribute(e,f),u=Math.max(u,r.distanceToSquared(_n));if(i)for(let f=0,h=i.length;f<h;f++){const d=i[f],p=this.morphTargetsRelative;for(let g=0,v=d.count;g<v;g++)_n.fromBufferAttribute(d,g),p&&(Wr.fromBufferAttribute(e,g),_n.add(Wr)),u=Math.max(u,r.distanceToSquared(_n))}this.boundingSphere.radius=Math.sqrt(u),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){const e=this.index,i=this.attributes;if(e===null||i.position===void 0||i.normal===void 0||i.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}const r=i.position,u=i.normal,f=i.uv;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new xi(new Float32Array(4*r.count),4));const h=this.getAttribute("tangent"),d=[],p=[];for(let V=0;V<r.count;V++)d[V]=new Q,p[V]=new Q;const g=new Q,v=new Q,_=new Q,y=new ce,M=new ce,E=new ce,R=new Q,x=new Q;function S(V,gt,T){g.fromBufferAttribute(r,V),v.fromBufferAttribute(r,gt),_.fromBufferAttribute(r,T),y.fromBufferAttribute(f,V),M.fromBufferAttribute(f,gt),E.fromBufferAttribute(f,T),v.sub(g),_.sub(g),M.sub(y),E.sub(y);const w=1/(M.x*E.y-E.x*M.y);isFinite(w)&&(R.copy(v).multiplyScalar(E.y).addScaledVector(_,-M.y).multiplyScalar(w),x.copy(_).multiplyScalar(M.x).addScaledVector(v,-E.x).multiplyScalar(w),d[V].add(R),d[gt].add(R),d[T].add(R),p[V].add(x),p[gt].add(x),p[T].add(x))}let L=this.groups;L.length===0&&(L=[{start:0,count:e.count}]);for(let V=0,gt=L.length;V<gt;++V){const T=L[V],w=T.start,nt=T.count;for(let rt=w,lt=w+nt;rt<lt;rt+=3)S(e.getX(rt+0),e.getX(rt+1),e.getX(rt+2))}const U=new Q,P=new Q,J=new Q,B=new Q;function O(V){J.fromBufferAttribute(u,V),B.copy(J);const gt=d[V];U.copy(gt),U.sub(J.multiplyScalar(J.dot(gt))).normalize(),P.crossVectors(B,gt);const w=P.dot(p[V])<0?-1:1;h.setXYZW(V,U.x,U.y,U.z,w)}for(let V=0,gt=L.length;V<gt;++V){const T=L[V],w=T.start,nt=T.count;for(let rt=w,lt=w+nt;rt<lt;rt+=3)O(e.getX(rt+0)),O(e.getX(rt+1)),O(e.getX(rt+2))}}computeVertexNormals(){const e=this.index,i=this.getAttribute("position");if(i!==void 0){let r=this.getAttribute("normal");if(r===void 0)r=new xi(new Float32Array(i.count*3),3),this.setAttribute("normal",r);else for(let y=0,M=r.count;y<M;y++)r.setXYZ(y,0,0,0);const u=new Q,f=new Q,h=new Q,d=new Q,p=new Q,g=new Q,v=new Q,_=new Q;if(e)for(let y=0,M=e.count;y<M;y+=3){const E=e.getX(y+0),R=e.getX(y+1),x=e.getX(y+2);u.fromBufferAttribute(i,E),f.fromBufferAttribute(i,R),h.fromBufferAttribute(i,x),v.subVectors(h,f),_.subVectors(u,f),v.cross(_),d.fromBufferAttribute(r,E),p.fromBufferAttribute(r,R),g.fromBufferAttribute(r,x),d.add(v),p.add(v),g.add(v),r.setXYZ(E,d.x,d.y,d.z),r.setXYZ(R,p.x,p.y,p.z),r.setXYZ(x,g.x,g.y,g.z)}else for(let y=0,M=i.count;y<M;y+=3)u.fromBufferAttribute(i,y+0),f.fromBufferAttribute(i,y+1),h.fromBufferAttribute(i,y+2),v.subVectors(h,f),_.subVectors(u,f),v.cross(_),r.setXYZ(y+0,v.x,v.y,v.z),r.setXYZ(y+1,v.x,v.y,v.z),r.setXYZ(y+2,v.x,v.y,v.z);this.normalizeNormals(),r.needsUpdate=!0}}normalizeNormals(){const e=this.attributes.normal;for(let i=0,r=e.count;i<r;i++)_n.fromBufferAttribute(e,i),_n.normalize(),e.setXYZ(i,_n.x,_n.y,_n.z)}toNonIndexed(){function e(d,p){const g=d.array,v=d.itemSize,_=d.normalized,y=new g.constructor(p.length*v);let M=0,E=0;for(let R=0,x=p.length;R<x;R++){d.isInterleavedBufferAttribute?M=p[R]*d.data.stride+d.offset:M=p[R]*v;for(let S=0;S<v;S++)y[E++]=g[M++]}return new xi(y,v,_)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;const i=new Qn,r=this.index.array,u=this.attributes;for(const d in u){const p=u[d],g=e(p,r);i.setAttribute(d,g)}const f=this.morphAttributes;for(const d in f){const p=[],g=f[d];for(let v=0,_=g.length;v<_;v++){const y=g[v],M=e(y,r);p.push(M)}i.morphAttributes[d]=p}i.morphTargetsRelative=this.morphTargetsRelative;const h=this.groups;for(let d=0,p=h.length;d<p;d++){const g=h[d];i.addGroup(g.start,g.count,g.materialIndex)}return i}toJSON(){const e={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(e.uuid=this.uuid,e.type=this.type,this.name!==""&&(e.name=this.name),Object.keys(this.userData).length>0&&(e.userData=this.userData),this.parameters!==void 0){const p=this.parameters;for(const g in p)p[g]!==void 0&&(e[g]=p[g]);return e}e.data={attributes:{}};const i=this.index;i!==null&&(e.data.index={type:i.array.constructor.name,array:Array.prototype.slice.call(i.array)});const r=this.attributes;for(const p in r){const g=r[p];e.data.attributes[p]=g.toJSON(e.data)}const u={};let f=!1;for(const p in this.morphAttributes){const g=this.morphAttributes[p],v=[];for(let _=0,y=g.length;_<y;_++){const M=g[_];v.push(M.toJSON(e.data))}v.length>0&&(u[p]=v,f=!0)}f&&(e.data.morphAttributes=u,e.data.morphTargetsRelative=this.morphTargetsRelative);const h=this.groups;h.length>0&&(e.data.groups=JSON.parse(JSON.stringify(h)));const d=this.boundingSphere;return d!==null&&(e.data.boundingSphere={center:d.center.toArray(),radius:d.radius}),e}clone(){return new this.constructor().copy(this)}copy(e){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;const i={};this.name=e.name;const r=e.index;r!==null&&this.setIndex(r.clone(i));const u=e.attributes;for(const g in u){const v=u[g];this.setAttribute(g,v.clone(i))}const f=e.morphAttributes;for(const g in f){const v=[],_=f[g];for(let y=0,M=_.length;y<M;y++)v.push(_[y].clone(i));this.morphAttributes[g]=v}this.morphTargetsRelative=e.morphTargetsRelative;const h=e.groups;for(let g=0,v=h.length;g<v;g++){const _=h[g];this.addGroup(_.start,_.count,_.materialIndex)}const d=e.boundingBox;d!==null&&(this.boundingBox=d.clone());const p=e.boundingSphere;return p!==null&&(this.boundingSphere=p.clone()),this.drawRange.start=e.drawRange.start,this.drawRange.count=e.drawRange.count,this.userData=e.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}}const Nv=new Ze,zs=new Xp,tc=new Lc,Lv=new Q,ec=new Q,nc=new Q,ic=new Q,Pd=new Q,ac=new Q,Ov=new Q,sc=new Q;class jn extends bn{constructor(e=new Qn,i=new js){super(),this.isMesh=!0,this.type="Mesh",this.geometry=e,this.material=i,this.updateMorphTargets()}copy(e,i){return super.copy(e,i),e.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=e.morphTargetInfluences.slice()),e.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},e.morphTargetDictionary)),this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}updateMorphTargets(){const i=this.geometry.morphAttributes,r=Object.keys(i);if(r.length>0){const u=i[r[0]];if(u!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let f=0,h=u.length;f<h;f++){const d=u[f].name||String(f);this.morphTargetInfluences.push(0),this.morphTargetDictionary[d]=f}}}}getVertexPosition(e,i){const r=this.geometry,u=r.attributes.position,f=r.morphAttributes.position,h=r.morphTargetsRelative;i.fromBufferAttribute(u,e);const d=this.morphTargetInfluences;if(f&&d){ac.set(0,0,0);for(let p=0,g=f.length;p<g;p++){const v=d[p],_=f[p];v!==0&&(Pd.fromBufferAttribute(_,e),h?ac.addScaledVector(Pd,v):ac.addScaledVector(Pd.sub(i),v))}i.add(ac)}return i}raycast(e,i){const r=this.geometry,u=this.material,f=this.matrixWorld;u!==void 0&&(r.boundingSphere===null&&r.computeBoundingSphere(),tc.copy(r.boundingSphere),tc.applyMatrix4(f),zs.copy(e.ray).recast(e.near),!(tc.containsPoint(zs.origin)===!1&&(zs.intersectSphere(tc,Lv)===null||zs.origin.distanceToSquared(Lv)>(e.far-e.near)**2))&&(Nv.copy(f).invert(),zs.copy(e.ray).applyMatrix4(Nv),!(r.boundingBox!==null&&zs.intersectsBox(r.boundingBox)===!1)&&this._computeIntersections(e,i,zs)))}_computeIntersections(e,i,r){let u;const f=this.geometry,h=this.material,d=f.index,p=f.attributes.position,g=f.attributes.uv,v=f.attributes.uv1,_=f.attributes.normal,y=f.groups,M=f.drawRange;if(d!==null)if(Array.isArray(h))for(let E=0,R=y.length;E<R;E++){const x=y[E],S=h[x.materialIndex],L=Math.max(x.start,M.start),U=Math.min(d.count,Math.min(x.start+x.count,M.start+M.count));for(let P=L,J=U;P<J;P+=3){const B=d.getX(P),O=d.getX(P+1),V=d.getX(P+2);u=rc(this,S,e,r,g,v,_,B,O,V),u&&(u.faceIndex=Math.floor(P/3),u.face.materialIndex=x.materialIndex,i.push(u))}}else{const E=Math.max(0,M.start),R=Math.min(d.count,M.start+M.count);for(let x=E,S=R;x<S;x+=3){const L=d.getX(x),U=d.getX(x+1),P=d.getX(x+2);u=rc(this,h,e,r,g,v,_,L,U,P),u&&(u.faceIndex=Math.floor(x/3),i.push(u))}}else if(p!==void 0)if(Array.isArray(h))for(let E=0,R=y.length;E<R;E++){const x=y[E],S=h[x.materialIndex],L=Math.max(x.start,M.start),U=Math.min(p.count,Math.min(x.start+x.count,M.start+M.count));for(let P=L,J=U;P<J;P+=3){const B=P,O=P+1,V=P+2;u=rc(this,S,e,r,g,v,_,B,O,V),u&&(u.faceIndex=Math.floor(P/3),u.face.materialIndex=x.materialIndex,i.push(u))}}else{const E=Math.max(0,M.start),R=Math.min(p.count,M.start+M.count);for(let x=E,S=R;x<S;x+=3){const L=x,U=x+1,P=x+2;u=rc(this,h,e,r,g,v,_,L,U,P),u&&(u.faceIndex=Math.floor(x/3),i.push(u))}}}}function JE(o,e,i,r,u,f,h,d){let p;if(e.side===Zn?p=r.intersectTriangle(h,f,u,!0,d):p=r.intersectTriangle(u,f,h,e.side===ls,d),p===null)return null;sc.copy(d),sc.applyMatrix4(o.matrixWorld);const g=i.ray.origin.distanceTo(sc);return g<i.near||g>i.far?null:{distance:g,point:sc.clone(),object:o}}function rc(o,e,i,r,u,f,h,d,p,g){o.getVertexPosition(d,ec),o.getVertexPosition(p,nc),o.getVertexPosition(g,ic);const v=JE(o,e,i,r,ec,nc,ic,Ov);if(v){const _=new Q;Pi.getBarycoord(Ov,ec,nc,ic,_),u&&(v.uv=Pi.getInterpolatedAttribute(u,d,p,g,_,new ce)),f&&(v.uv1=Pi.getInterpolatedAttribute(f,d,p,g,_,new ce)),h&&(v.normal=Pi.getInterpolatedAttribute(h,d,p,g,_,new Q),v.normal.dot(r.direction)>0&&v.normal.multiplyScalar(-1));const y={a:d,b:p,c:g,normal:new Q,materialIndex:0};Pi.getNormal(ec,nc,ic,y.normal),v.face=y,v.barycoord=_}return v}class co extends Qn{constructor(e=1,i=1,r=1,u=1,f=1,h=1){super(),this.type="BoxGeometry",this.parameters={width:e,height:i,depth:r,widthSegments:u,heightSegments:f,depthSegments:h};const d=this;u=Math.floor(u),f=Math.floor(f),h=Math.floor(h);const p=[],g=[],v=[],_=[];let y=0,M=0;E("z","y","x",-1,-1,r,i,e,h,f,0),E("z","y","x",1,-1,r,i,-e,h,f,1),E("x","z","y",1,1,e,r,i,u,h,2),E("x","z","y",1,-1,e,r,-i,u,h,3),E("x","y","z",1,-1,e,i,r,u,f,4),E("x","y","z",-1,-1,e,i,-r,u,f,5),this.setIndex(p),this.setAttribute("position",new gn(g,3)),this.setAttribute("normal",new gn(v,3)),this.setAttribute("uv",new gn(_,2));function E(R,x,S,L,U,P,J,B,O,V,gt){const T=P/O,w=J/V,nt=P/2,rt=J/2,lt=B/2,ft=O+1,H=V+1;let at=0,Z=0;const yt=new Q;for(let St=0;St<H;St++){const Pt=St*w-rt;for(let oe=0;oe<ft;oe++){const me=oe*T-nt;yt[R]=me*L,yt[x]=Pt*U,yt[S]=lt,g.push(yt.x,yt.y,yt.z),yt[R]=0,yt[x]=0,yt[S]=B>0?1:-1,v.push(yt.x,yt.y,yt.z),_.push(oe/O),_.push(1-St/V),at+=1}}for(let St=0;St<V;St++)for(let Pt=0;Pt<O;Pt++){const oe=y+Pt+ft*St,me=y+Pt+ft*(St+1),D=y+(Pt+1)+ft*(St+1),X=y+(Pt+1)+ft*St;p.push(oe,me,X),p.push(me,D,X),Z+=6}d.addGroup(M,Z,gt),M+=Z,y+=at}}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new co(e.width,e.height,e.depth,e.widthSegments,e.heightSegments,e.depthSegments)}}function uo(o){const e={};for(const i in o){e[i]={};for(const r in o[i]){const u=o[i][r];u&&(u.isColor||u.isMatrix3||u.isMatrix4||u.isVector2||u.isVector3||u.isVector4||u.isTexture||u.isQuaternion)?u.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),e[i][r]=null):e[i][r]=u.clone():Array.isArray(u)?e[i][r]=u.slice():e[i][r]=u}}return e}function Bn(o){const e={};for(let i=0;i<o.length;i++){const r=uo(o[i]);for(const u in r)e[u]=r[u]}return e}function $E(o){const e=[];for(let i=0;i<o.length;i++)e.push(o[i].clone());return e}function IS(o){const e=o.getRenderTarget();return e===null?o.outputColorSpace:e.isXRRenderTarget===!0?e.texture.colorSpace:De.workingColorSpace}const tT={clone:uo,merge:Bn};var eT=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,nT=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`;class us extends Sl{constructor(e){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=eT,this.fragmentShader=nT,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,e!==void 0&&this.setValues(e)}copy(e){return super.copy(e),this.fragmentShader=e.fragmentShader,this.vertexShader=e.vertexShader,this.uniforms=uo(e.uniforms),this.uniformsGroups=$E(e.uniformsGroups),this.defines=Object.assign({},e.defines),this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.fog=e.fog,this.lights=e.lights,this.clipping=e.clipping,this.extensions=Object.assign({},e.extensions),this.glslVersion=e.glslVersion,this}toJSON(e){const i=super.toJSON(e);i.glslVersion=this.glslVersion,i.uniforms={};for(const u in this.uniforms){const h=this.uniforms[u].value;h&&h.isTexture?i.uniforms[u]={type:"t",value:h.toJSON(e).uuid}:h&&h.isColor?i.uniforms[u]={type:"c",value:h.getHex()}:h&&h.isVector2?i.uniforms[u]={type:"v2",value:h.toArray()}:h&&h.isVector3?i.uniforms[u]={type:"v3",value:h.toArray()}:h&&h.isVector4?i.uniforms[u]={type:"v4",value:h.toArray()}:h&&h.isMatrix3?i.uniforms[u]={type:"m3",value:h.toArray()}:h&&h.isMatrix4?i.uniforms[u]={type:"m4",value:h.toArray()}:i.uniforms[u]={value:h}}Object.keys(this.defines).length>0&&(i.defines=this.defines),i.vertexShader=this.vertexShader,i.fragmentShader=this.fragmentShader,i.lights=this.lights,i.clipping=this.clipping;const r={};for(const u in this.extensions)this.extensions[u]===!0&&(r[u]=!0);return Object.keys(r).length>0&&(i.extensions=r),i}}class BS extends bn{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new Ze,this.projectionMatrix=new Ze,this.projectionMatrixInverse=new Ze,this.coordinateSystem=Ma}copy(e,i){return super.copy(e,i),this.matrixWorldInverse.copy(e.matrixWorldInverse),this.projectionMatrix.copy(e.projectionMatrix),this.projectionMatrixInverse.copy(e.projectionMatrixInverse),this.coordinateSystem=e.coordinateSystem,this}getWorldDirection(e){return super.getWorldDirection(e).negate()}updateMatrixWorld(e){super.updateMatrixWorld(e),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(e,i){super.updateWorldMatrix(e,i),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}}const is=new Q,Pv=new ce,zv=new ce;class Si extends BS{constructor(e=50,i=1,r=.1,u=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=e,this.zoom=1,this.near=r,this.far=u,this.focus=10,this.aspect=i,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(e,i){return super.copy(e,i),this.fov=e.fov,this.zoom=e.zoom,this.near=e.near,this.far=e.far,this.focus=e.focus,this.aspect=e.aspect,this.view=e.view===null?null:Object.assign({},e.view),this.filmGauge=e.filmGauge,this.filmOffset=e.filmOffset,this}setFocalLength(e){const i=.5*this.getFilmHeight()/e;this.fov=Np*2*Math.atan(i),this.updateProjectionMatrix()}getFocalLength(){const e=Math.tan(xc*.5*this.fov);return .5*this.getFilmHeight()/e}getEffectiveFOV(){return Np*2*Math.atan(Math.tan(xc*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(e,i,r){is.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),i.set(is.x,is.y).multiplyScalar(-e/is.z),is.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),r.set(is.x,is.y).multiplyScalar(-e/is.z)}getViewSize(e,i){return this.getViewBounds(e,Pv,zv),i.subVectors(zv,Pv)}setViewOffset(e,i,r,u,f,h){this.aspect=e/i,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=i,this.view.offsetX=r,this.view.offsetY=u,this.view.width=f,this.view.height=h,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const e=this.near;let i=e*Math.tan(xc*.5*this.fov)/this.zoom,r=2*i,u=this.aspect*r,f=-.5*u;const h=this.view;if(this.view!==null&&this.view.enabled){const p=h.fullWidth,g=h.fullHeight;f+=h.offsetX*u/p,i-=h.offsetY*r/g,u*=h.width/p,r*=h.height/g}const d=this.filmOffset;d!==0&&(f+=e*d/this.getFilmWidth()),this.projectionMatrix.makePerspective(f,f+u,i,i-r,e,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){const i=super.toJSON(e);return i.object.fov=this.fov,i.object.zoom=this.zoom,i.object.near=this.near,i.object.far=this.far,i.object.focus=this.focus,i.object.aspect=this.aspect,this.view!==null&&(i.object.view=Object.assign({},this.view)),i.object.filmGauge=this.filmGauge,i.object.filmOffset=this.filmOffset,i}}const jr=-90,Zr=1;class iT extends bn{constructor(e,i,r){super(),this.type="CubeCamera",this.renderTarget=r,this.coordinateSystem=null,this.activeMipmapLevel=0;const u=new Si(jr,Zr,e,i);u.layers=this.layers,this.add(u);const f=new Si(jr,Zr,e,i);f.layers=this.layers,this.add(f);const h=new Si(jr,Zr,e,i);h.layers=this.layers,this.add(h);const d=new Si(jr,Zr,e,i);d.layers=this.layers,this.add(d);const p=new Si(jr,Zr,e,i);p.layers=this.layers,this.add(p);const g=new Si(jr,Zr,e,i);g.layers=this.layers,this.add(g)}updateCoordinateSystem(){const e=this.coordinateSystem,i=this.children.concat(),[r,u,f,h,d,p]=i;for(const g of i)this.remove(g);if(e===Ma)r.up.set(0,1,0),r.lookAt(1,0,0),u.up.set(0,1,0),u.lookAt(-1,0,0),f.up.set(0,0,-1),f.lookAt(0,1,0),h.up.set(0,0,1),h.lookAt(0,-1,0),d.up.set(0,1,0),d.lookAt(0,0,1),p.up.set(0,1,0),p.lookAt(0,0,-1);else if(e===Rc)r.up.set(0,-1,0),r.lookAt(-1,0,0),u.up.set(0,-1,0),u.lookAt(1,0,0),f.up.set(0,0,1),f.lookAt(0,1,0),h.up.set(0,0,-1),h.lookAt(0,-1,0),d.up.set(0,-1,0),d.lookAt(0,0,1),p.up.set(0,-1,0),p.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+e);for(const g of i)this.add(g),g.updateMatrixWorld()}update(e,i){this.parent===null&&this.updateMatrixWorld();const{renderTarget:r,activeMipmapLevel:u}=this;this.coordinateSystem!==e.coordinateSystem&&(this.coordinateSystem=e.coordinateSystem,this.updateCoordinateSystem());const[f,h,d,p,g,v]=this.children,_=e.getRenderTarget(),y=e.getActiveCubeFace(),M=e.getActiveMipmapLevel(),E=e.xr.enabled;e.xr.enabled=!1;const R=r.texture.generateMipmaps;r.texture.generateMipmaps=!1,e.setRenderTarget(r,0,u),e.render(i,f),e.setRenderTarget(r,1,u),e.render(i,h),e.setRenderTarget(r,2,u),e.render(i,d),e.setRenderTarget(r,3,u),e.render(i,p),e.setRenderTarget(r,4,u),e.render(i,g),r.texture.generateMipmaps=R,e.setRenderTarget(r,5,u),e.render(i,v),e.setRenderTarget(_,y,M),e.xr.enabled=E,r.texture.needsPMREMUpdate=!0}}class FS extends Kn{constructor(e,i,r,u,f,h,d,p,g,v){e=e!==void 0?e:[],i=i!==void 0?i:so,super(e,i,r,u,f,h,d,p,g,v),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(e){this.image=e}}class aT extends qs{constructor(e=1,i={}){super(e,e,i),this.isWebGLCubeRenderTarget=!0;const r={width:e,height:e,depth:1},u=[r,r,r,r,r,r];this.texture=new FS(u,i.mapping,i.wrapS,i.wrapT,i.magFilter,i.minFilter,i.format,i.type,i.anisotropy,i.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=i.generateMipmaps!==void 0?i.generateMipmaps:!1,this.texture.minFilter=i.minFilter!==void 0?i.minFilter:Oi}fromEquirectangularTexture(e,i){this.texture.type=i.type,this.texture.colorSpace=i.colorSpace,this.texture.generateMipmaps=i.generateMipmaps,this.texture.minFilter=i.minFilter,this.texture.magFilter=i.magFilter;const r={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},u=new co(5,5,5),f=new us({name:"CubemapFromEquirect",uniforms:uo(r.uniforms),vertexShader:r.vertexShader,fragmentShader:r.fragmentShader,side:Zn,blending:rs});f.uniforms.tEquirect.value=i;const h=new jn(u,f),d=i.minFilter;return i.minFilter===Ys&&(i.minFilter=Oi),new iT(1,10,this).update(e,h),i.minFilter=d,h.geometry.dispose(),h.material.dispose(),this}clear(e,i,r,u){const f=e.getRenderTarget();for(let h=0;h<6;h++)e.setRenderTarget(this,h),e.clear(i,r,u);e.setRenderTarget(f)}}const zd=new Q,sT=new Q,rT=new he;class as{constructor(e=new Q(1,0,0),i=0){this.isPlane=!0,this.normal=e,this.constant=i}set(e,i){return this.normal.copy(e),this.constant=i,this}setComponents(e,i,r,u){return this.normal.set(e,i,r),this.constant=u,this}setFromNormalAndCoplanarPoint(e,i){return this.normal.copy(e),this.constant=-i.dot(this.normal),this}setFromCoplanarPoints(e,i,r){const u=zd.subVectors(r,i).cross(sT.subVectors(e,i)).normalize();return this.setFromNormalAndCoplanarPoint(u,e),this}copy(e){return this.normal.copy(e.normal),this.constant=e.constant,this}normalize(){const e=1/this.normal.length();return this.normal.multiplyScalar(e),this.constant*=e,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(e){return this.normal.dot(e)+this.constant}distanceToSphere(e){return this.distanceToPoint(e.center)-e.radius}projectPoint(e,i){return i.copy(e).addScaledVector(this.normal,-this.distanceToPoint(e))}intersectLine(e,i){const r=e.delta(zd),u=this.normal.dot(r);if(u===0)return this.distanceToPoint(e.start)===0?i.copy(e.start):null;const f=-(e.start.dot(this.normal)+this.constant)/u;return f<0||f>1?null:i.copy(e.start).addScaledVector(r,f)}intersectsLine(e){const i=this.distanceToPoint(e.start),r=this.distanceToPoint(e.end);return i<0&&r>0||r<0&&i>0}intersectsBox(e){return e.intersectsPlane(this)}intersectsSphere(e){return e.intersectsPlane(this)}coplanarPoint(e){return e.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(e,i){const r=i||rT.getNormalMatrix(e),u=this.coplanarPoint(zd).applyMatrix4(e),f=this.normal.applyMatrix3(r).normalize();return this.constant=-u.dot(f),this}translate(e){return this.constant-=e.dot(this.normal),this}equals(e){return e.normal.equals(this.normal)&&e.constant===this.constant}clone(){return new this.constructor().copy(this)}}const Is=new Lc,oc=new Q;class Yp{constructor(e=new as,i=new as,r=new as,u=new as,f=new as,h=new as){this.planes=[e,i,r,u,f,h]}set(e,i,r,u,f,h){const d=this.planes;return d[0].copy(e),d[1].copy(i),d[2].copy(r),d[3].copy(u),d[4].copy(f),d[5].copy(h),this}copy(e){const i=this.planes;for(let r=0;r<6;r++)i[r].copy(e.planes[r]);return this}setFromProjectionMatrix(e,i=Ma){const r=this.planes,u=e.elements,f=u[0],h=u[1],d=u[2],p=u[3],g=u[4],v=u[5],_=u[6],y=u[7],M=u[8],E=u[9],R=u[10],x=u[11],S=u[12],L=u[13],U=u[14],P=u[15];if(r[0].setComponents(p-f,y-g,x-M,P-S).normalize(),r[1].setComponents(p+f,y+g,x+M,P+S).normalize(),r[2].setComponents(p+h,y+v,x+E,P+L).normalize(),r[3].setComponents(p-h,y-v,x-E,P-L).normalize(),r[4].setComponents(p-d,y-_,x-R,P-U).normalize(),i===Ma)r[5].setComponents(p+d,y+_,x+R,P+U).normalize();else if(i===Rc)r[5].setComponents(d,_,R,U).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+i);return this}intersectsObject(e){if(e.boundingSphere!==void 0)e.boundingSphere===null&&e.computeBoundingSphere(),Is.copy(e.boundingSphere).applyMatrix4(e.matrixWorld);else{const i=e.geometry;i.boundingSphere===null&&i.computeBoundingSphere(),Is.copy(i.boundingSphere).applyMatrix4(e.matrixWorld)}return this.intersectsSphere(Is)}intersectsSprite(e){return Is.center.set(0,0,0),Is.radius=.7071067811865476,Is.applyMatrix4(e.matrixWorld),this.intersectsSphere(Is)}intersectsSphere(e){const i=this.planes,r=e.center,u=-e.radius;for(let f=0;f<6;f++)if(i[f].distanceToPoint(r)<u)return!1;return!0}intersectsBox(e){const i=this.planes;for(let r=0;r<6;r++){const u=i[r];if(oc.x=u.normal.x>0?e.max.x:e.min.x,oc.y=u.normal.y>0?e.max.y:e.min.y,oc.z=u.normal.z>0?e.max.z:e.min.z,u.distanceToPoint(oc)<0)return!1}return!0}containsPoint(e){const i=this.planes;for(let r=0;r<6;r++)if(i[r].distanceToPoint(e)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}}function HS(){let o=null,e=!1,i=null,r=null;function u(f,h){i(f,h),r=o.requestAnimationFrame(u)}return{start:function(){e!==!0&&i!==null&&(r=o.requestAnimationFrame(u),e=!0)},stop:function(){o.cancelAnimationFrame(r),e=!1},setAnimationLoop:function(f){i=f},setContext:function(f){o=f}}}function oT(o){const e=new WeakMap;function i(d,p){const g=d.array,v=d.usage,_=g.byteLength,y=o.createBuffer();o.bindBuffer(p,y),o.bufferData(p,g,v),d.onUploadCallback();let M;if(g instanceof Float32Array)M=o.FLOAT;else if(g instanceof Uint16Array)d.isFloat16BufferAttribute?M=o.HALF_FLOAT:M=o.UNSIGNED_SHORT;else if(g instanceof Int16Array)M=o.SHORT;else if(g instanceof Uint32Array)M=o.UNSIGNED_INT;else if(g instanceof Int32Array)M=o.INT;else if(g instanceof Int8Array)M=o.BYTE;else if(g instanceof Uint8Array)M=o.UNSIGNED_BYTE;else if(g instanceof Uint8ClampedArray)M=o.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+g);return{buffer:y,type:M,bytesPerElement:g.BYTES_PER_ELEMENT,version:d.version,size:_}}function r(d,p,g){const v=p.array,_=p.updateRanges;if(o.bindBuffer(g,d),_.length===0)o.bufferSubData(g,0,v);else{_.sort((M,E)=>M.start-E.start);let y=0;for(let M=1;M<_.length;M++){const E=_[y],R=_[M];R.start<=E.start+E.count+1?E.count=Math.max(E.count,R.start+R.count-E.start):(++y,_[y]=R)}_.length=y+1;for(let M=0,E=_.length;M<E;M++){const R=_[M];o.bufferSubData(g,R.start*v.BYTES_PER_ELEMENT,v,R.start,R.count)}p.clearUpdateRanges()}p.onUploadCallback()}function u(d){return d.isInterleavedBufferAttribute&&(d=d.data),e.get(d)}function f(d){d.isInterleavedBufferAttribute&&(d=d.data);const p=e.get(d);p&&(o.deleteBuffer(p.buffer),e.delete(d))}function h(d,p){if(d.isInterleavedBufferAttribute&&(d=d.data),d.isGLBufferAttribute){const v=e.get(d);(!v||v.version<d.version)&&e.set(d,{buffer:d.buffer,type:d.type,bytesPerElement:d.elementSize,version:d.version});return}const g=e.get(d);if(g===void 0)e.set(d,i(d,p));else if(g.version<d.version){if(g.size!==d.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");r(g.buffer,d,p),g.version=d.version}}return{get:u,remove:f,update:h}}class yl extends Qn{constructor(e=1,i=1,r=1,u=1){super(),this.type="PlaneGeometry",this.parameters={width:e,height:i,widthSegments:r,heightSegments:u};const f=e/2,h=i/2,d=Math.floor(r),p=Math.floor(u),g=d+1,v=p+1,_=e/d,y=i/p,M=[],E=[],R=[],x=[];for(let S=0;S<v;S++){const L=S*y-h;for(let U=0;U<g;U++){const P=U*_-f;E.push(P,-L,0),R.push(0,0,1),x.push(U/d),x.push(1-S/p)}}for(let S=0;S<p;S++)for(let L=0;L<d;L++){const U=L+g*S,P=L+g*(S+1),J=L+1+g*(S+1),B=L+1+g*S;M.push(U,P,B),M.push(P,J,B)}this.setIndex(M),this.setAttribute("position",new gn(E,3)),this.setAttribute("normal",new gn(R,3)),this.setAttribute("uv",new gn(x,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new yl(e.width,e.height,e.widthSegments,e.heightSegments)}}var lT=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,uT=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,cT=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,fT=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,hT=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,dT=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,pT=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,mT=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,_T=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec3 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 ).rgb;
	}
#endif`,gT=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,vT=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,ST=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,yT=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,xT=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,MT=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,ET=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,TT=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,bT=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,AT=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,RT=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,CT=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,wT=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec3 vColor;
#endif`,DT=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif
#ifdef USE_BATCHING_COLOR
	vec3 batchingColor = getBatchingColor( getIndirectIndex( gl_DrawID ) );
	vColor.xyz *= batchingColor.xyz;
#endif`,UT=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
vec3 inverseTransformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( vec4( dir, 0.0 ) * matrix ).xyz );
}
mat3 transposeMat3( const in mat3 m ) {
	mat3 tmp;
	tmp[ 0 ] = vec3( m[ 0 ].x, m[ 1 ].x, m[ 2 ].x );
	tmp[ 1 ] = vec3( m[ 0 ].y, m[ 1 ].y, m[ 2 ].y );
	tmp[ 2 ] = vec3( m[ 0 ].z, m[ 1 ].z, m[ 2 ].z );
	return tmp;
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,NT=`#ifdef ENVMAP_TYPE_CUBE_UV
	#define cubeUV_minMipLevel 4.0
	#define cubeUV_minTileSize 16.0
	float getFace( vec3 direction ) {
		vec3 absDirection = abs( direction );
		float face = - 1.0;
		if ( absDirection.x > absDirection.z ) {
			if ( absDirection.x > absDirection.y )
				face = direction.x > 0.0 ? 0.0 : 3.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		} else {
			if ( absDirection.z > absDirection.y )
				face = direction.z > 0.0 ? 2.0 : 5.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		}
		return face;
	}
	vec2 getUV( vec3 direction, float face ) {
		vec2 uv;
		if ( face == 0.0 ) {
			uv = vec2( direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 1.0 ) {
			uv = vec2( - direction.x, - direction.z ) / abs( direction.y );
		} else if ( face == 2.0 ) {
			uv = vec2( - direction.x, direction.y ) / abs( direction.z );
		} else if ( face == 3.0 ) {
			uv = vec2( - direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 4.0 ) {
			uv = vec2( - direction.x, direction.z ) / abs( direction.y );
		} else {
			uv = vec2( direction.x, direction.y ) / abs( direction.z );
		}
		return 0.5 * ( uv + 1.0 );
	}
	vec3 bilinearCubeUV( sampler2D envMap, vec3 direction, float mipInt ) {
		float face = getFace( direction );
		float filterInt = max( cubeUV_minMipLevel - mipInt, 0.0 );
		mipInt = max( mipInt, cubeUV_minMipLevel );
		float faceSize = exp2( mipInt );
		highp vec2 uv = getUV( direction, face ) * ( faceSize - 2.0 ) + 1.0;
		if ( face > 2.0 ) {
			uv.y += faceSize;
			face -= 3.0;
		}
		uv.x += face * faceSize;
		uv.x += filterInt * 3.0 * cubeUV_minTileSize;
		uv.y += 4.0 * ( exp2( CUBEUV_MAX_MIP ) - faceSize );
		uv.x *= CUBEUV_TEXEL_WIDTH;
		uv.y *= CUBEUV_TEXEL_HEIGHT;
		#ifdef texture2DGradEXT
			return texture2DGradEXT( envMap, uv, vec2( 0.0 ), vec2( 0.0 ) ).rgb;
		#else
			return texture2D( envMap, uv ).rgb;
		#endif
	}
	#define cubeUV_r0 1.0
	#define cubeUV_m0 - 2.0
	#define cubeUV_r1 0.8
	#define cubeUV_m1 - 1.0
	#define cubeUV_r4 0.4
	#define cubeUV_m4 2.0
	#define cubeUV_r5 0.305
	#define cubeUV_m5 3.0
	#define cubeUV_r6 0.21
	#define cubeUV_m6 4.0
	float roughnessToMip( float roughness ) {
		float mip = 0.0;
		if ( roughness >= cubeUV_r1 ) {
			mip = ( cubeUV_r0 - roughness ) * ( cubeUV_m1 - cubeUV_m0 ) / ( cubeUV_r0 - cubeUV_r1 ) + cubeUV_m0;
		} else if ( roughness >= cubeUV_r4 ) {
			mip = ( cubeUV_r1 - roughness ) * ( cubeUV_m4 - cubeUV_m1 ) / ( cubeUV_r1 - cubeUV_r4 ) + cubeUV_m1;
		} else if ( roughness >= cubeUV_r5 ) {
			mip = ( cubeUV_r4 - roughness ) * ( cubeUV_m5 - cubeUV_m4 ) / ( cubeUV_r4 - cubeUV_r5 ) + cubeUV_m4;
		} else if ( roughness >= cubeUV_r6 ) {
			mip = ( cubeUV_r5 - roughness ) * ( cubeUV_m6 - cubeUV_m5 ) / ( cubeUV_r5 - cubeUV_r6 ) + cubeUV_m5;
		} else {
			mip = - 2.0 * log2( 1.16 * roughness );		}
		return mip;
	}
	vec4 textureCubeUV( sampler2D envMap, vec3 sampleDir, float roughness ) {
		float mip = clamp( roughnessToMip( roughness ), cubeUV_m0, CUBEUV_MAX_MIP );
		float mipF = fract( mip );
		float mipInt = floor( mip );
		vec3 color0 = bilinearCubeUV( envMap, sampleDir, mipInt );
		if ( mipF == 0.0 ) {
			return vec4( color0, 1.0 );
		} else {
			vec3 color1 = bilinearCubeUV( envMap, sampleDir, mipInt + 1.0 );
			return vec4( mix( color0, color1, mipF ), 1.0 );
		}
	}
#endif`,LT=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
	#ifdef FLIP_SIDED
		transformedTangent = - transformedTangent;
	#endif
#endif`,OT=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,PT=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,zT=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,IT=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,BT="gl_FragColor = linearToOutputTexel( gl_FragColor );",FT=`
const mat3 LINEAR_SRGB_TO_LINEAR_DISPLAY_P3 = mat3(
	vec3( 0.8224621, 0.177538, 0.0 ),
	vec3( 0.0331941, 0.9668058, 0.0 ),
	vec3( 0.0170827, 0.0723974, 0.9105199 )
);
const mat3 LINEAR_DISPLAY_P3_TO_LINEAR_SRGB = mat3(
	vec3( 1.2249401, - 0.2249404, 0.0 ),
	vec3( - 0.0420569, 1.0420571, 0.0 ),
	vec3( - 0.0196376, - 0.0786361, 1.0982735 )
);
vec4 LinearSRGBToLinearDisplayP3( in vec4 value ) {
	return vec4( value.rgb * LINEAR_SRGB_TO_LINEAR_DISPLAY_P3, value.a );
}
vec4 LinearDisplayP3ToLinearSRGB( in vec4 value ) {
	return vec4( value.rgb * LINEAR_DISPLAY_P3_TO_LINEAR_SRGB, value.a );
}
vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,HT=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * vec3( flipEnvMap * reflectVec.x, reflectVec.yz ) );
	#else
		vec4 envColor = vec4( 0.0 );
	#endif
	#ifdef ENVMAP_BLENDING_MULTIPLY
		outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_MIX )
		outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_ADD )
		outgoingLight += envColor.xyz * specularStrength * reflectivity;
	#endif
#endif`,GT=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	uniform mat3 envMapRotation;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,VT=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,XT=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,YT=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,kT=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,qT=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,WT=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,jT=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,ZT=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,KT=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,QT=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,JT=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,$T=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif`,tb=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * worldNormal, 1.0 );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, roughness * roughness) );
			reflectVec = inverseTransformDirection( reflectVec, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * reflectVec, roughness );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_CUBE_UV
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
#endif`,eb=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,nb=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,ib=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,ab=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,sb=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb * ( 1.0 - metalnessFactor );
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.0525 );material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = mix( min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = mix( vec3( 0.04 ), diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.0525 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.07, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,rb=`struct PhysicalMaterial {
	vec3 diffuseColor;
	float roughness;
	vec3 specularColor;
	float specularF90;
	float dispersion;
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		float v = 0.5 / ( gv + gl );
		return saturate(v);
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = material.clearcoatRoughness;
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColor;
	float f90 = material.specularF90;
	float roughness = material.roughness;
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float V = V_GGX_SmithCorrelated_Anisotropic( material.alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( material.alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transposeMat3( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float a = roughness < 0.25 ? -339.2 * r2 + 161.4 * roughness - 25.9 : -8.48 * r2 + 14.3 * roughness - 9.95;
	float b = roughness < 0.25 ? 44.0 * r2 - 23.7 * roughness + 3.26 : 1.97 * r2 - 3.27 * roughness + 0.72;
	float DG = exp( a * dotNV + b ) + ( roughness < 0.25 ? 0.0 : 0.1 * ( roughness - 0.25 ) );
	return saturate( DG * RECIPROCAL_PI );
}
vec2 DFGApprox( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	const vec4 c0 = vec4( - 1, - 0.0275, - 0.572, 0.022 );
	const vec4 c1 = vec4( 1, 0.0425, 1.04, - 0.04 );
	vec4 r = roughness * c0 + c1;
	float a004 = min( r.x * r.x, exp2( - 9.28 * dotNV ) ) * r.x + r.y;
	vec2 fab = vec2( - 1.04, 1.04 ) * a004 + r.zw;
	return fab;
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColor * t2.x + ( vec3( 1.0 ) - material.specularColor ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseColor * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
	#endif
	reflectedLight.directSpecular += irradiance * BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
	#endif
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.iridescence, material.iridescenceFresnel, material.roughness, singleScattering, multiScattering );
	#else
		computeMultiscattering( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.roughness, singleScattering, multiScattering );
	#endif
	vec3 totalScattering = singleScattering + multiScattering;
	vec3 diffuse = material.diffuseColor * ( 1.0 - max( max( totalScattering.r, totalScattering.g ), totalScattering.b ) );
	reflectedLight.indirectSpecular += radiance * singleScattering;
	reflectedLight.indirectSpecular += multiScattering * cosineWeightedIrradiance;
	reflectedLight.indirectDiffuse += diffuse * cosineWeightedIrradiance;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,ob=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		material.iridescenceFresnel = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		material.iridescenceF0 = Schlick_to_F0( material.iridescenceFresnel, 1.0, dotNVi );
	}
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,lb=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD ) && defined( ENVMAP_TYPE_CUBE_UV )
		iblIrradiance += getIBLIrradiance( geometryNormal );
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		radiance += getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		radiance += getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,ub=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,cb=`#if defined( USE_LOGDEPTHBUF )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,fb=`#if defined( USE_LOGDEPTHBUF )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,hb=`#ifdef USE_LOGDEPTHBUF
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,db=`#ifdef USE_LOGDEPTHBUF
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,pb=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = vec4( mix( pow( sampledDiffuseColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), sampledDiffuseColor.rgb * 0.0773993808, vec3( lessThanEqual( sampledDiffuseColor.rgb, vec3( 0.04045 ) ) ) ), sampledDiffuseColor.w );
	
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,mb=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,_b=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,gb=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,vb=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,Sb=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,yb=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,xb=`#if defined( USE_MORPHCOLORS )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,Mb=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,Eb=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,Tb=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,bb=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,Ab=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,Rb=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,Cb=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,wb=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,Db=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,Ub=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,Nb=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,Lb=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,Ob=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,Pb=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,zb=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return depth * ( near - far ) - near;
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return ( near * far ) / ( ( far - near ) * depth - far );
}`,Ib=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,Bb=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,Fb=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,Hb=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,Gb=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,Vb=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,Xb=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform sampler2D pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	float texture2DCompare( sampler2D depths, vec2 uv, float compare ) {
		return step( compare, unpackRGBAToDepth( texture2D( depths, uv ) ) );
	}
	vec2 texture2DDistribution( sampler2D shadow, vec2 uv ) {
		return unpackRGBATo2Half( texture2D( shadow, uv ) );
	}
	float VSMShadow (sampler2D shadow, vec2 uv, float compare ){
		float occlusion = 1.0;
		vec2 distribution = texture2DDistribution( shadow, uv );
		float hard_shadow = step( compare , distribution.x );
		if (hard_shadow != 1.0 ) {
			float distance = compare - distribution.x ;
			float variance = max( 0.00000, distribution.y * distribution.y );
			float softness_probability = variance / (variance + distance * distance );			softness_probability = clamp( ( softness_probability - 0.3 ) / ( 0.95 - 0.3 ), 0.0, 1.0 );			occlusion = clamp( max( hard_shadow, softness_probability ), 0.0, 1.0 );
		}
		return occlusion;
	}
	float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
		float shadow = 1.0;
		shadowCoord.xyz /= shadowCoord.w;
		shadowCoord.z += shadowBias;
		bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
		bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
		if ( frustumTest ) {
		#if defined( SHADOWMAP_TYPE_PCF )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx0 = - texelSize.x * shadowRadius;
			float dy0 = - texelSize.y * shadowRadius;
			float dx1 = + texelSize.x * shadowRadius;
			float dy1 = + texelSize.y * shadowRadius;
			float dx2 = dx0 / 2.0;
			float dy2 = dy0 / 2.0;
			float dx3 = dx1 / 2.0;
			float dy3 = dy1 / 2.0;
			shadow = (
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy1 ), shadowCoord.z )
			) * ( 1.0 / 17.0 );
		#elif defined( SHADOWMAP_TYPE_PCF_SOFT )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx = texelSize.x;
			float dy = texelSize.y;
			vec2 uv = shadowCoord.xy;
			vec2 f = fract( uv * shadowMapSize + 0.5 );
			uv -= f * texelSize;
			shadow = (
				texture2DCompare( shadowMap, uv, shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( dx, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( 0.0, dy ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + texelSize, shadowCoord.z ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, 0.0 ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 0.0 ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, dy ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( 0.0, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 0.0, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( texture2DCompare( shadowMap, uv + vec2( dx, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( dx, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( mix( texture2DCompare( shadowMap, uv + vec2( -dx, -dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, -dy ), shadowCoord.z ),
						  f.x ),
					 mix( texture2DCompare( shadowMap, uv + vec2( -dx, 2.0 * dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 2.0 * dy ), shadowCoord.z ),
						  f.x ),
					 f.y )
			) * ( 1.0 / 9.0 );
		#elif defined( SHADOWMAP_TYPE_VSM )
			shadow = VSMShadow( shadowMap, shadowCoord.xy, shadowCoord.z );
		#else
			shadow = texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z );
		#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	vec2 cubeToUV( vec3 v, float texelSizeY ) {
		vec3 absV = abs( v );
		float scaleToCube = 1.0 / max( absV.x, max( absV.y, absV.z ) );
		absV *= scaleToCube;
		v *= scaleToCube * ( 1.0 - 2.0 * texelSizeY );
		vec2 planar = v.xy;
		float almostATexel = 1.5 * texelSizeY;
		float almostOne = 1.0 - almostATexel;
		if ( absV.z >= almostOne ) {
			if ( v.z > 0.0 )
				planar.x = 4.0 - v.x;
		} else if ( absV.x >= almostOne ) {
			float signX = sign( v.x );
			planar.x = v.z * signX + 2.0 * signX;
		} else if ( absV.y >= almostOne ) {
			float signY = sign( v.y );
			planar.x = v.x + 2.0 * signY + 2.0;
			planar.y = v.z * signY - 2.0;
		}
		return vec2( 0.125, 0.25 ) * planar + vec2( 0.375, 0.75 );
	}
	float getPointShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		
		float lightToPositionLength = length( lightToPosition );
		if ( lightToPositionLength - shadowCameraFar <= 0.0 && lightToPositionLength - shadowCameraNear >= 0.0 ) {
			float dp = ( lightToPositionLength - shadowCameraNear ) / ( shadowCameraFar - shadowCameraNear );			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			vec2 texelSize = vec2( 1.0 ) / ( shadowMapSize * vec2( 4.0, 2.0 ) );
			#if defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_PCF_SOFT ) || defined( SHADOWMAP_TYPE_VSM )
				vec2 offset = vec2( - 1, 1 ) * shadowRadius * texelSize.y;
				shadow = (
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxx, texelSize.y ), dp )
				) * ( 1.0 / 9.0 );
			#else
				shadow = texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp );
			#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
#endif`,Yb=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,kb=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	vec3 shadowWorldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,qb=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,Wb=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,jb=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,Zb=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,Kb=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,Qb=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,Jb=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,$b=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,t1=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,e1=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = inverseTransformDirection( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseColor, material.specularColor, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,n1=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
		
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
		
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		
		#else
		
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,i1=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,a1=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,s1=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,r1=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`;const o1=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,l1=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,u1=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,c1=`#ifdef ENVMAP_TYPE_CUBE
	uniform samplerCube envMap;
#elif defined( ENVMAP_TYPE_CUBE_UV )
	uniform sampler2D envMap;
#endif
uniform float flipEnvMap;
uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <cube_uv_reflection_fragment>
void main() {
	#ifdef ENVMAP_TYPE_CUBE
		vec4 texColor = textureCube( envMap, backgroundRotation * vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) );
	#elif defined( ENVMAP_TYPE_CUBE_UV )
		vec4 texColor = textureCubeUV( envMap, backgroundRotation * vWorldDirection, backgroundBlurriness );
	#else
		vec4 texColor = vec4( 0.0, 0.0, 0.0, 1.0 );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,f1=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,h1=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,d1=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,p1=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	float fragCoordZ = 0.5 * vHighPrecisionZW[0] / vHighPrecisionZW[1] + 0.5;
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,m1=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,_1=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main () {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = packDepthToRGBA( dist );
}`,g1=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,v1=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,S1=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,y1=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,x1=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,M1=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,E1=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,T1=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,b1=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,A1=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,R1=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,C1=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <packing>
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( packNormalToRGB( normal ), diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,w1=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,D1=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,U1=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,N1=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <cube_uv_reflection_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
		float sheenEnergyComp = 1.0 - 0.157 * max3( material.sheenColor );
		outgoingLight = outgoingLight * sheenEnergyComp + sheenSpecularDirect + sheenSpecularIndirect;
	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,L1=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,O1=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,P1=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,z1=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,I1=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,B1=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <packing>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,F1=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,H1=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,fe={alphahash_fragment:lT,alphahash_pars_fragment:uT,alphamap_fragment:cT,alphamap_pars_fragment:fT,alphatest_fragment:hT,alphatest_pars_fragment:dT,aomap_fragment:pT,aomap_pars_fragment:mT,batching_pars_vertex:_T,batching_vertex:gT,begin_vertex:vT,beginnormal_vertex:ST,bsdfs:yT,iridescence_fragment:xT,bumpmap_pars_fragment:MT,clipping_planes_fragment:ET,clipping_planes_pars_fragment:TT,clipping_planes_pars_vertex:bT,clipping_planes_vertex:AT,color_fragment:RT,color_pars_fragment:CT,color_pars_vertex:wT,color_vertex:DT,common:UT,cube_uv_reflection_fragment:NT,defaultnormal_vertex:LT,displacementmap_pars_vertex:OT,displacementmap_vertex:PT,emissivemap_fragment:zT,emissivemap_pars_fragment:IT,colorspace_fragment:BT,colorspace_pars_fragment:FT,envmap_fragment:HT,envmap_common_pars_fragment:GT,envmap_pars_fragment:VT,envmap_pars_vertex:XT,envmap_physical_pars_fragment:tb,envmap_vertex:YT,fog_vertex:kT,fog_pars_vertex:qT,fog_fragment:WT,fog_pars_fragment:jT,gradientmap_pars_fragment:ZT,lightmap_pars_fragment:KT,lights_lambert_fragment:QT,lights_lambert_pars_fragment:JT,lights_pars_begin:$T,lights_toon_fragment:eb,lights_toon_pars_fragment:nb,lights_phong_fragment:ib,lights_phong_pars_fragment:ab,lights_physical_fragment:sb,lights_physical_pars_fragment:rb,lights_fragment_begin:ob,lights_fragment_maps:lb,lights_fragment_end:ub,logdepthbuf_fragment:cb,logdepthbuf_pars_fragment:fb,logdepthbuf_pars_vertex:hb,logdepthbuf_vertex:db,map_fragment:pb,map_pars_fragment:mb,map_particle_fragment:_b,map_particle_pars_fragment:gb,metalnessmap_fragment:vb,metalnessmap_pars_fragment:Sb,morphinstance_vertex:yb,morphcolor_vertex:xb,morphnormal_vertex:Mb,morphtarget_pars_vertex:Eb,morphtarget_vertex:Tb,normal_fragment_begin:bb,normal_fragment_maps:Ab,normal_pars_fragment:Rb,normal_pars_vertex:Cb,normal_vertex:wb,normalmap_pars_fragment:Db,clearcoat_normal_fragment_begin:Ub,clearcoat_normal_fragment_maps:Nb,clearcoat_pars_fragment:Lb,iridescence_pars_fragment:Ob,opaque_fragment:Pb,packing:zb,premultiplied_alpha_fragment:Ib,project_vertex:Bb,dithering_fragment:Fb,dithering_pars_fragment:Hb,roughnessmap_fragment:Gb,roughnessmap_pars_fragment:Vb,shadowmap_pars_fragment:Xb,shadowmap_pars_vertex:Yb,shadowmap_vertex:kb,shadowmask_pars_fragment:qb,skinbase_vertex:Wb,skinning_pars_vertex:jb,skinning_vertex:Zb,skinnormal_vertex:Kb,specularmap_fragment:Qb,specularmap_pars_fragment:Jb,tonemapping_fragment:$b,tonemapping_pars_fragment:t1,transmission_fragment:e1,transmission_pars_fragment:n1,uv_pars_fragment:i1,uv_pars_vertex:a1,uv_vertex:s1,worldpos_vertex:r1,background_vert:o1,background_frag:l1,backgroundCube_vert:u1,backgroundCube_frag:c1,cube_vert:f1,cube_frag:h1,depth_vert:d1,depth_frag:p1,distanceRGBA_vert:m1,distanceRGBA_frag:_1,equirect_vert:g1,equirect_frag:v1,linedashed_vert:S1,linedashed_frag:y1,meshbasic_vert:x1,meshbasic_frag:M1,meshlambert_vert:E1,meshlambert_frag:T1,meshmatcap_vert:b1,meshmatcap_frag:A1,meshnormal_vert:R1,meshnormal_frag:C1,meshphong_vert:w1,meshphong_frag:D1,meshphysical_vert:U1,meshphysical_frag:N1,meshtoon_vert:L1,meshtoon_frag:O1,points_vert:P1,points_frag:z1,shadow_vert:I1,shadow_frag:B1,sprite_vert:F1,sprite_frag:H1},Dt={common:{diffuse:{value:new ye(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new he},alphaMap:{value:null},alphaMapTransform:{value:new he},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new he}},envmap:{envMap:{value:null},envMapRotation:{value:new he},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new he}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new he}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new he},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new he},normalScale:{value:new ce(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new he},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new he}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new he}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new he}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new ye(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new ye(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new he},alphaTest:{value:0},uvTransform:{value:new he}},sprite:{diffuse:{value:new ye(16777215)},opacity:{value:1},center:{value:new ce(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new he},alphaMap:{value:null},alphaMapTransform:{value:new he},alphaTest:{value:0}}},Zi={basic:{uniforms:Bn([Dt.common,Dt.specularmap,Dt.envmap,Dt.aomap,Dt.lightmap,Dt.fog]),vertexShader:fe.meshbasic_vert,fragmentShader:fe.meshbasic_frag},lambert:{uniforms:Bn([Dt.common,Dt.specularmap,Dt.envmap,Dt.aomap,Dt.lightmap,Dt.emissivemap,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,Dt.fog,Dt.lights,{emissive:{value:new ye(0)}}]),vertexShader:fe.meshlambert_vert,fragmentShader:fe.meshlambert_frag},phong:{uniforms:Bn([Dt.common,Dt.specularmap,Dt.envmap,Dt.aomap,Dt.lightmap,Dt.emissivemap,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,Dt.fog,Dt.lights,{emissive:{value:new ye(0)},specular:{value:new ye(1118481)},shininess:{value:30}}]),vertexShader:fe.meshphong_vert,fragmentShader:fe.meshphong_frag},standard:{uniforms:Bn([Dt.common,Dt.envmap,Dt.aomap,Dt.lightmap,Dt.emissivemap,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,Dt.roughnessmap,Dt.metalnessmap,Dt.fog,Dt.lights,{emissive:{value:new ye(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:fe.meshphysical_vert,fragmentShader:fe.meshphysical_frag},toon:{uniforms:Bn([Dt.common,Dt.aomap,Dt.lightmap,Dt.emissivemap,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,Dt.gradientmap,Dt.fog,Dt.lights,{emissive:{value:new ye(0)}}]),vertexShader:fe.meshtoon_vert,fragmentShader:fe.meshtoon_frag},matcap:{uniforms:Bn([Dt.common,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,Dt.fog,{matcap:{value:null}}]),vertexShader:fe.meshmatcap_vert,fragmentShader:fe.meshmatcap_frag},points:{uniforms:Bn([Dt.points,Dt.fog]),vertexShader:fe.points_vert,fragmentShader:fe.points_frag},dashed:{uniforms:Bn([Dt.common,Dt.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:fe.linedashed_vert,fragmentShader:fe.linedashed_frag},depth:{uniforms:Bn([Dt.common,Dt.displacementmap]),vertexShader:fe.depth_vert,fragmentShader:fe.depth_frag},normal:{uniforms:Bn([Dt.common,Dt.bumpmap,Dt.normalmap,Dt.displacementmap,{opacity:{value:1}}]),vertexShader:fe.meshnormal_vert,fragmentShader:fe.meshnormal_frag},sprite:{uniforms:Bn([Dt.sprite,Dt.fog]),vertexShader:fe.sprite_vert,fragmentShader:fe.sprite_frag},background:{uniforms:{uvTransform:{value:new he},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:fe.background_vert,fragmentShader:fe.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new he}},vertexShader:fe.backgroundCube_vert,fragmentShader:fe.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:fe.cube_vert,fragmentShader:fe.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:fe.equirect_vert,fragmentShader:fe.equirect_frag},distanceRGBA:{uniforms:Bn([Dt.common,Dt.displacementmap,{referencePosition:{value:new Q},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:fe.distanceRGBA_vert,fragmentShader:fe.distanceRGBA_frag},shadow:{uniforms:Bn([Dt.lights,Dt.fog,{color:{value:new ye(0)},opacity:{value:1}}]),vertexShader:fe.shadow_vert,fragmentShader:fe.shadow_frag}};Zi.physical={uniforms:Bn([Zi.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new he},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new he},clearcoatNormalScale:{value:new ce(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new he},dispersion:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new he},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new he},sheen:{value:0},sheenColor:{value:new ye(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new he},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new he},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new he},transmissionSamplerSize:{value:new ce},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new he},attenuationDistance:{value:0},attenuationColor:{value:new ye(0)},specularColor:{value:new ye(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new he},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new he},anisotropyVector:{value:new ce},anisotropyMap:{value:null},anisotropyMapTransform:{value:new he}}]),vertexShader:fe.meshphysical_vert,fragmentShader:fe.meshphysical_frag};const lc={r:0,b:0,g:0},Bs=new Ta,G1=new Ze;function V1(o,e,i,r,u,f,h){const d=new ye(0);let p=f===!0?0:1,g,v,_=null,y=0,M=null;function E(L){let U=L.isScene===!0?L.background:null;return U&&U.isTexture&&(U=(L.backgroundBlurriness>0?i:e).get(U)),U}function R(L){let U=!1;const P=E(L);P===null?S(d,p):P&&P.isColor&&(S(P,1),U=!0);const J=o.xr.getEnvironmentBlendMode();J==="additive"?r.buffers.color.setClear(0,0,0,1,h):J==="alpha-blend"&&r.buffers.color.setClear(0,0,0,0,h),(o.autoClear||U)&&(r.buffers.depth.setTest(!0),r.buffers.depth.setMask(!0),r.buffers.color.setMask(!0),o.clear(o.autoClearColor,o.autoClearDepth,o.autoClearStencil))}function x(L,U){const P=E(U);P&&(P.isCubeTexture||P.mapping===Uc)?(v===void 0&&(v=new jn(new co(1,1,1),new us({name:"BackgroundCubeMaterial",uniforms:uo(Zi.backgroundCube.uniforms),vertexShader:Zi.backgroundCube.vertexShader,fragmentShader:Zi.backgroundCube.fragmentShader,side:Zn,depthTest:!1,depthWrite:!1,fog:!1})),v.geometry.deleteAttribute("normal"),v.geometry.deleteAttribute("uv"),v.onBeforeRender=function(J,B,O){this.matrixWorld.copyPosition(O.matrixWorld)},Object.defineProperty(v.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),u.update(v)),Bs.copy(U.backgroundRotation),Bs.x*=-1,Bs.y*=-1,Bs.z*=-1,P.isCubeTexture&&P.isRenderTargetTexture===!1&&(Bs.y*=-1,Bs.z*=-1),v.material.uniforms.envMap.value=P,v.material.uniforms.flipEnvMap.value=P.isCubeTexture&&P.isRenderTargetTexture===!1?-1:1,v.material.uniforms.backgroundBlurriness.value=U.backgroundBlurriness,v.material.uniforms.backgroundIntensity.value=U.backgroundIntensity,v.material.uniforms.backgroundRotation.value.setFromMatrix4(G1.makeRotationFromEuler(Bs)),v.material.toneMapped=De.getTransfer(P.colorSpace)!==Xe,(_!==P||y!==P.version||M!==o.toneMapping)&&(v.material.needsUpdate=!0,_=P,y=P.version,M=o.toneMapping),v.layers.enableAll(),L.unshift(v,v.geometry,v.material,0,0,null)):P&&P.isTexture&&(g===void 0&&(g=new jn(new yl(2,2),new us({name:"BackgroundMaterial",uniforms:uo(Zi.background.uniforms),vertexShader:Zi.background.vertexShader,fragmentShader:Zi.background.fragmentShader,side:ls,depthTest:!1,depthWrite:!1,fog:!1})),g.geometry.deleteAttribute("normal"),Object.defineProperty(g.material,"map",{get:function(){return this.uniforms.t2D.value}}),u.update(g)),g.material.uniforms.t2D.value=P,g.material.uniforms.backgroundIntensity.value=U.backgroundIntensity,g.material.toneMapped=De.getTransfer(P.colorSpace)!==Xe,P.matrixAutoUpdate===!0&&P.updateMatrix(),g.material.uniforms.uvTransform.value.copy(P.matrix),(_!==P||y!==P.version||M!==o.toneMapping)&&(g.material.needsUpdate=!0,_=P,y=P.version,M=o.toneMapping),g.layers.enableAll(),L.unshift(g,g.geometry,g.material,0,0,null))}function S(L,U){L.getRGB(lc,IS(o)),r.buffers.color.setClear(lc.r,lc.g,lc.b,U,h)}return{getClearColor:function(){return d},setClearColor:function(L,U=1){d.set(L),p=U,S(d,p)},getClearAlpha:function(){return p},setClearAlpha:function(L){p=L,S(d,p)},render:R,addToRenderList:x}}function X1(o,e){const i=o.getParameter(o.MAX_VERTEX_ATTRIBS),r={},u=y(null);let f=u,h=!1;function d(T,w,nt,rt,lt){let ft=!1;const H=_(rt,nt,w);f!==H&&(f=H,g(f.object)),ft=M(T,rt,nt,lt),ft&&E(T,rt,nt,lt),lt!==null&&e.update(lt,o.ELEMENT_ARRAY_BUFFER),(ft||h)&&(h=!1,P(T,w,nt,rt),lt!==null&&o.bindBuffer(o.ELEMENT_ARRAY_BUFFER,e.get(lt).buffer))}function p(){return o.createVertexArray()}function g(T){return o.bindVertexArray(T)}function v(T){return o.deleteVertexArray(T)}function _(T,w,nt){const rt=nt.wireframe===!0;let lt=r[T.id];lt===void 0&&(lt={},r[T.id]=lt);let ft=lt[w.id];ft===void 0&&(ft={},lt[w.id]=ft);let H=ft[rt];return H===void 0&&(H=y(p()),ft[rt]=H),H}function y(T){const w=[],nt=[],rt=[];for(let lt=0;lt<i;lt++)w[lt]=0,nt[lt]=0,rt[lt]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:w,enabledAttributes:nt,attributeDivisors:rt,object:T,attributes:{},index:null}}function M(T,w,nt,rt){const lt=f.attributes,ft=w.attributes;let H=0;const at=nt.getAttributes();for(const Z in at)if(at[Z].location>=0){const St=lt[Z];let Pt=ft[Z];if(Pt===void 0&&(Z==="instanceMatrix"&&T.instanceMatrix&&(Pt=T.instanceMatrix),Z==="instanceColor"&&T.instanceColor&&(Pt=T.instanceColor)),St===void 0||St.attribute!==Pt||Pt&&St.data!==Pt.data)return!0;H++}return f.attributesNum!==H||f.index!==rt}function E(T,w,nt,rt){const lt={},ft=w.attributes;let H=0;const at=nt.getAttributes();for(const Z in at)if(at[Z].location>=0){let St=ft[Z];St===void 0&&(Z==="instanceMatrix"&&T.instanceMatrix&&(St=T.instanceMatrix),Z==="instanceColor"&&T.instanceColor&&(St=T.instanceColor));const Pt={};Pt.attribute=St,St&&St.data&&(Pt.data=St.data),lt[Z]=Pt,H++}f.attributes=lt,f.attributesNum=H,f.index=rt}function R(){const T=f.newAttributes;for(let w=0,nt=T.length;w<nt;w++)T[w]=0}function x(T){S(T,0)}function S(T,w){const nt=f.newAttributes,rt=f.enabledAttributes,lt=f.attributeDivisors;nt[T]=1,rt[T]===0&&(o.enableVertexAttribArray(T),rt[T]=1),lt[T]!==w&&(o.vertexAttribDivisor(T,w),lt[T]=w)}function L(){const T=f.newAttributes,w=f.enabledAttributes;for(let nt=0,rt=w.length;nt<rt;nt++)w[nt]!==T[nt]&&(o.disableVertexAttribArray(nt),w[nt]=0)}function U(T,w,nt,rt,lt,ft,H){H===!0?o.vertexAttribIPointer(T,w,nt,lt,ft):o.vertexAttribPointer(T,w,nt,rt,lt,ft)}function P(T,w,nt,rt){R();const lt=rt.attributes,ft=nt.getAttributes(),H=w.defaultAttributeValues;for(const at in ft){const Z=ft[at];if(Z.location>=0){let yt=lt[at];if(yt===void 0&&(at==="instanceMatrix"&&T.instanceMatrix&&(yt=T.instanceMatrix),at==="instanceColor"&&T.instanceColor&&(yt=T.instanceColor)),yt!==void 0){const St=yt.normalized,Pt=yt.itemSize,oe=e.get(yt);if(oe===void 0)continue;const me=oe.buffer,D=oe.type,X=oe.bytesPerElement,dt=D===o.INT||D===o.UNSIGNED_INT||yt.gpuType===zp;if(yt.isInterleavedBufferAttribute){const ht=yt.data,Ct=ht.stride,Rt=yt.offset;if(ht.isInstancedInterleavedBuffer){for(let Ht=0;Ht<Z.locationSize;Ht++)S(Z.location+Ht,ht.meshPerAttribute);T.isInstancedMesh!==!0&&rt._maxInstanceCount===void 0&&(rt._maxInstanceCount=ht.meshPerAttribute*ht.count)}else for(let Ht=0;Ht<Z.locationSize;Ht++)x(Z.location+Ht);o.bindBuffer(o.ARRAY_BUFFER,me);for(let Ht=0;Ht<Z.locationSize;Ht++)U(Z.location+Ht,Pt/Z.locationSize,D,St,Ct*X,(Rt+Pt/Z.locationSize*Ht)*X,dt)}else{if(yt.isInstancedBufferAttribute){for(let ht=0;ht<Z.locationSize;ht++)S(Z.location+ht,yt.meshPerAttribute);T.isInstancedMesh!==!0&&rt._maxInstanceCount===void 0&&(rt._maxInstanceCount=yt.meshPerAttribute*yt.count)}else for(let ht=0;ht<Z.locationSize;ht++)x(Z.location+ht);o.bindBuffer(o.ARRAY_BUFFER,me);for(let ht=0;ht<Z.locationSize;ht++)U(Z.location+ht,Pt/Z.locationSize,D,St,Pt*X,Pt/Z.locationSize*ht*X,dt)}}else if(H!==void 0){const St=H[at];if(St!==void 0)switch(St.length){case 2:o.vertexAttrib2fv(Z.location,St);break;case 3:o.vertexAttrib3fv(Z.location,St);break;case 4:o.vertexAttrib4fv(Z.location,St);break;default:o.vertexAttrib1fv(Z.location,St)}}}}L()}function J(){V();for(const T in r){const w=r[T];for(const nt in w){const rt=w[nt];for(const lt in rt)v(rt[lt].object),delete rt[lt];delete w[nt]}delete r[T]}}function B(T){if(r[T.id]===void 0)return;const w=r[T.id];for(const nt in w){const rt=w[nt];for(const lt in rt)v(rt[lt].object),delete rt[lt];delete w[nt]}delete r[T.id]}function O(T){for(const w in r){const nt=r[w];if(nt[T.id]===void 0)continue;const rt=nt[T.id];for(const lt in rt)v(rt[lt].object),delete rt[lt];delete nt[T.id]}}function V(){gt(),h=!0,f!==u&&(f=u,g(f.object))}function gt(){u.geometry=null,u.program=null,u.wireframe=!1}return{setup:d,reset:V,resetDefaultState:gt,dispose:J,releaseStatesOfGeometry:B,releaseStatesOfProgram:O,initAttributes:R,enableAttribute:x,disableUnusedAttributes:L}}function Y1(o,e,i){let r;function u(g){r=g}function f(g,v){o.drawArrays(r,g,v),i.update(v,r,1)}function h(g,v,_){_!==0&&(o.drawArraysInstanced(r,g,v,_),i.update(v,r,_))}function d(g,v,_){if(_===0)return;e.get("WEBGL_multi_draw").multiDrawArraysWEBGL(r,g,0,v,0,_);let M=0;for(let E=0;E<_;E++)M+=v[E];i.update(M,r,1)}function p(g,v,_,y){if(_===0)return;const M=e.get("WEBGL_multi_draw");if(M===null)for(let E=0;E<g.length;E++)h(g[E],v[E],y[E]);else{M.multiDrawArraysInstancedWEBGL(r,g,0,v,0,y,0,_);let E=0;for(let R=0;R<_;R++)E+=v[R];for(let R=0;R<y.length;R++)i.update(E,r,y[R])}}this.setMode=u,this.render=f,this.renderInstances=h,this.renderMultiDraw=d,this.renderMultiDrawInstances=p}function k1(o,e,i,r){let u;function f(){if(u!==void 0)return u;if(e.has("EXT_texture_filter_anisotropic")===!0){const O=e.get("EXT_texture_filter_anisotropic");u=o.getParameter(O.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else u=0;return u}function h(O){return!(O!==zi&&r.convert(O)!==o.getParameter(o.IMPLEMENTATION_COLOR_READ_FORMAT))}function d(O){const V=O===_l&&(e.has("EXT_color_buffer_half_float")||e.has("EXT_color_buffer_float"));return!(O!==Ea&&r.convert(O)!==o.getParameter(o.IMPLEMENTATION_COLOR_READ_TYPE)&&O!==xa&&!V)}function p(O){if(O==="highp"){if(o.getShaderPrecisionFormat(o.VERTEX_SHADER,o.HIGH_FLOAT).precision>0&&o.getShaderPrecisionFormat(o.FRAGMENT_SHADER,o.HIGH_FLOAT).precision>0)return"highp";O="mediump"}return O==="mediump"&&o.getShaderPrecisionFormat(o.VERTEX_SHADER,o.MEDIUM_FLOAT).precision>0&&o.getShaderPrecisionFormat(o.FRAGMENT_SHADER,o.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let g=i.precision!==void 0?i.precision:"highp";const v=p(g);v!==g&&(console.warn("THREE.WebGLRenderer:",g,"not supported, using",v,"instead."),g=v);const _=i.logarithmicDepthBuffer===!0,y=i.reverseDepthBuffer===!0&&e.has("EXT_clip_control");if(y===!0){const O=e.get("EXT_clip_control");O.clipControlEXT(O.LOWER_LEFT_EXT,O.ZERO_TO_ONE_EXT)}const M=o.getParameter(o.MAX_TEXTURE_IMAGE_UNITS),E=o.getParameter(o.MAX_VERTEX_TEXTURE_IMAGE_UNITS),R=o.getParameter(o.MAX_TEXTURE_SIZE),x=o.getParameter(o.MAX_CUBE_MAP_TEXTURE_SIZE),S=o.getParameter(o.MAX_VERTEX_ATTRIBS),L=o.getParameter(o.MAX_VERTEX_UNIFORM_VECTORS),U=o.getParameter(o.MAX_VARYING_VECTORS),P=o.getParameter(o.MAX_FRAGMENT_UNIFORM_VECTORS),J=E>0,B=o.getParameter(o.MAX_SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:f,getMaxPrecision:p,textureFormatReadable:h,textureTypeReadable:d,precision:g,logarithmicDepthBuffer:_,reverseDepthBuffer:y,maxTextures:M,maxVertexTextures:E,maxTextureSize:R,maxCubemapSize:x,maxAttributes:S,maxVertexUniforms:L,maxVaryings:U,maxFragmentUniforms:P,vertexTextures:J,maxSamples:B}}function q1(o){const e=this;let i=null,r=0,u=!1,f=!1;const h=new as,d=new he,p={value:null,needsUpdate:!1};this.uniform=p,this.numPlanes=0,this.numIntersection=0,this.init=function(_,y){const M=_.length!==0||y||r!==0||u;return u=y,r=_.length,M},this.beginShadows=function(){f=!0,v(null)},this.endShadows=function(){f=!1},this.setGlobalState=function(_,y){i=v(_,y,0)},this.setState=function(_,y,M){const E=_.clippingPlanes,R=_.clipIntersection,x=_.clipShadows,S=o.get(_);if(!u||E===null||E.length===0||f&&!x)f?v(null):g();else{const L=f?0:r,U=L*4;let P=S.clippingState||null;p.value=P,P=v(E,y,U,M);for(let J=0;J!==U;++J)P[J]=i[J];S.clippingState=P,this.numIntersection=R?this.numPlanes:0,this.numPlanes+=L}};function g(){p.value!==i&&(p.value=i,p.needsUpdate=r>0),e.numPlanes=r,e.numIntersection=0}function v(_,y,M,E){const R=_!==null?_.length:0;let x=null;if(R!==0){if(x=p.value,E!==!0||x===null){const S=M+R*4,L=y.matrixWorldInverse;d.getNormalMatrix(L),(x===null||x.length<S)&&(x=new Float32Array(S));for(let U=0,P=M;U!==R;++U,P+=4)h.copy(_[U]).applyMatrix4(L,d),h.normal.toArray(x,P),x[P+3]=h.constant}p.value=x,p.needsUpdate=!0}return e.numPlanes=R,e.numIntersection=0,x}}function W1(o){let e=new WeakMap;function i(h,d){return d===np?h.mapping=so:d===ip&&(h.mapping=ro),h}function r(h){if(h&&h.isTexture){const d=h.mapping;if(d===np||d===ip)if(e.has(h)){const p=e.get(h).texture;return i(p,h.mapping)}else{const p=h.image;if(p&&p.height>0){const g=new aT(p.height);return g.fromEquirectangularTexture(o,h),e.set(h,g),h.addEventListener("dispose",u),i(g.texture,h.mapping)}else return null}}return h}function u(h){const d=h.target;d.removeEventListener("dispose",u);const p=e.get(d);p!==void 0&&(e.delete(d),p.dispose())}function f(){e=new WeakMap}return{get:r,dispose:f}}class GS extends BS{constructor(e=-1,i=1,r=1,u=-1,f=.1,h=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=e,this.right=i,this.top=r,this.bottom=u,this.near=f,this.far=h,this.updateProjectionMatrix()}copy(e,i){return super.copy(e,i),this.left=e.left,this.right=e.right,this.top=e.top,this.bottom=e.bottom,this.near=e.near,this.far=e.far,this.zoom=e.zoom,this.view=e.view===null?null:Object.assign({},e.view),this}setViewOffset(e,i,r,u,f,h){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=i,this.view.offsetX=r,this.view.offsetY=u,this.view.width=f,this.view.height=h,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const e=(this.right-this.left)/(2*this.zoom),i=(this.top-this.bottom)/(2*this.zoom),r=(this.right+this.left)/2,u=(this.top+this.bottom)/2;let f=r-e,h=r+e,d=u+i,p=u-i;if(this.view!==null&&this.view.enabled){const g=(this.right-this.left)/this.view.fullWidth/this.zoom,v=(this.top-this.bottom)/this.view.fullHeight/this.zoom;f+=g*this.view.offsetX,h=f+g*this.view.width,d-=v*this.view.offsetY,p=d-v*this.view.height}this.projectionMatrix.makeOrthographic(f,h,d,p,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){const i=super.toJSON(e);return i.object.zoom=this.zoom,i.object.left=this.left,i.object.right=this.right,i.object.top=this.top,i.object.bottom=this.bottom,i.object.near=this.near,i.object.far=this.far,this.view!==null&&(i.object.view=Object.assign({},this.view)),i}}const $r=4,Iv=[.125,.215,.35,.446,.526,.582],Vs=20,Id=new GS,Bv=new ye;let Bd=null,Fd=0,Hd=0,Gd=!1;const Hs=(1+Math.sqrt(5))/2,Kr=1/Hs,Fv=[new Q(-Hs,Kr,0),new Q(Hs,Kr,0),new Q(-Kr,0,Hs),new Q(Kr,0,Hs),new Q(0,Hs,-Kr),new Q(0,Hs,Kr),new Q(-1,1,-1),new Q(1,1,-1),new Q(-1,1,1),new Q(1,1,1)];class Hv{constructor(e){this._renderer=e,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(e,i=0,r=.1,u=100){Bd=this._renderer.getRenderTarget(),Fd=this._renderer.getActiveCubeFace(),Hd=this._renderer.getActiveMipmapLevel(),Gd=this._renderer.xr.enabled,this._renderer.xr.enabled=!1,this._setSize(256);const f=this._allocateTargets();return f.depthBuffer=!0,this._sceneToCubeUV(e,r,u,f),i>0&&this._blur(f,0,0,i),this._applyPMREM(f),this._cleanup(f),f}fromEquirectangular(e,i=null){return this._fromTexture(e,i)}fromCubemap(e,i=null){return this._fromTexture(e,i)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=Xv(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=Vv(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(e){this._lodMax=Math.floor(Math.log2(e)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let e=0;e<this._lodPlanes.length;e++)this._lodPlanes[e].dispose()}_cleanup(e){this._renderer.setRenderTarget(Bd,Fd,Hd),this._renderer.xr.enabled=Gd,e.scissorTest=!1,uc(e,0,0,e.width,e.height)}_fromTexture(e,i){e.mapping===so||e.mapping===ro?this._setSize(e.image.length===0?16:e.image[0].width||e.image[0].image.width):this._setSize(e.image.width/4),Bd=this._renderer.getRenderTarget(),Fd=this._renderer.getActiveCubeFace(),Hd=this._renderer.getActiveMipmapLevel(),Gd=this._renderer.xr.enabled,this._renderer.xr.enabled=!1;const r=i||this._allocateTargets();return this._textureToCubeUV(e,r),this._applyPMREM(r),this._cleanup(r),r}_allocateTargets(){const e=3*Math.max(this._cubeSize,112),i=4*this._cubeSize,r={magFilter:Oi,minFilter:Oi,generateMipmaps:!1,type:_l,format:zi,colorSpace:cs,depthBuffer:!1},u=Gv(e,i,r);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==e||this._pingPongRenderTarget.height!==i){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=Gv(e,i,r);const{_lodMax:f}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=j1(f)),this._blurMaterial=Z1(f,e,i)}return u}_compileMaterial(e){const i=new jn(this._lodPlanes[0],e);this._renderer.compile(i,Id)}_sceneToCubeUV(e,i,r,u){const d=new Si(90,1,i,r),p=[1,-1,1,1,1,1],g=[1,1,1,-1,-1,-1],v=this._renderer,_=v.autoClear,y=v.toneMapping;v.getClearColor(Bv),v.toneMapping=os,v.autoClear=!1;const M=new js({name:"PMREM.Background",side:Zn,depthWrite:!1,depthTest:!1}),E=new jn(new co,M);let R=!1;const x=e.background;x?x.isColor&&(M.color.copy(x),e.background=null,R=!0):(M.color.copy(Bv),R=!0);for(let S=0;S<6;S++){const L=S%3;L===0?(d.up.set(0,p[S],0),d.lookAt(g[S],0,0)):L===1?(d.up.set(0,0,p[S]),d.lookAt(0,g[S],0)):(d.up.set(0,p[S],0),d.lookAt(0,0,g[S]));const U=this._cubeSize;uc(u,L*U,S>2?U:0,U,U),v.setRenderTarget(u),R&&v.render(E,d),v.render(e,d)}E.geometry.dispose(),E.material.dispose(),v.toneMapping=y,v.autoClear=_,e.background=x}_textureToCubeUV(e,i){const r=this._renderer,u=e.mapping===so||e.mapping===ro;u?(this._cubemapMaterial===null&&(this._cubemapMaterial=Xv()),this._cubemapMaterial.uniforms.flipEnvMap.value=e.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=Vv());const f=u?this._cubemapMaterial:this._equirectMaterial,h=new jn(this._lodPlanes[0],f),d=f.uniforms;d.envMap.value=e;const p=this._cubeSize;uc(i,0,0,3*p,2*p),r.setRenderTarget(i),r.render(h,Id)}_applyPMREM(e){const i=this._renderer,r=i.autoClear;i.autoClear=!1;const u=this._lodPlanes.length;for(let f=1;f<u;f++){const h=Math.sqrt(this._sigmas[f]*this._sigmas[f]-this._sigmas[f-1]*this._sigmas[f-1]),d=Fv[(u-f-1)%Fv.length];this._blur(e,f-1,f,h,d)}i.autoClear=r}_blur(e,i,r,u,f){const h=this._pingPongRenderTarget;this._halfBlur(e,h,i,r,u,"latitudinal",f),this._halfBlur(h,e,r,r,u,"longitudinal",f)}_halfBlur(e,i,r,u,f,h,d){const p=this._renderer,g=this._blurMaterial;h!=="latitudinal"&&h!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");const v=3,_=new jn(this._lodPlanes[u],g),y=g.uniforms,M=this._sizeLods[r]-1,E=isFinite(f)?Math.PI/(2*M):2*Math.PI/(2*Vs-1),R=f/E,x=isFinite(f)?1+Math.floor(v*R):Vs;x>Vs&&console.warn(`sigmaRadians, ${f}, is too large and will clip, as it requested ${x} samples when the maximum is set to ${Vs}`);const S=[];let L=0;for(let O=0;O<Vs;++O){const V=O/R,gt=Math.exp(-V*V/2);S.push(gt),O===0?L+=gt:O<x&&(L+=2*gt)}for(let O=0;O<S.length;O++)S[O]=S[O]/L;y.envMap.value=e.texture,y.samples.value=x,y.weights.value=S,y.latitudinal.value=h==="latitudinal",d&&(y.poleAxis.value=d);const{_lodMax:U}=this;y.dTheta.value=E,y.mipInt.value=U-r;const P=this._sizeLods[u],J=3*P*(u>U-$r?u-U+$r:0),B=4*(this._cubeSize-P);uc(i,J,B,3*P,2*P),p.setRenderTarget(i),p.render(_,Id)}}function j1(o){const e=[],i=[],r=[];let u=o;const f=o-$r+1+Iv.length;for(let h=0;h<f;h++){const d=Math.pow(2,u);i.push(d);let p=1/d;h>o-$r?p=Iv[h-o+$r-1]:h===0&&(p=0),r.push(p);const g=1/(d-2),v=-g,_=1+g,y=[v,v,_,v,_,_,v,v,_,_,v,_],M=6,E=6,R=3,x=2,S=1,L=new Float32Array(R*E*M),U=new Float32Array(x*E*M),P=new Float32Array(S*E*M);for(let B=0;B<M;B++){const O=B%3*2/3-1,V=B>2?0:-1,gt=[O,V,0,O+2/3,V,0,O+2/3,V+1,0,O,V,0,O+2/3,V+1,0,O,V+1,0];L.set(gt,R*E*B),U.set(y,x*E*B);const T=[B,B,B,B,B,B];P.set(T,S*E*B)}const J=new Qn;J.setAttribute("position",new xi(L,R)),J.setAttribute("uv",new xi(U,x)),J.setAttribute("faceIndex",new xi(P,S)),e.push(J),u>$r&&u--}return{lodPlanes:e,sizeLods:i,sigmas:r}}function Gv(o,e,i){const r=new qs(o,e,i);return r.texture.mapping=Uc,r.texture.name="PMREM.cubeUv",r.scissorTest=!0,r}function uc(o,e,i,r,u){o.viewport.set(e,i,r,u),o.scissor.set(e,i,r,u)}function Z1(o,e,i){const r=new Float32Array(Vs),u=new Q(0,1,0);return new us({name:"SphericalGaussianBlur",defines:{n:Vs,CUBEUV_TEXEL_WIDTH:1/e,CUBEUV_TEXEL_HEIGHT:1/i,CUBEUV_MAX_MIP:`${o}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:r},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:u}},vertexShader:kp(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;
			uniform int samples;
			uniform float weights[ n ];
			uniform bool latitudinal;
			uniform float dTheta;
			uniform float mipInt;
			uniform vec3 poleAxis;

			#define ENVMAP_TYPE_CUBE_UV
			#include <cube_uv_reflection_fragment>

			vec3 getSample( float theta, vec3 axis ) {

				float cosTheta = cos( theta );
				// Rodrigues' axis-angle rotation
				vec3 sampleDirection = vOutputDirection * cosTheta
					+ cross( axis, vOutputDirection ) * sin( theta )
					+ axis * dot( axis, vOutputDirection ) * ( 1.0 - cosTheta );

				return bilinearCubeUV( envMap, sampleDirection, mipInt );

			}

			void main() {

				vec3 axis = latitudinal ? poleAxis : cross( poleAxis, vOutputDirection );

				if ( all( equal( axis, vec3( 0.0 ) ) ) ) {

					axis = vec3( vOutputDirection.z, 0.0, - vOutputDirection.x );

				}

				axis = normalize( axis );

				gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );
				gl_FragColor.rgb += weights[ 0 ] * getSample( 0.0, axis );

				for ( int i = 1; i < n; i++ ) {

					if ( i >= samples ) {

						break;

					}

					float theta = dTheta * float( i );
					gl_FragColor.rgb += weights[ i ] * getSample( -1.0 * theta, axis );
					gl_FragColor.rgb += weights[ i ] * getSample( theta, axis );

				}

			}
		`,blending:rs,depthTest:!1,depthWrite:!1})}function Vv(){return new us({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:kp(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;

			#include <common>

			void main() {

				vec3 outputDirection = normalize( vOutputDirection );
				vec2 uv = equirectUv( outputDirection );

				gl_FragColor = vec4( texture2D ( envMap, uv ).rgb, 1.0 );

			}
		`,blending:rs,depthTest:!1,depthWrite:!1})}function Xv(){return new us({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:kp(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:rs,depthTest:!1,depthWrite:!1})}function kp(){return`

		precision mediump float;
		precision mediump int;

		attribute float faceIndex;

		varying vec3 vOutputDirection;

		// RH coordinate system; PMREM face-indexing convention
		vec3 getDirection( vec2 uv, float face ) {

			uv = 2.0 * uv - 1.0;

			vec3 direction = vec3( uv, 1.0 );

			if ( face == 0.0 ) {

				direction = direction.zyx; // ( 1, v, u ) pos x

			} else if ( face == 1.0 ) {

				direction = direction.xzy;
				direction.xz *= -1.0; // ( -u, 1, -v ) pos y

			} else if ( face == 2.0 ) {

				direction.x *= -1.0; // ( -u, v, 1 ) pos z

			} else if ( face == 3.0 ) {

				direction = direction.zyx;
				direction.xz *= -1.0; // ( -1, v, -u ) neg x

			} else if ( face == 4.0 ) {

				direction = direction.xzy;
				direction.xy *= -1.0; // ( -u, -1, v ) neg y

			} else if ( face == 5.0 ) {

				direction.z *= -1.0; // ( u, v, -1 ) neg z

			}

			return direction;

		}

		void main() {

			vOutputDirection = getDirection( uv, faceIndex );
			gl_Position = vec4( position, 1.0 );

		}
	`}function K1(o){let e=new WeakMap,i=null;function r(d){if(d&&d.isTexture){const p=d.mapping,g=p===np||p===ip,v=p===so||p===ro;if(g||v){let _=e.get(d);const y=_!==void 0?_.texture.pmremVersion:0;if(d.isRenderTargetTexture&&d.pmremVersion!==y)return i===null&&(i=new Hv(o)),_=g?i.fromEquirectangular(d,_):i.fromCubemap(d,_),_.texture.pmremVersion=d.pmremVersion,e.set(d,_),_.texture;if(_!==void 0)return _.texture;{const M=d.image;return g&&M&&M.height>0||v&&M&&u(M)?(i===null&&(i=new Hv(o)),_=g?i.fromEquirectangular(d):i.fromCubemap(d),_.texture.pmremVersion=d.pmremVersion,e.set(d,_),d.addEventListener("dispose",f),_.texture):null}}}return d}function u(d){let p=0;const g=6;for(let v=0;v<g;v++)d[v]!==void 0&&p++;return p===g}function f(d){const p=d.target;p.removeEventListener("dispose",f);const g=e.get(p);g!==void 0&&(e.delete(p),g.dispose())}function h(){e=new WeakMap,i!==null&&(i.dispose(),i=null)}return{get:r,dispose:h}}function Q1(o){const e={};function i(r){if(e[r]!==void 0)return e[r];let u;switch(r){case"WEBGL_depth_texture":u=o.getExtension("WEBGL_depth_texture")||o.getExtension("MOZ_WEBGL_depth_texture")||o.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":u=o.getExtension("EXT_texture_filter_anisotropic")||o.getExtension("MOZ_EXT_texture_filter_anisotropic")||o.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":u=o.getExtension("WEBGL_compressed_texture_s3tc")||o.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||o.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":u=o.getExtension("WEBGL_compressed_texture_pvrtc")||o.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:u=o.getExtension(r)}return e[r]=u,u}return{has:function(r){return i(r)!==null},init:function(){i("EXT_color_buffer_float"),i("WEBGL_clip_cull_distance"),i("OES_texture_float_linear"),i("EXT_color_buffer_half_float"),i("WEBGL_multisampled_render_to_texture"),i("WEBGL_render_shared_exponent")},get:function(r){const u=i(r);return u===null&&Mc("THREE.WebGLRenderer: "+r+" extension not supported."),u}}}function J1(o,e,i,r){const u={},f=new WeakMap;function h(_){const y=_.target;y.index!==null&&e.remove(y.index);for(const E in y.attributes)e.remove(y.attributes[E]);for(const E in y.morphAttributes){const R=y.morphAttributes[E];for(let x=0,S=R.length;x<S;x++)e.remove(R[x])}y.removeEventListener("dispose",h),delete u[y.id];const M=f.get(y);M&&(e.remove(M),f.delete(y)),r.releaseStatesOfGeometry(y),y.isInstancedBufferGeometry===!0&&delete y._maxInstanceCount,i.memory.geometries--}function d(_,y){return u[y.id]===!0||(y.addEventListener("dispose",h),u[y.id]=!0,i.memory.geometries++),y}function p(_){const y=_.attributes;for(const E in y)e.update(y[E],o.ARRAY_BUFFER);const M=_.morphAttributes;for(const E in M){const R=M[E];for(let x=0,S=R.length;x<S;x++)e.update(R[x],o.ARRAY_BUFFER)}}function g(_){const y=[],M=_.index,E=_.attributes.position;let R=0;if(M!==null){const L=M.array;R=M.version;for(let U=0,P=L.length;U<P;U+=3){const J=L[U+0],B=L[U+1],O=L[U+2];y.push(J,B,B,O,O,J)}}else if(E!==void 0){const L=E.array;R=E.version;for(let U=0,P=L.length/3-1;U<P;U+=3){const J=U+0,B=U+1,O=U+2;y.push(J,B,B,O,O,J)}}else return;const x=new(DS(y)?zS:PS)(y,1);x.version=R;const S=f.get(_);S&&e.remove(S),f.set(_,x)}function v(_){const y=f.get(_);if(y){const M=_.index;M!==null&&y.version<M.version&&g(_)}else g(_);return f.get(_)}return{get:d,update:p,getWireframeAttribute:v}}function $1(o,e,i){let r;function u(y){r=y}let f,h;function d(y){f=y.type,h=y.bytesPerElement}function p(y,M){o.drawElements(r,M,f,y*h),i.update(M,r,1)}function g(y,M,E){E!==0&&(o.drawElementsInstanced(r,M,f,y*h,E),i.update(M,r,E))}function v(y,M,E){if(E===0)return;e.get("WEBGL_multi_draw").multiDrawElementsWEBGL(r,M,0,f,y,0,E);let x=0;for(let S=0;S<E;S++)x+=M[S];i.update(x,r,1)}function _(y,M,E,R){if(E===0)return;const x=e.get("WEBGL_multi_draw");if(x===null)for(let S=0;S<y.length;S++)g(y[S]/h,M[S],R[S]);else{x.multiDrawElementsInstancedWEBGL(r,M,0,f,y,0,R,0,E);let S=0;for(let L=0;L<E;L++)S+=M[L];for(let L=0;L<R.length;L++)i.update(S,r,R[L])}}this.setMode=u,this.setIndex=d,this.render=p,this.renderInstances=g,this.renderMultiDraw=v,this.renderMultiDrawInstances=_}function tA(o){const e={geometries:0,textures:0},i={frame:0,calls:0,triangles:0,points:0,lines:0};function r(f,h,d){switch(i.calls++,h){case o.TRIANGLES:i.triangles+=d*(f/3);break;case o.LINES:i.lines+=d*(f/2);break;case o.LINE_STRIP:i.lines+=d*(f-1);break;case o.LINE_LOOP:i.lines+=d*f;break;case o.POINTS:i.points+=d*f;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",h);break}}function u(){i.calls=0,i.triangles=0,i.points=0,i.lines=0}return{memory:e,render:i,programs:null,autoReset:!0,reset:u,update:r}}function eA(o,e,i){const r=new WeakMap,u=new Je;function f(h,d,p){const g=h.morphTargetInfluences,v=d.morphAttributes.position||d.morphAttributes.normal||d.morphAttributes.color,_=v!==void 0?v.length:0;let y=r.get(d);if(y===void 0||y.count!==_){let T=function(){V.dispose(),r.delete(d),d.removeEventListener("dispose",T)};var M=T;y!==void 0&&y.texture.dispose();const E=d.morphAttributes.position!==void 0,R=d.morphAttributes.normal!==void 0,x=d.morphAttributes.color!==void 0,S=d.morphAttributes.position||[],L=d.morphAttributes.normal||[],U=d.morphAttributes.color||[];let P=0;E===!0&&(P=1),R===!0&&(P=2),x===!0&&(P=3);let J=d.attributes.position.count*P,B=1;J>e.maxTextureSize&&(B=Math.ceil(J/e.maxTextureSize),J=e.maxTextureSize);const O=new Float32Array(J*B*4*_),V=new NS(O,J,B,_);V.type=xa,V.needsUpdate=!0;const gt=P*4;for(let w=0;w<_;w++){const nt=S[w],rt=L[w],lt=U[w],ft=J*B*4*w;for(let H=0;H<nt.count;H++){const at=H*gt;E===!0&&(u.fromBufferAttribute(nt,H),O[ft+at+0]=u.x,O[ft+at+1]=u.y,O[ft+at+2]=u.z,O[ft+at+3]=0),R===!0&&(u.fromBufferAttribute(rt,H),O[ft+at+4]=u.x,O[ft+at+5]=u.y,O[ft+at+6]=u.z,O[ft+at+7]=0),x===!0&&(u.fromBufferAttribute(lt,H),O[ft+at+8]=u.x,O[ft+at+9]=u.y,O[ft+at+10]=u.z,O[ft+at+11]=lt.itemSize===4?u.w:1)}}y={count:_,texture:V,size:new ce(J,B)},r.set(d,y),d.addEventListener("dispose",T)}if(h.isInstancedMesh===!0&&h.morphTexture!==null)p.getUniforms().setValue(o,"morphTexture",h.morphTexture,i);else{let E=0;for(let x=0;x<g.length;x++)E+=g[x];const R=d.morphTargetsRelative?1:1-E;p.getUniforms().setValue(o,"morphTargetBaseInfluence",R),p.getUniforms().setValue(o,"morphTargetInfluences",g)}p.getUniforms().setValue(o,"morphTargetsTexture",y.texture,i),p.getUniforms().setValue(o,"morphTargetsTextureSize",y.size)}return{update:f}}function nA(o,e,i,r){let u=new WeakMap;function f(p){const g=r.render.frame,v=p.geometry,_=e.get(p,v);if(u.get(_)!==g&&(e.update(_),u.set(_,g)),p.isInstancedMesh&&(p.hasEventListener("dispose",d)===!1&&p.addEventListener("dispose",d),u.get(p)!==g&&(i.update(p.instanceMatrix,o.ARRAY_BUFFER),p.instanceColor!==null&&i.update(p.instanceColor,o.ARRAY_BUFFER),u.set(p,g))),p.isSkinnedMesh){const y=p.skeleton;u.get(y)!==g&&(y.update(),u.set(y,g))}return _}function h(){u=new WeakMap}function d(p){const g=p.target;g.removeEventListener("dispose",d),i.remove(g.instanceMatrix),g.instanceColor!==null&&i.remove(g.instanceColor)}return{update:f,dispose:h}}class VS extends Kn{constructor(e,i,r,u,f,h,d,p,g,v=no){if(v!==no&&v!==lo)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");r===void 0&&v===no&&(r=ks),r===void 0&&v===lo&&(r=oo),super(null,u,f,h,d,p,v,r,g),this.isDepthTexture=!0,this.image={width:e,height:i},this.magFilter=d!==void 0?d:yi,this.minFilter=p!==void 0?p:yi,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(e){return super.copy(e),this.compareFunction=e.compareFunction,this}toJSON(e){const i=super.toJSON(e);return this.compareFunction!==null&&(i.compareFunction=this.compareFunction),i}}const XS=new Kn,Yv=new VS(1,1),YS=new NS,kS=new VE,qS=new FS,kv=[],qv=[],Wv=new Float32Array(16),jv=new Float32Array(9),Zv=new Float32Array(4);function fo(o,e,i){const r=o[0];if(r<=0||r>0)return o;const u=e*i;let f=kv[u];if(f===void 0&&(f=new Float32Array(u),kv[u]=f),e!==0){r.toArray(f,0);for(let h=1,d=0;h!==e;++h)d+=i,o[h].toArray(f,d)}return f}function fn(o,e){if(o.length!==e.length)return!1;for(let i=0,r=o.length;i<r;i++)if(o[i]!==e[i])return!1;return!0}function hn(o,e){for(let i=0,r=e.length;i<r;i++)o[i]=e[i]}function Oc(o,e){let i=qv[e];i===void 0&&(i=new Int32Array(e),qv[e]=i);for(let r=0;r!==e;++r)i[r]=o.allocateTextureUnit();return i}function iA(o,e){const i=this.cache;i[0]!==e&&(o.uniform1f(this.addr,e),i[0]=e)}function aA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y)&&(o.uniform2f(this.addr,e.x,e.y),i[0]=e.x,i[1]=e.y);else{if(fn(i,e))return;o.uniform2fv(this.addr,e),hn(i,e)}}function sA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z)&&(o.uniform3f(this.addr,e.x,e.y,e.z),i[0]=e.x,i[1]=e.y,i[2]=e.z);else if(e.r!==void 0)(i[0]!==e.r||i[1]!==e.g||i[2]!==e.b)&&(o.uniform3f(this.addr,e.r,e.g,e.b),i[0]=e.r,i[1]=e.g,i[2]=e.b);else{if(fn(i,e))return;o.uniform3fv(this.addr,e),hn(i,e)}}function rA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z||i[3]!==e.w)&&(o.uniform4f(this.addr,e.x,e.y,e.z,e.w),i[0]=e.x,i[1]=e.y,i[2]=e.z,i[3]=e.w);else{if(fn(i,e))return;o.uniform4fv(this.addr,e),hn(i,e)}}function oA(o,e){const i=this.cache,r=e.elements;if(r===void 0){if(fn(i,e))return;o.uniformMatrix2fv(this.addr,!1,e),hn(i,e)}else{if(fn(i,r))return;Zv.set(r),o.uniformMatrix2fv(this.addr,!1,Zv),hn(i,r)}}function lA(o,e){const i=this.cache,r=e.elements;if(r===void 0){if(fn(i,e))return;o.uniformMatrix3fv(this.addr,!1,e),hn(i,e)}else{if(fn(i,r))return;jv.set(r),o.uniformMatrix3fv(this.addr,!1,jv),hn(i,r)}}function uA(o,e){const i=this.cache,r=e.elements;if(r===void 0){if(fn(i,e))return;o.uniformMatrix4fv(this.addr,!1,e),hn(i,e)}else{if(fn(i,r))return;Wv.set(r),o.uniformMatrix4fv(this.addr,!1,Wv),hn(i,r)}}function cA(o,e){const i=this.cache;i[0]!==e&&(o.uniform1i(this.addr,e),i[0]=e)}function fA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y)&&(o.uniform2i(this.addr,e.x,e.y),i[0]=e.x,i[1]=e.y);else{if(fn(i,e))return;o.uniform2iv(this.addr,e),hn(i,e)}}function hA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z)&&(o.uniform3i(this.addr,e.x,e.y,e.z),i[0]=e.x,i[1]=e.y,i[2]=e.z);else{if(fn(i,e))return;o.uniform3iv(this.addr,e),hn(i,e)}}function dA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z||i[3]!==e.w)&&(o.uniform4i(this.addr,e.x,e.y,e.z,e.w),i[0]=e.x,i[1]=e.y,i[2]=e.z,i[3]=e.w);else{if(fn(i,e))return;o.uniform4iv(this.addr,e),hn(i,e)}}function pA(o,e){const i=this.cache;i[0]!==e&&(o.uniform1ui(this.addr,e),i[0]=e)}function mA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y)&&(o.uniform2ui(this.addr,e.x,e.y),i[0]=e.x,i[1]=e.y);else{if(fn(i,e))return;o.uniform2uiv(this.addr,e),hn(i,e)}}function _A(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z)&&(o.uniform3ui(this.addr,e.x,e.y,e.z),i[0]=e.x,i[1]=e.y,i[2]=e.z);else{if(fn(i,e))return;o.uniform3uiv(this.addr,e),hn(i,e)}}function gA(o,e){const i=this.cache;if(e.x!==void 0)(i[0]!==e.x||i[1]!==e.y||i[2]!==e.z||i[3]!==e.w)&&(o.uniform4ui(this.addr,e.x,e.y,e.z,e.w),i[0]=e.x,i[1]=e.y,i[2]=e.z,i[3]=e.w);else{if(fn(i,e))return;o.uniform4uiv(this.addr,e),hn(i,e)}}function vA(o,e,i){const r=this.cache,u=i.allocateTextureUnit();r[0]!==u&&(o.uniform1i(this.addr,u),r[0]=u);let f;this.type===o.SAMPLER_2D_SHADOW?(Yv.compareFunction=wS,f=Yv):f=XS,i.setTexture2D(e||f,u)}function SA(o,e,i){const r=this.cache,u=i.allocateTextureUnit();r[0]!==u&&(o.uniform1i(this.addr,u),r[0]=u),i.setTexture3D(e||kS,u)}function yA(o,e,i){const r=this.cache,u=i.allocateTextureUnit();r[0]!==u&&(o.uniform1i(this.addr,u),r[0]=u),i.setTextureCube(e||qS,u)}function xA(o,e,i){const r=this.cache,u=i.allocateTextureUnit();r[0]!==u&&(o.uniform1i(this.addr,u),r[0]=u),i.setTexture2DArray(e||YS,u)}function MA(o){switch(o){case 5126:return iA;case 35664:return aA;case 35665:return sA;case 35666:return rA;case 35674:return oA;case 35675:return lA;case 35676:return uA;case 5124:case 35670:return cA;case 35667:case 35671:return fA;case 35668:case 35672:return hA;case 35669:case 35673:return dA;case 5125:return pA;case 36294:return mA;case 36295:return _A;case 36296:return gA;case 35678:case 36198:case 36298:case 36306:case 35682:return vA;case 35679:case 36299:case 36307:return SA;case 35680:case 36300:case 36308:case 36293:return yA;case 36289:case 36303:case 36311:case 36292:return xA}}function EA(o,e){o.uniform1fv(this.addr,e)}function TA(o,e){const i=fo(e,this.size,2);o.uniform2fv(this.addr,i)}function bA(o,e){const i=fo(e,this.size,3);o.uniform3fv(this.addr,i)}function AA(o,e){const i=fo(e,this.size,4);o.uniform4fv(this.addr,i)}function RA(o,e){const i=fo(e,this.size,4);o.uniformMatrix2fv(this.addr,!1,i)}function CA(o,e){const i=fo(e,this.size,9);o.uniformMatrix3fv(this.addr,!1,i)}function wA(o,e){const i=fo(e,this.size,16);o.uniformMatrix4fv(this.addr,!1,i)}function DA(o,e){o.uniform1iv(this.addr,e)}function UA(o,e){o.uniform2iv(this.addr,e)}function NA(o,e){o.uniform3iv(this.addr,e)}function LA(o,e){o.uniform4iv(this.addr,e)}function OA(o,e){o.uniform1uiv(this.addr,e)}function PA(o,e){o.uniform2uiv(this.addr,e)}function zA(o,e){o.uniform3uiv(this.addr,e)}function IA(o,e){o.uniform4uiv(this.addr,e)}function BA(o,e,i){const r=this.cache,u=e.length,f=Oc(i,u);fn(r,f)||(o.uniform1iv(this.addr,f),hn(r,f));for(let h=0;h!==u;++h)i.setTexture2D(e[h]||XS,f[h])}function FA(o,e,i){const r=this.cache,u=e.length,f=Oc(i,u);fn(r,f)||(o.uniform1iv(this.addr,f),hn(r,f));for(let h=0;h!==u;++h)i.setTexture3D(e[h]||kS,f[h])}function HA(o,e,i){const r=this.cache,u=e.length,f=Oc(i,u);fn(r,f)||(o.uniform1iv(this.addr,f),hn(r,f));for(let h=0;h!==u;++h)i.setTextureCube(e[h]||qS,f[h])}function GA(o,e,i){const r=this.cache,u=e.length,f=Oc(i,u);fn(r,f)||(o.uniform1iv(this.addr,f),hn(r,f));for(let h=0;h!==u;++h)i.setTexture2DArray(e[h]||YS,f[h])}function VA(o){switch(o){case 5126:return EA;case 35664:return TA;case 35665:return bA;case 35666:return AA;case 35674:return RA;case 35675:return CA;case 35676:return wA;case 5124:case 35670:return DA;case 35667:case 35671:return UA;case 35668:case 35672:return NA;case 35669:case 35673:return LA;case 5125:return OA;case 36294:return PA;case 36295:return zA;case 36296:return IA;case 35678:case 36198:case 36298:case 36306:case 35682:return BA;case 35679:case 36299:case 36307:return FA;case 35680:case 36300:case 36308:case 36293:return HA;case 36289:case 36303:case 36311:case 36292:return GA}}class XA{constructor(e,i,r){this.id=e,this.addr=r,this.cache=[],this.type=i.type,this.setValue=MA(i.type)}}class YA{constructor(e,i,r){this.id=e,this.addr=r,this.cache=[],this.type=i.type,this.size=i.size,this.setValue=VA(i.type)}}class kA{constructor(e){this.id=e,this.seq=[],this.map={}}setValue(e,i,r){const u=this.seq;for(let f=0,h=u.length;f!==h;++f){const d=u[f];d.setValue(e,i[d.id],r)}}}const Vd=/(\w+)(\])?(\[|\.)?/g;function Kv(o,e){o.seq.push(e),o.map[e.id]=e}function qA(o,e,i){const r=o.name,u=r.length;for(Vd.lastIndex=0;;){const f=Vd.exec(r),h=Vd.lastIndex;let d=f[1];const p=f[2]==="]",g=f[3];if(p&&(d=d|0),g===void 0||g==="["&&h+2===u){Kv(i,g===void 0?new XA(d,o,e):new YA(d,o,e));break}else{let _=i.map[d];_===void 0&&(_=new kA(d),Kv(i,_)),i=_}}}class Ec{constructor(e,i){this.seq=[],this.map={};const r=e.getProgramParameter(i,e.ACTIVE_UNIFORMS);for(let u=0;u<r;++u){const f=e.getActiveUniform(i,u),h=e.getUniformLocation(i,f.name);qA(f,h,this)}}setValue(e,i,r,u){const f=this.map[i];f!==void 0&&f.setValue(e,r,u)}setOptional(e,i,r){const u=i[r];u!==void 0&&this.setValue(e,r,u)}static upload(e,i,r,u){for(let f=0,h=i.length;f!==h;++f){const d=i[f],p=r[d.id];p.needsUpdate!==!1&&d.setValue(e,p.value,u)}}static seqWithValue(e,i){const r=[];for(let u=0,f=e.length;u!==f;++u){const h=e[u];h.id in i&&r.push(h)}return r}}function Qv(o,e,i){const r=o.createShader(e);return o.shaderSource(r,i),o.compileShader(r),r}const WA=37297;let jA=0;function ZA(o,e){const i=o.split(`
`),r=[],u=Math.max(e-6,0),f=Math.min(e+6,i.length);for(let h=u;h<f;h++){const d=h+1;r.push(`${d===e?">":" "} ${d}: ${i[h]}`)}return r.join(`
`)}function KA(o){const e=De.getPrimaries(De.workingColorSpace),i=De.getPrimaries(o);let r;switch(e===i?r="":e===Ac&&i===bc?r="LinearDisplayP3ToLinearSRGB":e===bc&&i===Ac&&(r="LinearSRGBToLinearDisplayP3"),o){case cs:case Nc:return[r,"LinearTransferOETF"];case ji:case Vp:return[r,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space:",o),[r,"LinearTransferOETF"]}}function Jv(o,e,i){const r=o.getShaderParameter(e,o.COMPILE_STATUS),u=o.getShaderInfoLog(e).trim();if(r&&u==="")return"";const f=/ERROR: 0:(\d+)/.exec(u);if(f){const h=parseInt(f[1]);return i.toUpperCase()+`

`+u+`

`+ZA(o.getShaderSource(e),h)}else return u}function QA(o,e){const i=KA(e);return`vec4 ${o}( vec4 value ) { return ${i[0]}( ${i[1]}( value ) ); }`}function JA(o,e){let i;switch(e){case hE:i="Linear";break;case dE:i="Reinhard";break;case pE:i="Cineon";break;case mE:i="ACESFilmic";break;case gE:i="AgX";break;case vE:i="Neutral";break;case _E:i="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",e),i="Linear"}return"vec3 "+o+"( vec3 color ) { return "+i+"ToneMapping( color ); }"}const cc=new Q;function $A(){De.getLuminanceCoefficients(cc);const o=cc.x.toFixed(4),e=cc.y.toFixed(4),i=cc.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${o}, ${e}, ${i} );`,"	return dot( weights, rgb );","}"].join(`
`)}function tR(o){return[o.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",o.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(hl).join(`
`)}function eR(o){const e=[];for(const i in o){const r=o[i];r!==!1&&e.push("#define "+i+" "+r)}return e.join(`
`)}function nR(o,e){const i={},r=o.getProgramParameter(e,o.ACTIVE_ATTRIBUTES);for(let u=0;u<r;u++){const f=o.getActiveAttrib(e,u),h=f.name;let d=1;f.type===o.FLOAT_MAT2&&(d=2),f.type===o.FLOAT_MAT3&&(d=3),f.type===o.FLOAT_MAT4&&(d=4),i[h]={type:f.type,location:o.getAttribLocation(e,h),locationSize:d}}return i}function hl(o){return o!==""}function $v(o,e){const i=e.numSpotLightShadows+e.numSpotLightMaps-e.numSpotLightShadowsWithMaps;return o.replace(/NUM_DIR_LIGHTS/g,e.numDirLights).replace(/NUM_SPOT_LIGHTS/g,e.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,e.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,i).replace(/NUM_RECT_AREA_LIGHTS/g,e.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,e.numPointLights).replace(/NUM_HEMI_LIGHTS/g,e.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,e.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,e.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,e.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,e.numPointLightShadows)}function tS(o,e){return o.replace(/NUM_CLIPPING_PLANES/g,e.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,e.numClippingPlanes-e.numClipIntersection)}const iR=/^[ \t]*#include +<([\w\d./]+)>/gm;function Lp(o){return o.replace(iR,sR)}const aR=new Map;function sR(o,e){let i=fe[e];if(i===void 0){const r=aR.get(e);if(r!==void 0)i=fe[r],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',e,r);else throw new Error("Can not resolve #include <"+e+">")}return Lp(i)}const rR=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function eS(o){return o.replace(rR,oR)}function oR(o,e,i,r){let u="";for(let f=parseInt(e);f<parseInt(i);f++)u+=r.replace(/\[\s*i\s*\]/g,"[ "+f+" ]").replace(/UNROLLED_LOOP_INDEX/g,f);return u}function nS(o){let e=`precision ${o.precision} float;
	precision ${o.precision} int;
	precision ${o.precision} sampler2D;
	precision ${o.precision} samplerCube;
	precision ${o.precision} sampler3D;
	precision ${o.precision} sampler2DArray;
	precision ${o.precision} sampler2DShadow;
	precision ${o.precision} samplerCubeShadow;
	precision ${o.precision} sampler2DArrayShadow;
	precision ${o.precision} isampler2D;
	precision ${o.precision} isampler3D;
	precision ${o.precision} isamplerCube;
	precision ${o.precision} isampler2DArray;
	precision ${o.precision} usampler2D;
	precision ${o.precision} usampler3D;
	precision ${o.precision} usamplerCube;
	precision ${o.precision} usampler2DArray;
	`;return o.precision==="highp"?e+=`
#define HIGH_PRECISION`:o.precision==="mediump"?e+=`
#define MEDIUM_PRECISION`:o.precision==="lowp"&&(e+=`
#define LOW_PRECISION`),e}function lR(o){let e="SHADOWMAP_TYPE_BASIC";return o.shadowMapType===_S?e="SHADOWMAP_TYPE_PCF":o.shadowMapType===kM?e="SHADOWMAP_TYPE_PCF_SOFT":o.shadowMapType===ya&&(e="SHADOWMAP_TYPE_VSM"),e}function uR(o){let e="ENVMAP_TYPE_CUBE";if(o.envMap)switch(o.envMapMode){case so:case ro:e="ENVMAP_TYPE_CUBE";break;case Uc:e="ENVMAP_TYPE_CUBE_UV";break}return e}function cR(o){let e="ENVMAP_MODE_REFLECTION";return o.envMap&&o.envMapMode===ro&&(e="ENVMAP_MODE_REFRACTION"),e}function fR(o){let e="ENVMAP_BLENDING_NONE";if(o.envMap)switch(o.combine){case gS:e="ENVMAP_BLENDING_MULTIPLY";break;case cE:e="ENVMAP_BLENDING_MIX";break;case fE:e="ENVMAP_BLENDING_ADD";break}return e}function hR(o){const e=o.envMapCubeUVHeight;if(e===null)return null;const i=Math.log2(e)-2,r=1/e;return{texelWidth:1/(3*Math.max(Math.pow(2,i),112)),texelHeight:r,maxMip:i}}function dR(o,e,i,r){const u=o.getContext(),f=i.defines;let h=i.vertexShader,d=i.fragmentShader;const p=lR(i),g=uR(i),v=cR(i),_=fR(i),y=hR(i),M=tR(i),E=eR(f),R=u.createProgram();let x,S,L=i.glslVersion?"#version "+i.glslVersion+`
`:"";i.isRawShaderMaterial?(x=["#define SHADER_TYPE "+i.shaderType,"#define SHADER_NAME "+i.shaderName,E].filter(hl).join(`
`),x.length>0&&(x+=`
`),S=["#define SHADER_TYPE "+i.shaderType,"#define SHADER_NAME "+i.shaderName,E].filter(hl).join(`
`),S.length>0&&(S+=`
`)):(x=[nS(i),"#define SHADER_TYPE "+i.shaderType,"#define SHADER_NAME "+i.shaderName,E,i.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",i.batching?"#define USE_BATCHING":"",i.batchingColor?"#define USE_BATCHING_COLOR":"",i.instancing?"#define USE_INSTANCING":"",i.instancingColor?"#define USE_INSTANCING_COLOR":"",i.instancingMorph?"#define USE_INSTANCING_MORPH":"",i.useFog&&i.fog?"#define USE_FOG":"",i.useFog&&i.fogExp2?"#define FOG_EXP2":"",i.map?"#define USE_MAP":"",i.envMap?"#define USE_ENVMAP":"",i.envMap?"#define "+v:"",i.lightMap?"#define USE_LIGHTMAP":"",i.aoMap?"#define USE_AOMAP":"",i.bumpMap?"#define USE_BUMPMAP":"",i.normalMap?"#define USE_NORMALMAP":"",i.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",i.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",i.displacementMap?"#define USE_DISPLACEMENTMAP":"",i.emissiveMap?"#define USE_EMISSIVEMAP":"",i.anisotropy?"#define USE_ANISOTROPY":"",i.anisotropyMap?"#define USE_ANISOTROPYMAP":"",i.clearcoatMap?"#define USE_CLEARCOATMAP":"",i.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",i.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",i.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",i.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",i.specularMap?"#define USE_SPECULARMAP":"",i.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",i.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",i.roughnessMap?"#define USE_ROUGHNESSMAP":"",i.metalnessMap?"#define USE_METALNESSMAP":"",i.alphaMap?"#define USE_ALPHAMAP":"",i.alphaHash?"#define USE_ALPHAHASH":"",i.transmission?"#define USE_TRANSMISSION":"",i.transmissionMap?"#define USE_TRANSMISSIONMAP":"",i.thicknessMap?"#define USE_THICKNESSMAP":"",i.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",i.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",i.mapUv?"#define MAP_UV "+i.mapUv:"",i.alphaMapUv?"#define ALPHAMAP_UV "+i.alphaMapUv:"",i.lightMapUv?"#define LIGHTMAP_UV "+i.lightMapUv:"",i.aoMapUv?"#define AOMAP_UV "+i.aoMapUv:"",i.emissiveMapUv?"#define EMISSIVEMAP_UV "+i.emissiveMapUv:"",i.bumpMapUv?"#define BUMPMAP_UV "+i.bumpMapUv:"",i.normalMapUv?"#define NORMALMAP_UV "+i.normalMapUv:"",i.displacementMapUv?"#define DISPLACEMENTMAP_UV "+i.displacementMapUv:"",i.metalnessMapUv?"#define METALNESSMAP_UV "+i.metalnessMapUv:"",i.roughnessMapUv?"#define ROUGHNESSMAP_UV "+i.roughnessMapUv:"",i.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+i.anisotropyMapUv:"",i.clearcoatMapUv?"#define CLEARCOATMAP_UV "+i.clearcoatMapUv:"",i.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+i.clearcoatNormalMapUv:"",i.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+i.clearcoatRoughnessMapUv:"",i.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+i.iridescenceMapUv:"",i.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+i.iridescenceThicknessMapUv:"",i.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+i.sheenColorMapUv:"",i.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+i.sheenRoughnessMapUv:"",i.specularMapUv?"#define SPECULARMAP_UV "+i.specularMapUv:"",i.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+i.specularColorMapUv:"",i.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+i.specularIntensityMapUv:"",i.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+i.transmissionMapUv:"",i.thicknessMapUv?"#define THICKNESSMAP_UV "+i.thicknessMapUv:"",i.vertexTangents&&i.flatShading===!1?"#define USE_TANGENT":"",i.vertexColors?"#define USE_COLOR":"",i.vertexAlphas?"#define USE_COLOR_ALPHA":"",i.vertexUv1s?"#define USE_UV1":"",i.vertexUv2s?"#define USE_UV2":"",i.vertexUv3s?"#define USE_UV3":"",i.pointsUvs?"#define USE_POINTS_UV":"",i.flatShading?"#define FLAT_SHADED":"",i.skinning?"#define USE_SKINNING":"",i.morphTargets?"#define USE_MORPHTARGETS":"",i.morphNormals&&i.flatShading===!1?"#define USE_MORPHNORMALS":"",i.morphColors?"#define USE_MORPHCOLORS":"",i.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+i.morphTextureStride:"",i.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+i.morphTargetsCount:"",i.doubleSided?"#define DOUBLE_SIDED":"",i.flipSided?"#define FLIP_SIDED":"",i.shadowMapEnabled?"#define USE_SHADOWMAP":"",i.shadowMapEnabled?"#define "+p:"",i.sizeAttenuation?"#define USE_SIZEATTENUATION":"",i.numLightProbes>0?"#define USE_LIGHT_PROBES":"",i.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",i.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(hl).join(`
`),S=[nS(i),"#define SHADER_TYPE "+i.shaderType,"#define SHADER_NAME "+i.shaderName,E,i.useFog&&i.fog?"#define USE_FOG":"",i.useFog&&i.fogExp2?"#define FOG_EXP2":"",i.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",i.map?"#define USE_MAP":"",i.matcap?"#define USE_MATCAP":"",i.envMap?"#define USE_ENVMAP":"",i.envMap?"#define "+g:"",i.envMap?"#define "+v:"",i.envMap?"#define "+_:"",y?"#define CUBEUV_TEXEL_WIDTH "+y.texelWidth:"",y?"#define CUBEUV_TEXEL_HEIGHT "+y.texelHeight:"",y?"#define CUBEUV_MAX_MIP "+y.maxMip+".0":"",i.lightMap?"#define USE_LIGHTMAP":"",i.aoMap?"#define USE_AOMAP":"",i.bumpMap?"#define USE_BUMPMAP":"",i.normalMap?"#define USE_NORMALMAP":"",i.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",i.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",i.emissiveMap?"#define USE_EMISSIVEMAP":"",i.anisotropy?"#define USE_ANISOTROPY":"",i.anisotropyMap?"#define USE_ANISOTROPYMAP":"",i.clearcoat?"#define USE_CLEARCOAT":"",i.clearcoatMap?"#define USE_CLEARCOATMAP":"",i.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",i.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",i.dispersion?"#define USE_DISPERSION":"",i.iridescence?"#define USE_IRIDESCENCE":"",i.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",i.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",i.specularMap?"#define USE_SPECULARMAP":"",i.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",i.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",i.roughnessMap?"#define USE_ROUGHNESSMAP":"",i.metalnessMap?"#define USE_METALNESSMAP":"",i.alphaMap?"#define USE_ALPHAMAP":"",i.alphaTest?"#define USE_ALPHATEST":"",i.alphaHash?"#define USE_ALPHAHASH":"",i.sheen?"#define USE_SHEEN":"",i.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",i.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",i.transmission?"#define USE_TRANSMISSION":"",i.transmissionMap?"#define USE_TRANSMISSIONMAP":"",i.thicknessMap?"#define USE_THICKNESSMAP":"",i.vertexTangents&&i.flatShading===!1?"#define USE_TANGENT":"",i.vertexColors||i.instancingColor||i.batchingColor?"#define USE_COLOR":"",i.vertexAlphas?"#define USE_COLOR_ALPHA":"",i.vertexUv1s?"#define USE_UV1":"",i.vertexUv2s?"#define USE_UV2":"",i.vertexUv3s?"#define USE_UV3":"",i.pointsUvs?"#define USE_POINTS_UV":"",i.gradientMap?"#define USE_GRADIENTMAP":"",i.flatShading?"#define FLAT_SHADED":"",i.doubleSided?"#define DOUBLE_SIDED":"",i.flipSided?"#define FLIP_SIDED":"",i.shadowMapEnabled?"#define USE_SHADOWMAP":"",i.shadowMapEnabled?"#define "+p:"",i.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",i.numLightProbes>0?"#define USE_LIGHT_PROBES":"",i.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",i.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",i.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",i.toneMapping!==os?"#define TONE_MAPPING":"",i.toneMapping!==os?fe.tonemapping_pars_fragment:"",i.toneMapping!==os?JA("toneMapping",i.toneMapping):"",i.dithering?"#define DITHERING":"",i.opaque?"#define OPAQUE":"",fe.colorspace_pars_fragment,QA("linearToOutputTexel",i.outputColorSpace),$A(),i.useDepthPacking?"#define DEPTH_PACKING "+i.depthPacking:"",`
`].filter(hl).join(`
`)),h=Lp(h),h=$v(h,i),h=tS(h,i),d=Lp(d),d=$v(d,i),d=tS(d,i),h=eS(h),d=eS(d),i.isRawShaderMaterial!==!0&&(L=`#version 300 es
`,x=[M,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+x,S=["#define varying in",i.glslVersion===Sv?"":"layout(location = 0) out highp vec4 pc_fragColor;",i.glslVersion===Sv?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+S);const U=L+x+h,P=L+S+d,J=Qv(u,u.VERTEX_SHADER,U),B=Qv(u,u.FRAGMENT_SHADER,P);u.attachShader(R,J),u.attachShader(R,B),i.index0AttributeName!==void 0?u.bindAttribLocation(R,0,i.index0AttributeName):i.morphTargets===!0&&u.bindAttribLocation(R,0,"position"),u.linkProgram(R);function O(w){if(o.debug.checkShaderErrors){const nt=u.getProgramInfoLog(R).trim(),rt=u.getShaderInfoLog(J).trim(),lt=u.getShaderInfoLog(B).trim();let ft=!0,H=!0;if(u.getProgramParameter(R,u.LINK_STATUS)===!1)if(ft=!1,typeof o.debug.onShaderError=="function")o.debug.onShaderError(u,R,J,B);else{const at=Jv(u,J,"vertex"),Z=Jv(u,B,"fragment");console.error("THREE.WebGLProgram: Shader Error "+u.getError()+" - VALIDATE_STATUS "+u.getProgramParameter(R,u.VALIDATE_STATUS)+`

Material Name: `+w.name+`
Material Type: `+w.type+`

Program Info Log: `+nt+`
`+at+`
`+Z)}else nt!==""?console.warn("THREE.WebGLProgram: Program Info Log:",nt):(rt===""||lt==="")&&(H=!1);H&&(w.diagnostics={runnable:ft,programLog:nt,vertexShader:{log:rt,prefix:x},fragmentShader:{log:lt,prefix:S}})}u.deleteShader(J),u.deleteShader(B),V=new Ec(u,R),gt=nR(u,R)}let V;this.getUniforms=function(){return V===void 0&&O(this),V};let gt;this.getAttributes=function(){return gt===void 0&&O(this),gt};let T=i.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return T===!1&&(T=u.getProgramParameter(R,WA)),T},this.destroy=function(){r.releaseStatesOfProgram(this),u.deleteProgram(R),this.program=void 0},this.type=i.shaderType,this.name=i.shaderName,this.id=jA++,this.cacheKey=e,this.usedTimes=1,this.program=R,this.vertexShader=J,this.fragmentShader=B,this}let pR=0;class mR{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(e){const i=e.vertexShader,r=e.fragmentShader,u=this._getShaderStage(i),f=this._getShaderStage(r),h=this._getShaderCacheForMaterial(e);return h.has(u)===!1&&(h.add(u),u.usedTimes++),h.has(f)===!1&&(h.add(f),f.usedTimes++),this}remove(e){const i=this.materialCache.get(e);for(const r of i)r.usedTimes--,r.usedTimes===0&&this.shaderCache.delete(r.code);return this.materialCache.delete(e),this}getVertexShaderID(e){return this._getShaderStage(e.vertexShader).id}getFragmentShaderID(e){return this._getShaderStage(e.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(e){const i=this.materialCache;let r=i.get(e);return r===void 0&&(r=new Set,i.set(e,r)),r}_getShaderStage(e){const i=this.shaderCache;let r=i.get(e);return r===void 0&&(r=new _R(e),i.set(e,r)),r}}class _R{constructor(e){this.id=pR++,this.code=e,this.usedTimes=0}}function gR(o,e,i,r,u,f,h){const d=new LS,p=new mR,g=new Set,v=[],_=u.logarithmicDepthBuffer,y=u.reverseDepthBuffer,M=u.vertexTextures;let E=u.precision;const R={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function x(T){return g.add(T),T===0?"uv":`uv${T}`}function S(T,w,nt,rt,lt){const ft=rt.fog,H=lt.geometry,at=T.isMeshStandardMaterial?rt.environment:null,Z=(T.isMeshStandardMaterial?i:e).get(T.envMap||at),yt=Z&&Z.mapping===Uc?Z.image.height:null,St=R[T.type];T.precision!==null&&(E=u.getMaxPrecision(T.precision),E!==T.precision&&console.warn("THREE.WebGLProgram.getParameters:",T.precision,"not supported, using",E,"instead."));const Pt=H.morphAttributes.position||H.morphAttributes.normal||H.morphAttributes.color,oe=Pt!==void 0?Pt.length:0;let me=0;H.morphAttributes.position!==void 0&&(me=1),H.morphAttributes.normal!==void 0&&(me=2),H.morphAttributes.color!==void 0&&(me=3);let D,X,dt,ht;if(St){const tn=Zi[St];D=tn.vertexShader,X=tn.fragmentShader}else D=T.vertexShader,X=T.fragmentShader,p.update(T),dt=p.getVertexShaderID(T),ht=p.getFragmentShaderID(T);const Ct=o.getRenderTarget(),Rt=lt.isInstancedMesh===!0,Ht=lt.isBatchedMesh===!0,Mt=!!T.map,bt=!!T.matcap,F=!!Z,vn=!!T.aoMap,le=!!T.lightMap,ae=!!T.bumpMap,Xt=!!T.normalMap,Kt=!!T.displacementMap,Zt=!!T.emissiveMap,N=!!T.metalnessMap,A=!!T.roughnessMap,tt=T.anisotropy>0,pt=T.clearcoat>0,vt=T.dispersion>0,mt=T.iridescence>0,kt=T.sheen>0,wt=T.transmission>0,It=tt&&!!T.anisotropyMap,ue=pt&&!!T.clearcoatMap,xt=pt&&!!T.clearcoatNormalMap,Bt=pt&&!!T.clearcoatRoughnessMap,te=mt&&!!T.iridescenceMap,$t=mt&&!!T.iridescenceThicknessMap,Ft=kt&&!!T.sheenColorMap,pe=kt&&!!T.sheenRoughnessMap,ee=!!T.specularMap,Oe=!!T.specularColorMap,Y=!!T.specularIntensityMap,Tt=wt&&!!T.transmissionMap,ot=wt&&!!T.thicknessMap,_t=!!T.gradientMap,Lt=!!T.alphaMap,Ot=T.alphaTest>0,xe=!!T.alphaHash,ke=!!T.extensions;let An=os;T.toneMapped&&(Ct===null||Ct.isXRRenderTarget===!0)&&(An=o.toneMapping);const Te={shaderID:St,shaderType:T.type,shaderName:T.name,vertexShader:D,fragmentShader:X,defines:T.defines,customVertexShaderID:dt,customFragmentShaderID:ht,isRawShaderMaterial:T.isRawShaderMaterial===!0,glslVersion:T.glslVersion,precision:E,batching:Ht,batchingColor:Ht&&lt._colorsTexture!==null,instancing:Rt,instancingColor:Rt&&lt.instanceColor!==null,instancingMorph:Rt&&lt.morphTexture!==null,supportsVertexTextures:M,outputColorSpace:Ct===null?o.outputColorSpace:Ct.isXRRenderTarget===!0?Ct.texture.colorSpace:cs,alphaToCoverage:!!T.alphaToCoverage,map:Mt,matcap:bt,envMap:F,envMapMode:F&&Z.mapping,envMapCubeUVHeight:yt,aoMap:vn,lightMap:le,bumpMap:ae,normalMap:Xt,displacementMap:M&&Kt,emissiveMap:Zt,normalMapObjectSpace:Xt&&T.normalMapType===EE,normalMapTangentSpace:Xt&&T.normalMapType===ME,metalnessMap:N,roughnessMap:A,anisotropy:tt,anisotropyMap:It,clearcoat:pt,clearcoatMap:ue,clearcoatNormalMap:xt,clearcoatRoughnessMap:Bt,dispersion:vt,iridescence:mt,iridescenceMap:te,iridescenceThicknessMap:$t,sheen:kt,sheenColorMap:Ft,sheenRoughnessMap:pe,specularMap:ee,specularColorMap:Oe,specularIntensityMap:Y,transmission:wt,transmissionMap:Tt,thicknessMap:ot,gradientMap:_t,opaque:T.transparent===!1&&T.blending===eo&&T.alphaToCoverage===!1,alphaMap:Lt,alphaTest:Ot,alphaHash:xe,combine:T.combine,mapUv:Mt&&x(T.map.channel),aoMapUv:vn&&x(T.aoMap.channel),lightMapUv:le&&x(T.lightMap.channel),bumpMapUv:ae&&x(T.bumpMap.channel),normalMapUv:Xt&&x(T.normalMap.channel),displacementMapUv:Kt&&x(T.displacementMap.channel),emissiveMapUv:Zt&&x(T.emissiveMap.channel),metalnessMapUv:N&&x(T.metalnessMap.channel),roughnessMapUv:A&&x(T.roughnessMap.channel),anisotropyMapUv:It&&x(T.anisotropyMap.channel),clearcoatMapUv:ue&&x(T.clearcoatMap.channel),clearcoatNormalMapUv:xt&&x(T.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:Bt&&x(T.clearcoatRoughnessMap.channel),iridescenceMapUv:te&&x(T.iridescenceMap.channel),iridescenceThicknessMapUv:$t&&x(T.iridescenceThicknessMap.channel),sheenColorMapUv:Ft&&x(T.sheenColorMap.channel),sheenRoughnessMapUv:pe&&x(T.sheenRoughnessMap.channel),specularMapUv:ee&&x(T.specularMap.channel),specularColorMapUv:Oe&&x(T.specularColorMap.channel),specularIntensityMapUv:Y&&x(T.specularIntensityMap.channel),transmissionMapUv:Tt&&x(T.transmissionMap.channel),thicknessMapUv:ot&&x(T.thicknessMap.channel),alphaMapUv:Lt&&x(T.alphaMap.channel),vertexTangents:!!H.attributes.tangent&&(Xt||tt),vertexColors:T.vertexColors,vertexAlphas:T.vertexColors===!0&&!!H.attributes.color&&H.attributes.color.itemSize===4,pointsUvs:lt.isPoints===!0&&!!H.attributes.uv&&(Mt||Lt),fog:!!ft,useFog:T.fog===!0,fogExp2:!!ft&&ft.isFogExp2,flatShading:T.flatShading===!0,sizeAttenuation:T.sizeAttenuation===!0,logarithmicDepthBuffer:_,reverseDepthBuffer:y,skinning:lt.isSkinnedMesh===!0,morphTargets:H.morphAttributes.position!==void 0,morphNormals:H.morphAttributes.normal!==void 0,morphColors:H.morphAttributes.color!==void 0,morphTargetsCount:oe,morphTextureStride:me,numDirLights:w.directional.length,numPointLights:w.point.length,numSpotLights:w.spot.length,numSpotLightMaps:w.spotLightMap.length,numRectAreaLights:w.rectArea.length,numHemiLights:w.hemi.length,numDirLightShadows:w.directionalShadowMap.length,numPointLightShadows:w.pointShadowMap.length,numSpotLightShadows:w.spotShadowMap.length,numSpotLightShadowsWithMaps:w.numSpotLightShadowsWithMaps,numLightProbes:w.numLightProbes,numClippingPlanes:h.numPlanes,numClipIntersection:h.numIntersection,dithering:T.dithering,shadowMapEnabled:o.shadowMap.enabled&&nt.length>0,shadowMapType:o.shadowMap.type,toneMapping:An,decodeVideoTexture:Mt&&T.map.isVideoTexture===!0&&De.getTransfer(T.map.colorSpace)===Xe,premultipliedAlpha:T.premultipliedAlpha,doubleSided:T.side===Li,flipSided:T.side===Zn,useDepthPacking:T.depthPacking>=0,depthPacking:T.depthPacking||0,index0AttributeName:T.index0AttributeName,extensionClipCullDistance:ke&&T.extensions.clipCullDistance===!0&&r.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(ke&&T.extensions.multiDraw===!0||Ht)&&r.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:r.has("KHR_parallel_shader_compile"),customProgramCacheKey:T.customProgramCacheKey()};return Te.vertexUv1s=g.has(1),Te.vertexUv2s=g.has(2),Te.vertexUv3s=g.has(3),g.clear(),Te}function L(T){const w=[];if(T.shaderID?w.push(T.shaderID):(w.push(T.customVertexShaderID),w.push(T.customFragmentShaderID)),T.defines!==void 0)for(const nt in T.defines)w.push(nt),w.push(T.defines[nt]);return T.isRawShaderMaterial===!1&&(U(w,T),P(w,T),w.push(o.outputColorSpace)),w.push(T.customProgramCacheKey),w.join()}function U(T,w){T.push(w.precision),T.push(w.outputColorSpace),T.push(w.envMapMode),T.push(w.envMapCubeUVHeight),T.push(w.mapUv),T.push(w.alphaMapUv),T.push(w.lightMapUv),T.push(w.aoMapUv),T.push(w.bumpMapUv),T.push(w.normalMapUv),T.push(w.displacementMapUv),T.push(w.emissiveMapUv),T.push(w.metalnessMapUv),T.push(w.roughnessMapUv),T.push(w.anisotropyMapUv),T.push(w.clearcoatMapUv),T.push(w.clearcoatNormalMapUv),T.push(w.clearcoatRoughnessMapUv),T.push(w.iridescenceMapUv),T.push(w.iridescenceThicknessMapUv),T.push(w.sheenColorMapUv),T.push(w.sheenRoughnessMapUv),T.push(w.specularMapUv),T.push(w.specularColorMapUv),T.push(w.specularIntensityMapUv),T.push(w.transmissionMapUv),T.push(w.thicknessMapUv),T.push(w.combine),T.push(w.fogExp2),T.push(w.sizeAttenuation),T.push(w.morphTargetsCount),T.push(w.morphAttributeCount),T.push(w.numDirLights),T.push(w.numPointLights),T.push(w.numSpotLights),T.push(w.numSpotLightMaps),T.push(w.numHemiLights),T.push(w.numRectAreaLights),T.push(w.numDirLightShadows),T.push(w.numPointLightShadows),T.push(w.numSpotLightShadows),T.push(w.numSpotLightShadowsWithMaps),T.push(w.numLightProbes),T.push(w.shadowMapType),T.push(w.toneMapping),T.push(w.numClippingPlanes),T.push(w.numClipIntersection),T.push(w.depthPacking)}function P(T,w){d.disableAll(),w.supportsVertexTextures&&d.enable(0),w.instancing&&d.enable(1),w.instancingColor&&d.enable(2),w.instancingMorph&&d.enable(3),w.matcap&&d.enable(4),w.envMap&&d.enable(5),w.normalMapObjectSpace&&d.enable(6),w.normalMapTangentSpace&&d.enable(7),w.clearcoat&&d.enable(8),w.iridescence&&d.enable(9),w.alphaTest&&d.enable(10),w.vertexColors&&d.enable(11),w.vertexAlphas&&d.enable(12),w.vertexUv1s&&d.enable(13),w.vertexUv2s&&d.enable(14),w.vertexUv3s&&d.enable(15),w.vertexTangents&&d.enable(16),w.anisotropy&&d.enable(17),w.alphaHash&&d.enable(18),w.batching&&d.enable(19),w.dispersion&&d.enable(20),w.batchingColor&&d.enable(21),T.push(d.mask),d.disableAll(),w.fog&&d.enable(0),w.useFog&&d.enable(1),w.flatShading&&d.enable(2),w.logarithmicDepthBuffer&&d.enable(3),w.reverseDepthBuffer&&d.enable(4),w.skinning&&d.enable(5),w.morphTargets&&d.enable(6),w.morphNormals&&d.enable(7),w.morphColors&&d.enable(8),w.premultipliedAlpha&&d.enable(9),w.shadowMapEnabled&&d.enable(10),w.doubleSided&&d.enable(11),w.flipSided&&d.enable(12),w.useDepthPacking&&d.enable(13),w.dithering&&d.enable(14),w.transmission&&d.enable(15),w.sheen&&d.enable(16),w.opaque&&d.enable(17),w.pointsUvs&&d.enable(18),w.decodeVideoTexture&&d.enable(19),w.alphaToCoverage&&d.enable(20),T.push(d.mask)}function J(T){const w=R[T.type];let nt;if(w){const rt=Zi[w];nt=tT.clone(rt.uniforms)}else nt=T.uniforms;return nt}function B(T,w){let nt;for(let rt=0,lt=v.length;rt<lt;rt++){const ft=v[rt];if(ft.cacheKey===w){nt=ft,++nt.usedTimes;break}}return nt===void 0&&(nt=new dR(o,w,T,f),v.push(nt)),nt}function O(T){if(--T.usedTimes===0){const w=v.indexOf(T);v[w]=v[v.length-1],v.pop(),T.destroy()}}function V(T){p.remove(T)}function gt(){p.dispose()}return{getParameters:S,getProgramCacheKey:L,getUniforms:J,acquireProgram:B,releaseProgram:O,releaseShaderCache:V,programs:v,dispose:gt}}function vR(){let o=new WeakMap;function e(h){return o.has(h)}function i(h){let d=o.get(h);return d===void 0&&(d={},o.set(h,d)),d}function r(h){o.delete(h)}function u(h,d,p){o.get(h)[d]=p}function f(){o=new WeakMap}return{has:e,get:i,remove:r,update:u,dispose:f}}function SR(o,e){return o.groupOrder!==e.groupOrder?o.groupOrder-e.groupOrder:o.renderOrder!==e.renderOrder?o.renderOrder-e.renderOrder:o.material.id!==e.material.id?o.material.id-e.material.id:o.z!==e.z?o.z-e.z:o.id-e.id}function iS(o,e){return o.groupOrder!==e.groupOrder?o.groupOrder-e.groupOrder:o.renderOrder!==e.renderOrder?o.renderOrder-e.renderOrder:o.z!==e.z?e.z-o.z:o.id-e.id}function aS(){const o=[];let e=0;const i=[],r=[],u=[];function f(){e=0,i.length=0,r.length=0,u.length=0}function h(_,y,M,E,R,x){let S=o[e];return S===void 0?(S={id:_.id,object:_,geometry:y,material:M,groupOrder:E,renderOrder:_.renderOrder,z:R,group:x},o[e]=S):(S.id=_.id,S.object=_,S.geometry=y,S.material=M,S.groupOrder=E,S.renderOrder=_.renderOrder,S.z=R,S.group=x),e++,S}function d(_,y,M,E,R,x){const S=h(_,y,M,E,R,x);M.transmission>0?r.push(S):M.transparent===!0?u.push(S):i.push(S)}function p(_,y,M,E,R,x){const S=h(_,y,M,E,R,x);M.transmission>0?r.unshift(S):M.transparent===!0?u.unshift(S):i.unshift(S)}function g(_,y){i.length>1&&i.sort(_||SR),r.length>1&&r.sort(y||iS),u.length>1&&u.sort(y||iS)}function v(){for(let _=e,y=o.length;_<y;_++){const M=o[_];if(M.id===null)break;M.id=null,M.object=null,M.geometry=null,M.material=null,M.group=null}}return{opaque:i,transmissive:r,transparent:u,init:f,push:d,unshift:p,finish:v,sort:g}}function yR(){let o=new WeakMap;function e(r,u){const f=o.get(r);let h;return f===void 0?(h=new aS,o.set(r,[h])):u>=f.length?(h=new aS,f.push(h)):h=f[u],h}function i(){o=new WeakMap}return{get:e,dispose:i}}function xR(){const o={};return{get:function(e){if(o[e.id]!==void 0)return o[e.id];let i;switch(e.type){case"DirectionalLight":i={direction:new Q,color:new ye};break;case"SpotLight":i={position:new Q,direction:new Q,color:new ye,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":i={position:new Q,color:new ye,distance:0,decay:0};break;case"HemisphereLight":i={direction:new Q,skyColor:new ye,groundColor:new ye};break;case"RectAreaLight":i={color:new ye,position:new Q,halfWidth:new Q,halfHeight:new Q};break}return o[e.id]=i,i}}}function MR(){const o={};return{get:function(e){if(o[e.id]!==void 0)return o[e.id];let i;switch(e.type){case"DirectionalLight":i={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new ce};break;case"SpotLight":i={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new ce};break;case"PointLight":i={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new ce,shadowCameraNear:1,shadowCameraFar:1e3};break}return o[e.id]=i,i}}}let ER=0;function TR(o,e){return(e.castShadow?2:0)-(o.castShadow?2:0)+(e.map?1:0)-(o.map?1:0)}function bR(o){const e=new xR,i=MR(),r={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let g=0;g<9;g++)r.probe.push(new Q);const u=new Q,f=new Ze,h=new Ze;function d(g){let v=0,_=0,y=0;for(let gt=0;gt<9;gt++)r.probe[gt].set(0,0,0);let M=0,E=0,R=0,x=0,S=0,L=0,U=0,P=0,J=0,B=0,O=0;g.sort(TR);for(let gt=0,T=g.length;gt<T;gt++){const w=g[gt],nt=w.color,rt=w.intensity,lt=w.distance,ft=w.shadow&&w.shadow.map?w.shadow.map.texture:null;if(w.isAmbientLight)v+=nt.r*rt,_+=nt.g*rt,y+=nt.b*rt;else if(w.isLightProbe){for(let H=0;H<9;H++)r.probe[H].addScaledVector(w.sh.coefficients[H],rt);O++}else if(w.isDirectionalLight){const H=e.get(w);if(H.color.copy(w.color).multiplyScalar(w.intensity),w.castShadow){const at=w.shadow,Z=i.get(w);Z.shadowIntensity=at.intensity,Z.shadowBias=at.bias,Z.shadowNormalBias=at.normalBias,Z.shadowRadius=at.radius,Z.shadowMapSize=at.mapSize,r.directionalShadow[M]=Z,r.directionalShadowMap[M]=ft,r.directionalShadowMatrix[M]=w.shadow.matrix,L++}r.directional[M]=H,M++}else if(w.isSpotLight){const H=e.get(w);H.position.setFromMatrixPosition(w.matrixWorld),H.color.copy(nt).multiplyScalar(rt),H.distance=lt,H.coneCos=Math.cos(w.angle),H.penumbraCos=Math.cos(w.angle*(1-w.penumbra)),H.decay=w.decay,r.spot[R]=H;const at=w.shadow;if(w.map&&(r.spotLightMap[J]=w.map,J++,at.updateMatrices(w),w.castShadow&&B++),r.spotLightMatrix[R]=at.matrix,w.castShadow){const Z=i.get(w);Z.shadowIntensity=at.intensity,Z.shadowBias=at.bias,Z.shadowNormalBias=at.normalBias,Z.shadowRadius=at.radius,Z.shadowMapSize=at.mapSize,r.spotShadow[R]=Z,r.spotShadowMap[R]=ft,P++}R++}else if(w.isRectAreaLight){const H=e.get(w);H.color.copy(nt).multiplyScalar(rt),H.halfWidth.set(w.width*.5,0,0),H.halfHeight.set(0,w.height*.5,0),r.rectArea[x]=H,x++}else if(w.isPointLight){const H=e.get(w);if(H.color.copy(w.color).multiplyScalar(w.intensity),H.distance=w.distance,H.decay=w.decay,w.castShadow){const at=w.shadow,Z=i.get(w);Z.shadowIntensity=at.intensity,Z.shadowBias=at.bias,Z.shadowNormalBias=at.normalBias,Z.shadowRadius=at.radius,Z.shadowMapSize=at.mapSize,Z.shadowCameraNear=at.camera.near,Z.shadowCameraFar=at.camera.far,r.pointShadow[E]=Z,r.pointShadowMap[E]=ft,r.pointShadowMatrix[E]=w.shadow.matrix,U++}r.point[E]=H,E++}else if(w.isHemisphereLight){const H=e.get(w);H.skyColor.copy(w.color).multiplyScalar(rt),H.groundColor.copy(w.groundColor).multiplyScalar(rt),r.hemi[S]=H,S++}}x>0&&(o.has("OES_texture_float_linear")===!0?(r.rectAreaLTC1=Dt.LTC_FLOAT_1,r.rectAreaLTC2=Dt.LTC_FLOAT_2):(r.rectAreaLTC1=Dt.LTC_HALF_1,r.rectAreaLTC2=Dt.LTC_HALF_2)),r.ambient[0]=v,r.ambient[1]=_,r.ambient[2]=y;const V=r.hash;(V.directionalLength!==M||V.pointLength!==E||V.spotLength!==R||V.rectAreaLength!==x||V.hemiLength!==S||V.numDirectionalShadows!==L||V.numPointShadows!==U||V.numSpotShadows!==P||V.numSpotMaps!==J||V.numLightProbes!==O)&&(r.directional.length=M,r.spot.length=R,r.rectArea.length=x,r.point.length=E,r.hemi.length=S,r.directionalShadow.length=L,r.directionalShadowMap.length=L,r.pointShadow.length=U,r.pointShadowMap.length=U,r.spotShadow.length=P,r.spotShadowMap.length=P,r.directionalShadowMatrix.length=L,r.pointShadowMatrix.length=U,r.spotLightMatrix.length=P+J-B,r.spotLightMap.length=J,r.numSpotLightShadowsWithMaps=B,r.numLightProbes=O,V.directionalLength=M,V.pointLength=E,V.spotLength=R,V.rectAreaLength=x,V.hemiLength=S,V.numDirectionalShadows=L,V.numPointShadows=U,V.numSpotShadows=P,V.numSpotMaps=J,V.numLightProbes=O,r.version=ER++)}function p(g,v){let _=0,y=0,M=0,E=0,R=0;const x=v.matrixWorldInverse;for(let S=0,L=g.length;S<L;S++){const U=g[S];if(U.isDirectionalLight){const P=r.directional[_];P.direction.setFromMatrixPosition(U.matrixWorld),u.setFromMatrixPosition(U.target.matrixWorld),P.direction.sub(u),P.direction.transformDirection(x),_++}else if(U.isSpotLight){const P=r.spot[M];P.position.setFromMatrixPosition(U.matrixWorld),P.position.applyMatrix4(x),P.direction.setFromMatrixPosition(U.matrixWorld),u.setFromMatrixPosition(U.target.matrixWorld),P.direction.sub(u),P.direction.transformDirection(x),M++}else if(U.isRectAreaLight){const P=r.rectArea[E];P.position.setFromMatrixPosition(U.matrixWorld),P.position.applyMatrix4(x),h.identity(),f.copy(U.matrixWorld),f.premultiply(x),h.extractRotation(f),P.halfWidth.set(U.width*.5,0,0),P.halfHeight.set(0,U.height*.5,0),P.halfWidth.applyMatrix4(h),P.halfHeight.applyMatrix4(h),E++}else if(U.isPointLight){const P=r.point[y];P.position.setFromMatrixPosition(U.matrixWorld),P.position.applyMatrix4(x),y++}else if(U.isHemisphereLight){const P=r.hemi[R];P.direction.setFromMatrixPosition(U.matrixWorld),P.direction.transformDirection(x),R++}}}return{setup:d,setupView:p,state:r}}function sS(o){const e=new bR(o),i=[],r=[];function u(v){g.camera=v,i.length=0,r.length=0}function f(v){i.push(v)}function h(v){r.push(v)}function d(){e.setup(i)}function p(v){e.setupView(i,v)}const g={lightsArray:i,shadowsArray:r,camera:null,lights:e,transmissionRenderTarget:{}};return{init:u,state:g,setupLights:d,setupLightsView:p,pushLight:f,pushShadow:h}}function AR(o){let e=new WeakMap;function i(u,f=0){const h=e.get(u);let d;return h===void 0?(d=new sS(o),e.set(u,[d])):f>=h.length?(d=new sS(o),h.push(d)):d=h[f],d}function r(){e=new WeakMap}return{get:i,dispose:r}}class RR extends Sl{constructor(e){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=yE,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(e)}copy(e){return super.copy(e),this.depthPacking=e.depthPacking,this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this}}class CR extends Sl{constructor(e){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(e)}copy(e){return super.copy(e),this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this}}const wR=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,DR=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
#include <packing>
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = unpackRGBATo2Half( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ) );
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = unpackRGBAToDepth( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ) );
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( squared_mean - mean * mean );
	gl_FragColor = pack2HalfToRGBA( vec2( mean, std_dev ) );
}`;function UR(o,e,i){let r=new Yp;const u=new ce,f=new ce,h=new Je,d=new RR({depthPacking:xE}),p=new CR,g={},v=i.maxTextureSize,_={[ls]:Zn,[Zn]:ls,[Li]:Li},y=new us({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new ce},radius:{value:4}},vertexShader:wR,fragmentShader:DR}),M=y.clone();M.defines.HORIZONTAL_PASS=1;const E=new Qn;E.setAttribute("position",new xi(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));const R=new jn(E,y),x=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=_S;let S=this.type;this.render=function(B,O,V){if(x.enabled===!1||x.autoUpdate===!1&&x.needsUpdate===!1||B.length===0)return;const gt=o.getRenderTarget(),T=o.getActiveCubeFace(),w=o.getActiveMipmapLevel(),nt=o.state;nt.setBlending(rs),nt.buffers.color.setClear(1,1,1,1),nt.buffers.depth.setTest(!0),nt.setScissorTest(!1);const rt=S!==ya&&this.type===ya,lt=S===ya&&this.type!==ya;for(let ft=0,H=B.length;ft<H;ft++){const at=B[ft],Z=at.shadow;if(Z===void 0){console.warn("THREE.WebGLShadowMap:",at,"has no shadow.");continue}if(Z.autoUpdate===!1&&Z.needsUpdate===!1)continue;u.copy(Z.mapSize);const yt=Z.getFrameExtents();if(u.multiply(yt),f.copy(Z.mapSize),(u.x>v||u.y>v)&&(u.x>v&&(f.x=Math.floor(v/yt.x),u.x=f.x*yt.x,Z.mapSize.x=f.x),u.y>v&&(f.y=Math.floor(v/yt.y),u.y=f.y*yt.y,Z.mapSize.y=f.y)),Z.map===null||rt===!0||lt===!0){const Pt=this.type!==ya?{minFilter:yi,magFilter:yi}:{};Z.map!==null&&Z.map.dispose(),Z.map=new qs(u.x,u.y,Pt),Z.map.texture.name=at.name+".shadowMap",Z.camera.updateProjectionMatrix()}o.setRenderTarget(Z.map),o.clear();const St=Z.getViewportCount();for(let Pt=0;Pt<St;Pt++){const oe=Z.getViewport(Pt);h.set(f.x*oe.x,f.y*oe.y,f.x*oe.z,f.y*oe.w),nt.viewport(h),Z.updateMatrices(at,Pt),r=Z.getFrustum(),P(O,V,Z.camera,at,this.type)}Z.isPointLightShadow!==!0&&this.type===ya&&L(Z,V),Z.needsUpdate=!1}S=this.type,x.needsUpdate=!1,o.setRenderTarget(gt,T,w)};function L(B,O){const V=e.update(R);y.defines.VSM_SAMPLES!==B.blurSamples&&(y.defines.VSM_SAMPLES=B.blurSamples,M.defines.VSM_SAMPLES=B.blurSamples,y.needsUpdate=!0,M.needsUpdate=!0),B.mapPass===null&&(B.mapPass=new qs(u.x,u.y)),y.uniforms.shadow_pass.value=B.map.texture,y.uniforms.resolution.value=B.mapSize,y.uniforms.radius.value=B.radius,o.setRenderTarget(B.mapPass),o.clear(),o.renderBufferDirect(O,null,V,y,R,null),M.uniforms.shadow_pass.value=B.mapPass.texture,M.uniforms.resolution.value=B.mapSize,M.uniforms.radius.value=B.radius,o.setRenderTarget(B.map),o.clear(),o.renderBufferDirect(O,null,V,M,R,null)}function U(B,O,V,gt){let T=null;const w=V.isPointLight===!0?B.customDistanceMaterial:B.customDepthMaterial;if(w!==void 0)T=w;else if(T=V.isPointLight===!0?p:d,o.localClippingEnabled&&O.clipShadows===!0&&Array.isArray(O.clippingPlanes)&&O.clippingPlanes.length!==0||O.displacementMap&&O.displacementScale!==0||O.alphaMap&&O.alphaTest>0||O.map&&O.alphaTest>0){const nt=T.uuid,rt=O.uuid;let lt=g[nt];lt===void 0&&(lt={},g[nt]=lt);let ft=lt[rt];ft===void 0&&(ft=T.clone(),lt[rt]=ft,O.addEventListener("dispose",J)),T=ft}if(T.visible=O.visible,T.wireframe=O.wireframe,gt===ya?T.side=O.shadowSide!==null?O.shadowSide:O.side:T.side=O.shadowSide!==null?O.shadowSide:_[O.side],T.alphaMap=O.alphaMap,T.alphaTest=O.alphaTest,T.map=O.map,T.clipShadows=O.clipShadows,T.clippingPlanes=O.clippingPlanes,T.clipIntersection=O.clipIntersection,T.displacementMap=O.displacementMap,T.displacementScale=O.displacementScale,T.displacementBias=O.displacementBias,T.wireframeLinewidth=O.wireframeLinewidth,T.linewidth=O.linewidth,V.isPointLight===!0&&T.isMeshDistanceMaterial===!0){const nt=o.properties.get(T);nt.light=V}return T}function P(B,O,V,gt,T){if(B.visible===!1)return;if(B.layers.test(O.layers)&&(B.isMesh||B.isLine||B.isPoints)&&(B.castShadow||B.receiveShadow&&T===ya)&&(!B.frustumCulled||r.intersectsObject(B))){B.modelViewMatrix.multiplyMatrices(V.matrixWorldInverse,B.matrixWorld);const rt=e.update(B),lt=B.material;if(Array.isArray(lt)){const ft=rt.groups;for(let H=0,at=ft.length;H<at;H++){const Z=ft[H],yt=lt[Z.materialIndex];if(yt&&yt.visible){const St=U(B,yt,gt,T);B.onBeforeShadow(o,B,O,V,rt,St,Z),o.renderBufferDirect(V,null,rt,St,B,Z),B.onAfterShadow(o,B,O,V,rt,St,Z)}}}else if(lt.visible){const ft=U(B,lt,gt,T);B.onBeforeShadow(o,B,O,V,rt,ft,null),o.renderBufferDirect(V,null,rt,ft,B,null),B.onAfterShadow(o,B,O,V,rt,ft,null)}}const nt=B.children;for(let rt=0,lt=nt.length;rt<lt;rt++)P(nt[rt],O,V,gt,T)}function J(B){B.target.removeEventListener("dispose",J);for(const V in g){const gt=g[V],T=B.target.uuid;T in gt&&(gt[T].dispose(),delete gt[T])}}}const NR={[Zd]:Kd,[Qd]:tp,[Jd]:ep,[ao]:$d,[Kd]:Zd,[tp]:Qd,[ep]:Jd,[$d]:ao};function LR(o){function e(){let Y=!1;const Tt=new Je;let ot=null;const _t=new Je(0,0,0,0);return{setMask:function(Lt){ot!==Lt&&!Y&&(o.colorMask(Lt,Lt,Lt,Lt),ot=Lt)},setLocked:function(Lt){Y=Lt},setClear:function(Lt,Ot,xe,ke,An){An===!0&&(Lt*=ke,Ot*=ke,xe*=ke),Tt.set(Lt,Ot,xe,ke),_t.equals(Tt)===!1&&(o.clearColor(Lt,Ot,xe,ke),_t.copy(Tt))},reset:function(){Y=!1,ot=null,_t.set(-1,0,0,0)}}}function i(){let Y=!1,Tt=!1,ot=null,_t=null,Lt=null;return{setReversed:function(Ot){Tt=Ot},setTest:function(Ot){Ot?dt(o.DEPTH_TEST):ht(o.DEPTH_TEST)},setMask:function(Ot){ot!==Ot&&!Y&&(o.depthMask(Ot),ot=Ot)},setFunc:function(Ot){if(Tt&&(Ot=NR[Ot]),_t!==Ot){switch(Ot){case Zd:o.depthFunc(o.NEVER);break;case Kd:o.depthFunc(o.ALWAYS);break;case Qd:o.depthFunc(o.LESS);break;case ao:o.depthFunc(o.LEQUAL);break;case Jd:o.depthFunc(o.EQUAL);break;case $d:o.depthFunc(o.GEQUAL);break;case tp:o.depthFunc(o.GREATER);break;case ep:o.depthFunc(o.NOTEQUAL);break;default:o.depthFunc(o.LEQUAL)}_t=Ot}},setLocked:function(Ot){Y=Ot},setClear:function(Ot){Lt!==Ot&&(o.clearDepth(Ot),Lt=Ot)},reset:function(){Y=!1,ot=null,_t=null,Lt=null}}}function r(){let Y=!1,Tt=null,ot=null,_t=null,Lt=null,Ot=null,xe=null,ke=null,An=null;return{setTest:function(Te){Y||(Te?dt(o.STENCIL_TEST):ht(o.STENCIL_TEST))},setMask:function(Te){Tt!==Te&&!Y&&(o.stencilMask(Te),Tt=Te)},setFunc:function(Te,tn,qe){(ot!==Te||_t!==tn||Lt!==qe)&&(o.stencilFunc(Te,tn,qe),ot=Te,_t=tn,Lt=qe)},setOp:function(Te,tn,qe){(Ot!==Te||xe!==tn||ke!==qe)&&(o.stencilOp(Te,tn,qe),Ot=Te,xe=tn,ke=qe)},setLocked:function(Te){Y=Te},setClear:function(Te){An!==Te&&(o.clearStencil(Te),An=Te)},reset:function(){Y=!1,Tt=null,ot=null,_t=null,Lt=null,Ot=null,xe=null,ke=null,An=null}}}const u=new e,f=new i,h=new r,d=new WeakMap,p=new WeakMap;let g={},v={},_=new WeakMap,y=[],M=null,E=!1,R=null,x=null,S=null,L=null,U=null,P=null,J=null,B=new ye(0,0,0),O=0,V=!1,gt=null,T=null,w=null,nt=null,rt=null;const lt=o.getParameter(o.MAX_COMBINED_TEXTURE_IMAGE_UNITS);let ft=!1,H=0;const at=o.getParameter(o.VERSION);at.indexOf("WebGL")!==-1?(H=parseFloat(/^WebGL (\d)/.exec(at)[1]),ft=H>=1):at.indexOf("OpenGL ES")!==-1&&(H=parseFloat(/^OpenGL ES (\d)/.exec(at)[1]),ft=H>=2);let Z=null,yt={};const St=o.getParameter(o.SCISSOR_BOX),Pt=o.getParameter(o.VIEWPORT),oe=new Je().fromArray(St),me=new Je().fromArray(Pt);function D(Y,Tt,ot,_t){const Lt=new Uint8Array(4),Ot=o.createTexture();o.bindTexture(Y,Ot),o.texParameteri(Y,o.TEXTURE_MIN_FILTER,o.NEAREST),o.texParameteri(Y,o.TEXTURE_MAG_FILTER,o.NEAREST);for(let xe=0;xe<ot;xe++)Y===o.TEXTURE_3D||Y===o.TEXTURE_2D_ARRAY?o.texImage3D(Tt,0,o.RGBA,1,1,_t,0,o.RGBA,o.UNSIGNED_BYTE,Lt):o.texImage2D(Tt+xe,0,o.RGBA,1,1,0,o.RGBA,o.UNSIGNED_BYTE,Lt);return Ot}const X={};X[o.TEXTURE_2D]=D(o.TEXTURE_2D,o.TEXTURE_2D,1),X[o.TEXTURE_CUBE_MAP]=D(o.TEXTURE_CUBE_MAP,o.TEXTURE_CUBE_MAP_POSITIVE_X,6),X[o.TEXTURE_2D_ARRAY]=D(o.TEXTURE_2D_ARRAY,o.TEXTURE_2D_ARRAY,1,1),X[o.TEXTURE_3D]=D(o.TEXTURE_3D,o.TEXTURE_3D,1,1),u.setClear(0,0,0,1),f.setClear(1),h.setClear(0),dt(o.DEPTH_TEST),f.setFunc(ao),le(!1),ae(dv),dt(o.CULL_FACE),F(rs);function dt(Y){g[Y]!==!0&&(o.enable(Y),g[Y]=!0)}function ht(Y){g[Y]!==!1&&(o.disable(Y),g[Y]=!1)}function Ct(Y,Tt){return v[Y]!==Tt?(o.bindFramebuffer(Y,Tt),v[Y]=Tt,Y===o.DRAW_FRAMEBUFFER&&(v[o.FRAMEBUFFER]=Tt),Y===o.FRAMEBUFFER&&(v[o.DRAW_FRAMEBUFFER]=Tt),!0):!1}function Rt(Y,Tt){let ot=y,_t=!1;if(Y){ot=_.get(Tt),ot===void 0&&(ot=[],_.set(Tt,ot));const Lt=Y.textures;if(ot.length!==Lt.length||ot[0]!==o.COLOR_ATTACHMENT0){for(let Ot=0,xe=Lt.length;Ot<xe;Ot++)ot[Ot]=o.COLOR_ATTACHMENT0+Ot;ot.length=Lt.length,_t=!0}}else ot[0]!==o.BACK&&(ot[0]=o.BACK,_t=!0);_t&&o.drawBuffers(ot)}function Ht(Y){return M!==Y?(o.useProgram(Y),M=Y,!0):!1}const Mt={[Gs]:o.FUNC_ADD,[WM]:o.FUNC_SUBTRACT,[jM]:o.FUNC_REVERSE_SUBTRACT};Mt[ZM]=o.MIN,Mt[KM]=o.MAX;const bt={[QM]:o.ZERO,[JM]:o.ONE,[$M]:o.SRC_COLOR,[Wd]:o.SRC_ALPHA,[sE]:o.SRC_ALPHA_SATURATE,[iE]:o.DST_COLOR,[eE]:o.DST_ALPHA,[tE]:o.ONE_MINUS_SRC_COLOR,[jd]:o.ONE_MINUS_SRC_ALPHA,[aE]:o.ONE_MINUS_DST_COLOR,[nE]:o.ONE_MINUS_DST_ALPHA,[rE]:o.CONSTANT_COLOR,[oE]:o.ONE_MINUS_CONSTANT_COLOR,[lE]:o.CONSTANT_ALPHA,[uE]:o.ONE_MINUS_CONSTANT_ALPHA};function F(Y,Tt,ot,_t,Lt,Ot,xe,ke,An,Te){if(Y===rs){E===!0&&(ht(o.BLEND),E=!1);return}if(E===!1&&(dt(o.BLEND),E=!0),Y!==qM){if(Y!==R||Te!==V){if((x!==Gs||U!==Gs)&&(o.blendEquation(o.FUNC_ADD),x=Gs,U=Gs),Te)switch(Y){case eo:o.blendFuncSeparate(o.ONE,o.ONE_MINUS_SRC_ALPHA,o.ONE,o.ONE_MINUS_SRC_ALPHA);break;case pv:o.blendFunc(o.ONE,o.ONE);break;case mv:o.blendFuncSeparate(o.ZERO,o.ONE_MINUS_SRC_COLOR,o.ZERO,o.ONE);break;case _v:o.blendFuncSeparate(o.ZERO,o.SRC_COLOR,o.ZERO,o.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",Y);break}else switch(Y){case eo:o.blendFuncSeparate(o.SRC_ALPHA,o.ONE_MINUS_SRC_ALPHA,o.ONE,o.ONE_MINUS_SRC_ALPHA);break;case pv:o.blendFunc(o.SRC_ALPHA,o.ONE);break;case mv:o.blendFuncSeparate(o.ZERO,o.ONE_MINUS_SRC_COLOR,o.ZERO,o.ONE);break;case _v:o.blendFunc(o.ZERO,o.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",Y);break}S=null,L=null,P=null,J=null,B.set(0,0,0),O=0,R=Y,V=Te}return}Lt=Lt||Tt,Ot=Ot||ot,xe=xe||_t,(Tt!==x||Lt!==U)&&(o.blendEquationSeparate(Mt[Tt],Mt[Lt]),x=Tt,U=Lt),(ot!==S||_t!==L||Ot!==P||xe!==J)&&(o.blendFuncSeparate(bt[ot],bt[_t],bt[Ot],bt[xe]),S=ot,L=_t,P=Ot,J=xe),(ke.equals(B)===!1||An!==O)&&(o.blendColor(ke.r,ke.g,ke.b,An),B.copy(ke),O=An),R=Y,V=!1}function vn(Y,Tt){Y.side===Li?ht(o.CULL_FACE):dt(o.CULL_FACE);let ot=Y.side===Zn;Tt&&(ot=!ot),le(ot),Y.blending===eo&&Y.transparent===!1?F(rs):F(Y.blending,Y.blendEquation,Y.blendSrc,Y.blendDst,Y.blendEquationAlpha,Y.blendSrcAlpha,Y.blendDstAlpha,Y.blendColor,Y.blendAlpha,Y.premultipliedAlpha),f.setFunc(Y.depthFunc),f.setTest(Y.depthTest),f.setMask(Y.depthWrite),u.setMask(Y.colorWrite);const _t=Y.stencilWrite;h.setTest(_t),_t&&(h.setMask(Y.stencilWriteMask),h.setFunc(Y.stencilFunc,Y.stencilRef,Y.stencilFuncMask),h.setOp(Y.stencilFail,Y.stencilZFail,Y.stencilZPass)),Kt(Y.polygonOffset,Y.polygonOffsetFactor,Y.polygonOffsetUnits),Y.alphaToCoverage===!0?dt(o.SAMPLE_ALPHA_TO_COVERAGE):ht(o.SAMPLE_ALPHA_TO_COVERAGE)}function le(Y){gt!==Y&&(Y?o.frontFace(o.CW):o.frontFace(o.CCW),gt=Y)}function ae(Y){Y!==XM?(dt(o.CULL_FACE),Y!==T&&(Y===dv?o.cullFace(o.BACK):Y===YM?o.cullFace(o.FRONT):o.cullFace(o.FRONT_AND_BACK))):ht(o.CULL_FACE),T=Y}function Xt(Y){Y!==w&&(ft&&o.lineWidth(Y),w=Y)}function Kt(Y,Tt,ot){Y?(dt(o.POLYGON_OFFSET_FILL),(nt!==Tt||rt!==ot)&&(o.polygonOffset(Tt,ot),nt=Tt,rt=ot)):ht(o.POLYGON_OFFSET_FILL)}function Zt(Y){Y?dt(o.SCISSOR_TEST):ht(o.SCISSOR_TEST)}function N(Y){Y===void 0&&(Y=o.TEXTURE0+lt-1),Z!==Y&&(o.activeTexture(Y),Z=Y)}function A(Y,Tt,ot){ot===void 0&&(Z===null?ot=o.TEXTURE0+lt-1:ot=Z);let _t=yt[ot];_t===void 0&&(_t={type:void 0,texture:void 0},yt[ot]=_t),(_t.type!==Y||_t.texture!==Tt)&&(Z!==ot&&(o.activeTexture(ot),Z=ot),o.bindTexture(Y,Tt||X[Y]),_t.type=Y,_t.texture=Tt)}function tt(){const Y=yt[Z];Y!==void 0&&Y.type!==void 0&&(o.bindTexture(Y.type,null),Y.type=void 0,Y.texture=void 0)}function pt(){try{o.compressedTexImage2D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function vt(){try{o.compressedTexImage3D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function mt(){try{o.texSubImage2D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function kt(){try{o.texSubImage3D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function wt(){try{o.compressedTexSubImage2D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function It(){try{o.compressedTexSubImage3D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function ue(){try{o.texStorage2D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function xt(){try{o.texStorage3D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function Bt(){try{o.texImage2D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function te(){try{o.texImage3D.apply(o,arguments)}catch(Y){console.error("THREE.WebGLState:",Y)}}function $t(Y){oe.equals(Y)===!1&&(o.scissor(Y.x,Y.y,Y.z,Y.w),oe.copy(Y))}function Ft(Y){me.equals(Y)===!1&&(o.viewport(Y.x,Y.y,Y.z,Y.w),me.copy(Y))}function pe(Y,Tt){let ot=p.get(Tt);ot===void 0&&(ot=new WeakMap,p.set(Tt,ot));let _t=ot.get(Y);_t===void 0&&(_t=o.getUniformBlockIndex(Tt,Y.name),ot.set(Y,_t))}function ee(Y,Tt){const _t=p.get(Tt).get(Y);d.get(Tt)!==_t&&(o.uniformBlockBinding(Tt,_t,Y.__bindingPointIndex),d.set(Tt,_t))}function Oe(){o.disable(o.BLEND),o.disable(o.CULL_FACE),o.disable(o.DEPTH_TEST),o.disable(o.POLYGON_OFFSET_FILL),o.disable(o.SCISSOR_TEST),o.disable(o.STENCIL_TEST),o.disable(o.SAMPLE_ALPHA_TO_COVERAGE),o.blendEquation(o.FUNC_ADD),o.blendFunc(o.ONE,o.ZERO),o.blendFuncSeparate(o.ONE,o.ZERO,o.ONE,o.ZERO),o.blendColor(0,0,0,0),o.colorMask(!0,!0,!0,!0),o.clearColor(0,0,0,0),o.depthMask(!0),o.depthFunc(o.LESS),o.clearDepth(1),o.stencilMask(4294967295),o.stencilFunc(o.ALWAYS,0,4294967295),o.stencilOp(o.KEEP,o.KEEP,o.KEEP),o.clearStencil(0),o.cullFace(o.BACK),o.frontFace(o.CCW),o.polygonOffset(0,0),o.activeTexture(o.TEXTURE0),o.bindFramebuffer(o.FRAMEBUFFER,null),o.bindFramebuffer(o.DRAW_FRAMEBUFFER,null),o.bindFramebuffer(o.READ_FRAMEBUFFER,null),o.useProgram(null),o.lineWidth(1),o.scissor(0,0,o.canvas.width,o.canvas.height),o.viewport(0,0,o.canvas.width,o.canvas.height),g={},Z=null,yt={},v={},_=new WeakMap,y=[],M=null,E=!1,R=null,x=null,S=null,L=null,U=null,P=null,J=null,B=new ye(0,0,0),O=0,V=!1,gt=null,T=null,w=null,nt=null,rt=null,oe.set(0,0,o.canvas.width,o.canvas.height),me.set(0,0,o.canvas.width,o.canvas.height),u.reset(),f.reset(),h.reset()}return{buffers:{color:u,depth:f,stencil:h},enable:dt,disable:ht,bindFramebuffer:Ct,drawBuffers:Rt,useProgram:Ht,setBlending:F,setMaterial:vn,setFlipSided:le,setCullFace:ae,setLineWidth:Xt,setPolygonOffset:Kt,setScissorTest:Zt,activeTexture:N,bindTexture:A,unbindTexture:tt,compressedTexImage2D:pt,compressedTexImage3D:vt,texImage2D:Bt,texImage3D:te,updateUBOMapping:pe,uniformBlockBinding:ee,texStorage2D:ue,texStorage3D:xt,texSubImage2D:mt,texSubImage3D:kt,compressedTexSubImage2D:wt,compressedTexSubImage3D:It,scissor:$t,viewport:Ft,reset:Oe}}function rS(o,e,i,r){const u=OR(r);switch(i){case MS:return o*e;case TS:return o*e;case bS:return o*e*2;case AS:return o*e/u.components*u.byteLength;case Fp:return o*e/u.components*u.byteLength;case RS:return o*e*2/u.components*u.byteLength;case Hp:return o*e*2/u.components*u.byteLength;case ES:return o*e*3/u.components*u.byteLength;case zi:return o*e*4/u.components*u.byteLength;case Gp:return o*e*4/u.components*u.byteLength;case _c:case gc:return Math.floor((o+3)/4)*Math.floor((e+3)/4)*8;case vc:case Sc:return Math.floor((o+3)/4)*Math.floor((e+3)/4)*16;case op:case up:return Math.max(o,16)*Math.max(e,8)/4;case rp:case lp:return Math.max(o,8)*Math.max(e,8)/2;case cp:case fp:return Math.floor((o+3)/4)*Math.floor((e+3)/4)*8;case hp:return Math.floor((o+3)/4)*Math.floor((e+3)/4)*16;case dp:return Math.floor((o+3)/4)*Math.floor((e+3)/4)*16;case pp:return Math.floor((o+4)/5)*Math.floor((e+3)/4)*16;case mp:return Math.floor((o+4)/5)*Math.floor((e+4)/5)*16;case _p:return Math.floor((o+5)/6)*Math.floor((e+4)/5)*16;case gp:return Math.floor((o+5)/6)*Math.floor((e+5)/6)*16;case vp:return Math.floor((o+7)/8)*Math.floor((e+4)/5)*16;case Sp:return Math.floor((o+7)/8)*Math.floor((e+5)/6)*16;case yp:return Math.floor((o+7)/8)*Math.floor((e+7)/8)*16;case xp:return Math.floor((o+9)/10)*Math.floor((e+4)/5)*16;case Mp:return Math.floor((o+9)/10)*Math.floor((e+5)/6)*16;case Ep:return Math.floor((o+9)/10)*Math.floor((e+7)/8)*16;case Tp:return Math.floor((o+9)/10)*Math.floor((e+9)/10)*16;case bp:return Math.floor((o+11)/12)*Math.floor((e+9)/10)*16;case Ap:return Math.floor((o+11)/12)*Math.floor((e+11)/12)*16;case yc:case Rp:case Cp:return Math.ceil(o/4)*Math.ceil(e/4)*16;case CS:case wp:return Math.ceil(o/4)*Math.ceil(e/4)*8;case Dp:case Up:return Math.ceil(o/4)*Math.ceil(e/4)*16}throw new Error(`Unable to determine texture byte length for ${i} format.`)}function OR(o){switch(o){case Ea:case SS:return{byteLength:1,components:1};case ml:case yS:case _l:return{byteLength:2,components:1};case Ip:case Bp:return{byteLength:2,components:4};case ks:case zp:case xa:return{byteLength:4,components:1};case xS:return{byteLength:4,components:3}}throw new Error(`Unknown texture type ${o}.`)}function PR(o,e,i,r,u,f,h){const d=e.has("WEBGL_multisampled_render_to_texture")?e.get("WEBGL_multisampled_render_to_texture"):null,p=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),g=new ce,v=new WeakMap;let _;const y=new WeakMap;let M=!1;try{M=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function E(N,A){return M?new OffscreenCanvas(N,A):Cc("canvas")}function R(N,A,tt){let pt=1;const vt=Zt(N);if((vt.width>tt||vt.height>tt)&&(pt=tt/Math.max(vt.width,vt.height)),pt<1)if(typeof HTMLImageElement<"u"&&N instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&N instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&N instanceof ImageBitmap||typeof VideoFrame<"u"&&N instanceof VideoFrame){const mt=Math.floor(pt*vt.width),kt=Math.floor(pt*vt.height);_===void 0&&(_=E(mt,kt));const wt=A?E(mt,kt):_;return wt.width=mt,wt.height=kt,wt.getContext("2d").drawImage(N,0,0,mt,kt),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+vt.width+"x"+vt.height+") to ("+mt+"x"+kt+")."),wt}else return"data"in N&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+vt.width+"x"+vt.height+")."),N;return N}function x(N){return N.generateMipmaps&&N.minFilter!==yi&&N.minFilter!==Oi}function S(N){o.generateMipmap(N)}function L(N,A,tt,pt,vt=!1){if(N!==null){if(o[N]!==void 0)return o[N];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+N+"'")}let mt=A;if(A===o.RED&&(tt===o.FLOAT&&(mt=o.R32F),tt===o.HALF_FLOAT&&(mt=o.R16F),tt===o.UNSIGNED_BYTE&&(mt=o.R8)),A===o.RED_INTEGER&&(tt===o.UNSIGNED_BYTE&&(mt=o.R8UI),tt===o.UNSIGNED_SHORT&&(mt=o.R16UI),tt===o.UNSIGNED_INT&&(mt=o.R32UI),tt===o.BYTE&&(mt=o.R8I),tt===o.SHORT&&(mt=o.R16I),tt===o.INT&&(mt=o.R32I)),A===o.RG&&(tt===o.FLOAT&&(mt=o.RG32F),tt===o.HALF_FLOAT&&(mt=o.RG16F),tt===o.UNSIGNED_BYTE&&(mt=o.RG8)),A===o.RG_INTEGER&&(tt===o.UNSIGNED_BYTE&&(mt=o.RG8UI),tt===o.UNSIGNED_SHORT&&(mt=o.RG16UI),tt===o.UNSIGNED_INT&&(mt=o.RG32UI),tt===o.BYTE&&(mt=o.RG8I),tt===o.SHORT&&(mt=o.RG16I),tt===o.INT&&(mt=o.RG32I)),A===o.RGB_INTEGER&&(tt===o.UNSIGNED_BYTE&&(mt=o.RGB8UI),tt===o.UNSIGNED_SHORT&&(mt=o.RGB16UI),tt===o.UNSIGNED_INT&&(mt=o.RGB32UI),tt===o.BYTE&&(mt=o.RGB8I),tt===o.SHORT&&(mt=o.RGB16I),tt===o.INT&&(mt=o.RGB32I)),A===o.RGBA_INTEGER&&(tt===o.UNSIGNED_BYTE&&(mt=o.RGBA8UI),tt===o.UNSIGNED_SHORT&&(mt=o.RGBA16UI),tt===o.UNSIGNED_INT&&(mt=o.RGBA32UI),tt===o.BYTE&&(mt=o.RGBA8I),tt===o.SHORT&&(mt=o.RGBA16I),tt===o.INT&&(mt=o.RGBA32I)),A===o.RGB&&tt===o.UNSIGNED_INT_5_9_9_9_REV&&(mt=o.RGB9_E5),A===o.RGBA){const kt=vt?Tc:De.getTransfer(pt);tt===o.FLOAT&&(mt=o.RGBA32F),tt===o.HALF_FLOAT&&(mt=o.RGBA16F),tt===o.UNSIGNED_BYTE&&(mt=kt===Xe?o.SRGB8_ALPHA8:o.RGBA8),tt===o.UNSIGNED_SHORT_4_4_4_4&&(mt=o.RGBA4),tt===o.UNSIGNED_SHORT_5_5_5_1&&(mt=o.RGB5_A1)}return(mt===o.R16F||mt===o.R32F||mt===o.RG16F||mt===o.RG32F||mt===o.RGBA16F||mt===o.RGBA32F)&&e.get("EXT_color_buffer_float"),mt}function U(N,A){let tt;return N?A===null||A===ks||A===oo?tt=o.DEPTH24_STENCIL8:A===xa?tt=o.DEPTH32F_STENCIL8:A===ml&&(tt=o.DEPTH24_STENCIL8,console.warn("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):A===null||A===ks||A===oo?tt=o.DEPTH_COMPONENT24:A===xa?tt=o.DEPTH_COMPONENT32F:A===ml&&(tt=o.DEPTH_COMPONENT16),tt}function P(N,A){return x(N)===!0||N.isFramebufferTexture&&N.minFilter!==yi&&N.minFilter!==Oi?Math.log2(Math.max(A.width,A.height))+1:N.mipmaps!==void 0&&N.mipmaps.length>0?N.mipmaps.length:N.isCompressedTexture&&Array.isArray(N.image)?A.mipmaps.length:1}function J(N){const A=N.target;A.removeEventListener("dispose",J),O(A),A.isVideoTexture&&v.delete(A)}function B(N){const A=N.target;A.removeEventListener("dispose",B),gt(A)}function O(N){const A=r.get(N);if(A.__webglInit===void 0)return;const tt=N.source,pt=y.get(tt);if(pt){const vt=pt[A.__cacheKey];vt.usedTimes--,vt.usedTimes===0&&V(N),Object.keys(pt).length===0&&y.delete(tt)}r.remove(N)}function V(N){const A=r.get(N);o.deleteTexture(A.__webglTexture);const tt=N.source,pt=y.get(tt);delete pt[A.__cacheKey],h.memory.textures--}function gt(N){const A=r.get(N);if(N.depthTexture&&N.depthTexture.dispose(),N.isWebGLCubeRenderTarget)for(let pt=0;pt<6;pt++){if(Array.isArray(A.__webglFramebuffer[pt]))for(let vt=0;vt<A.__webglFramebuffer[pt].length;vt++)o.deleteFramebuffer(A.__webglFramebuffer[pt][vt]);else o.deleteFramebuffer(A.__webglFramebuffer[pt]);A.__webglDepthbuffer&&o.deleteRenderbuffer(A.__webglDepthbuffer[pt])}else{if(Array.isArray(A.__webglFramebuffer))for(let pt=0;pt<A.__webglFramebuffer.length;pt++)o.deleteFramebuffer(A.__webglFramebuffer[pt]);else o.deleteFramebuffer(A.__webglFramebuffer);if(A.__webglDepthbuffer&&o.deleteRenderbuffer(A.__webglDepthbuffer),A.__webglMultisampledFramebuffer&&o.deleteFramebuffer(A.__webglMultisampledFramebuffer),A.__webglColorRenderbuffer)for(let pt=0;pt<A.__webglColorRenderbuffer.length;pt++)A.__webglColorRenderbuffer[pt]&&o.deleteRenderbuffer(A.__webglColorRenderbuffer[pt]);A.__webglDepthRenderbuffer&&o.deleteRenderbuffer(A.__webglDepthRenderbuffer)}const tt=N.textures;for(let pt=0,vt=tt.length;pt<vt;pt++){const mt=r.get(tt[pt]);mt.__webglTexture&&(o.deleteTexture(mt.__webglTexture),h.memory.textures--),r.remove(tt[pt])}r.remove(N)}let T=0;function w(){T=0}function nt(){const N=T;return N>=u.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+N+" texture units while this GPU supports only "+u.maxTextures),T+=1,N}function rt(N){const A=[];return A.push(N.wrapS),A.push(N.wrapT),A.push(N.wrapR||0),A.push(N.magFilter),A.push(N.minFilter),A.push(N.anisotropy),A.push(N.internalFormat),A.push(N.format),A.push(N.type),A.push(N.generateMipmaps),A.push(N.premultiplyAlpha),A.push(N.flipY),A.push(N.unpackAlignment),A.push(N.colorSpace),A.join()}function lt(N,A){const tt=r.get(N);if(N.isVideoTexture&&Xt(N),N.isRenderTargetTexture===!1&&N.version>0&&tt.__version!==N.version){const pt=N.image;if(pt===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if(pt.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{me(tt,N,A);return}}i.bindTexture(o.TEXTURE_2D,tt.__webglTexture,o.TEXTURE0+A)}function ft(N,A){const tt=r.get(N);if(N.version>0&&tt.__version!==N.version){me(tt,N,A);return}i.bindTexture(o.TEXTURE_2D_ARRAY,tt.__webglTexture,o.TEXTURE0+A)}function H(N,A){const tt=r.get(N);if(N.version>0&&tt.__version!==N.version){me(tt,N,A);return}i.bindTexture(o.TEXTURE_3D,tt.__webglTexture,o.TEXTURE0+A)}function at(N,A){const tt=r.get(N);if(N.version>0&&tt.__version!==N.version){D(tt,N,A);return}i.bindTexture(o.TEXTURE_CUBE_MAP,tt.__webglTexture,o.TEXTURE0+A)}const Z={[ap]:o.REPEAT,[Xs]:o.CLAMP_TO_EDGE,[sp]:o.MIRRORED_REPEAT},yt={[yi]:o.NEAREST,[SE]:o.NEAREST_MIPMAP_NEAREST,[Yu]:o.NEAREST_MIPMAP_LINEAR,[Oi]:o.LINEAR,[pd]:o.LINEAR_MIPMAP_NEAREST,[Ys]:o.LINEAR_MIPMAP_LINEAR},St={[TE]:o.NEVER,[DE]:o.ALWAYS,[bE]:o.LESS,[wS]:o.LEQUAL,[AE]:o.EQUAL,[wE]:o.GEQUAL,[RE]:o.GREATER,[CE]:o.NOTEQUAL};function Pt(N,A){if(A.type===xa&&e.has("OES_texture_float_linear")===!1&&(A.magFilter===Oi||A.magFilter===pd||A.magFilter===Yu||A.magFilter===Ys||A.minFilter===Oi||A.minFilter===pd||A.minFilter===Yu||A.minFilter===Ys)&&console.warn("THREE.WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),o.texParameteri(N,o.TEXTURE_WRAP_S,Z[A.wrapS]),o.texParameteri(N,o.TEXTURE_WRAP_T,Z[A.wrapT]),(N===o.TEXTURE_3D||N===o.TEXTURE_2D_ARRAY)&&o.texParameteri(N,o.TEXTURE_WRAP_R,Z[A.wrapR]),o.texParameteri(N,o.TEXTURE_MAG_FILTER,yt[A.magFilter]),o.texParameteri(N,o.TEXTURE_MIN_FILTER,yt[A.minFilter]),A.compareFunction&&(o.texParameteri(N,o.TEXTURE_COMPARE_MODE,o.COMPARE_REF_TO_TEXTURE),o.texParameteri(N,o.TEXTURE_COMPARE_FUNC,St[A.compareFunction])),e.has("EXT_texture_filter_anisotropic")===!0){if(A.magFilter===yi||A.minFilter!==Yu&&A.minFilter!==Ys||A.type===xa&&e.has("OES_texture_float_linear")===!1)return;if(A.anisotropy>1||r.get(A).__currentAnisotropy){const tt=e.get("EXT_texture_filter_anisotropic");o.texParameterf(N,tt.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(A.anisotropy,u.getMaxAnisotropy())),r.get(A).__currentAnisotropy=A.anisotropy}}}function oe(N,A){let tt=!1;N.__webglInit===void 0&&(N.__webglInit=!0,A.addEventListener("dispose",J));const pt=A.source;let vt=y.get(pt);vt===void 0&&(vt={},y.set(pt,vt));const mt=rt(A);if(mt!==N.__cacheKey){vt[mt]===void 0&&(vt[mt]={texture:o.createTexture(),usedTimes:0},h.memory.textures++,tt=!0),vt[mt].usedTimes++;const kt=vt[N.__cacheKey];kt!==void 0&&(vt[N.__cacheKey].usedTimes--,kt.usedTimes===0&&V(A)),N.__cacheKey=mt,N.__webglTexture=vt[mt].texture}return tt}function me(N,A,tt){let pt=o.TEXTURE_2D;(A.isDataArrayTexture||A.isCompressedArrayTexture)&&(pt=o.TEXTURE_2D_ARRAY),A.isData3DTexture&&(pt=o.TEXTURE_3D);const vt=oe(N,A),mt=A.source;i.bindTexture(pt,N.__webglTexture,o.TEXTURE0+tt);const kt=r.get(mt);if(mt.version!==kt.__version||vt===!0){i.activeTexture(o.TEXTURE0+tt);const wt=De.getPrimaries(De.workingColorSpace),It=A.colorSpace===ss?null:De.getPrimaries(A.colorSpace),ue=A.colorSpace===ss||wt===It?o.NONE:o.BROWSER_DEFAULT_WEBGL;o.pixelStorei(o.UNPACK_FLIP_Y_WEBGL,A.flipY),o.pixelStorei(o.UNPACK_PREMULTIPLY_ALPHA_WEBGL,A.premultiplyAlpha),o.pixelStorei(o.UNPACK_ALIGNMENT,A.unpackAlignment),o.pixelStorei(o.UNPACK_COLORSPACE_CONVERSION_WEBGL,ue);let xt=R(A.image,!1,u.maxTextureSize);xt=Kt(A,xt);const Bt=f.convert(A.format,A.colorSpace),te=f.convert(A.type);let $t=L(A.internalFormat,Bt,te,A.colorSpace,A.isVideoTexture);Pt(pt,A);let Ft;const pe=A.mipmaps,ee=A.isVideoTexture!==!0,Oe=kt.__version===void 0||vt===!0,Y=mt.dataReady,Tt=P(A,xt);if(A.isDepthTexture)$t=U(A.format===lo,A.type),Oe&&(ee?i.texStorage2D(o.TEXTURE_2D,1,$t,xt.width,xt.height):i.texImage2D(o.TEXTURE_2D,0,$t,xt.width,xt.height,0,Bt,te,null));else if(A.isDataTexture)if(pe.length>0){ee&&Oe&&i.texStorage2D(o.TEXTURE_2D,Tt,$t,pe[0].width,pe[0].height);for(let ot=0,_t=pe.length;ot<_t;ot++)Ft=pe[ot],ee?Y&&i.texSubImage2D(o.TEXTURE_2D,ot,0,0,Ft.width,Ft.height,Bt,te,Ft.data):i.texImage2D(o.TEXTURE_2D,ot,$t,Ft.width,Ft.height,0,Bt,te,Ft.data);A.generateMipmaps=!1}else ee?(Oe&&i.texStorage2D(o.TEXTURE_2D,Tt,$t,xt.width,xt.height),Y&&i.texSubImage2D(o.TEXTURE_2D,0,0,0,xt.width,xt.height,Bt,te,xt.data)):i.texImage2D(o.TEXTURE_2D,0,$t,xt.width,xt.height,0,Bt,te,xt.data);else if(A.isCompressedTexture)if(A.isCompressedArrayTexture){ee&&Oe&&i.texStorage3D(o.TEXTURE_2D_ARRAY,Tt,$t,pe[0].width,pe[0].height,xt.depth);for(let ot=0,_t=pe.length;ot<_t;ot++)if(Ft=pe[ot],A.format!==zi)if(Bt!==null)if(ee){if(Y)if(A.layerUpdates.size>0){const Lt=rS(Ft.width,Ft.height,A.format,A.type);for(const Ot of A.layerUpdates){const xe=Ft.data.subarray(Ot*Lt/Ft.data.BYTES_PER_ELEMENT,(Ot+1)*Lt/Ft.data.BYTES_PER_ELEMENT);i.compressedTexSubImage3D(o.TEXTURE_2D_ARRAY,ot,0,0,Ot,Ft.width,Ft.height,1,Bt,xe,0,0)}A.clearLayerUpdates()}else i.compressedTexSubImage3D(o.TEXTURE_2D_ARRAY,ot,0,0,0,Ft.width,Ft.height,xt.depth,Bt,Ft.data,0,0)}else i.compressedTexImage3D(o.TEXTURE_2D_ARRAY,ot,$t,Ft.width,Ft.height,xt.depth,0,Ft.data,0,0);else console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else ee?Y&&i.texSubImage3D(o.TEXTURE_2D_ARRAY,ot,0,0,0,Ft.width,Ft.height,xt.depth,Bt,te,Ft.data):i.texImage3D(o.TEXTURE_2D_ARRAY,ot,$t,Ft.width,Ft.height,xt.depth,0,Bt,te,Ft.data)}else{ee&&Oe&&i.texStorage2D(o.TEXTURE_2D,Tt,$t,pe[0].width,pe[0].height);for(let ot=0,_t=pe.length;ot<_t;ot++)Ft=pe[ot],A.format!==zi?Bt!==null?ee?Y&&i.compressedTexSubImage2D(o.TEXTURE_2D,ot,0,0,Ft.width,Ft.height,Bt,Ft.data):i.compressedTexImage2D(o.TEXTURE_2D,ot,$t,Ft.width,Ft.height,0,Ft.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):ee?Y&&i.texSubImage2D(o.TEXTURE_2D,ot,0,0,Ft.width,Ft.height,Bt,te,Ft.data):i.texImage2D(o.TEXTURE_2D,ot,$t,Ft.width,Ft.height,0,Bt,te,Ft.data)}else if(A.isDataArrayTexture)if(ee){if(Oe&&i.texStorage3D(o.TEXTURE_2D_ARRAY,Tt,$t,xt.width,xt.height,xt.depth),Y)if(A.layerUpdates.size>0){const ot=rS(xt.width,xt.height,A.format,A.type);for(const _t of A.layerUpdates){const Lt=xt.data.subarray(_t*ot/xt.data.BYTES_PER_ELEMENT,(_t+1)*ot/xt.data.BYTES_PER_ELEMENT);i.texSubImage3D(o.TEXTURE_2D_ARRAY,0,0,0,_t,xt.width,xt.height,1,Bt,te,Lt)}A.clearLayerUpdates()}else i.texSubImage3D(o.TEXTURE_2D_ARRAY,0,0,0,0,xt.width,xt.height,xt.depth,Bt,te,xt.data)}else i.texImage3D(o.TEXTURE_2D_ARRAY,0,$t,xt.width,xt.height,xt.depth,0,Bt,te,xt.data);else if(A.isData3DTexture)ee?(Oe&&i.texStorage3D(o.TEXTURE_3D,Tt,$t,xt.width,xt.height,xt.depth),Y&&i.texSubImage3D(o.TEXTURE_3D,0,0,0,0,xt.width,xt.height,xt.depth,Bt,te,xt.data)):i.texImage3D(o.TEXTURE_3D,0,$t,xt.width,xt.height,xt.depth,0,Bt,te,xt.data);else if(A.isFramebufferTexture){if(Oe)if(ee)i.texStorage2D(o.TEXTURE_2D,Tt,$t,xt.width,xt.height);else{let ot=xt.width,_t=xt.height;for(let Lt=0;Lt<Tt;Lt++)i.texImage2D(o.TEXTURE_2D,Lt,$t,ot,_t,0,Bt,te,null),ot>>=1,_t>>=1}}else if(pe.length>0){if(ee&&Oe){const ot=Zt(pe[0]);i.texStorage2D(o.TEXTURE_2D,Tt,$t,ot.width,ot.height)}for(let ot=0,_t=pe.length;ot<_t;ot++)Ft=pe[ot],ee?Y&&i.texSubImage2D(o.TEXTURE_2D,ot,0,0,Bt,te,Ft):i.texImage2D(o.TEXTURE_2D,ot,$t,Bt,te,Ft);A.generateMipmaps=!1}else if(ee){if(Oe){const ot=Zt(xt);i.texStorage2D(o.TEXTURE_2D,Tt,$t,ot.width,ot.height)}Y&&i.texSubImage2D(o.TEXTURE_2D,0,0,0,Bt,te,xt)}else i.texImage2D(o.TEXTURE_2D,0,$t,Bt,te,xt);x(A)&&S(pt),kt.__version=mt.version,A.onUpdate&&A.onUpdate(A)}N.__version=A.version}function D(N,A,tt){if(A.image.length!==6)return;const pt=oe(N,A),vt=A.source;i.bindTexture(o.TEXTURE_CUBE_MAP,N.__webglTexture,o.TEXTURE0+tt);const mt=r.get(vt);if(vt.version!==mt.__version||pt===!0){i.activeTexture(o.TEXTURE0+tt);const kt=De.getPrimaries(De.workingColorSpace),wt=A.colorSpace===ss?null:De.getPrimaries(A.colorSpace),It=A.colorSpace===ss||kt===wt?o.NONE:o.BROWSER_DEFAULT_WEBGL;o.pixelStorei(o.UNPACK_FLIP_Y_WEBGL,A.flipY),o.pixelStorei(o.UNPACK_PREMULTIPLY_ALPHA_WEBGL,A.premultiplyAlpha),o.pixelStorei(o.UNPACK_ALIGNMENT,A.unpackAlignment),o.pixelStorei(o.UNPACK_COLORSPACE_CONVERSION_WEBGL,It);const ue=A.isCompressedTexture||A.image[0].isCompressedTexture,xt=A.image[0]&&A.image[0].isDataTexture,Bt=[];for(let _t=0;_t<6;_t++)!ue&&!xt?Bt[_t]=R(A.image[_t],!0,u.maxCubemapSize):Bt[_t]=xt?A.image[_t].image:A.image[_t],Bt[_t]=Kt(A,Bt[_t]);const te=Bt[0],$t=f.convert(A.format,A.colorSpace),Ft=f.convert(A.type),pe=L(A.internalFormat,$t,Ft,A.colorSpace),ee=A.isVideoTexture!==!0,Oe=mt.__version===void 0||pt===!0,Y=vt.dataReady;let Tt=P(A,te);Pt(o.TEXTURE_CUBE_MAP,A);let ot;if(ue){ee&&Oe&&i.texStorage2D(o.TEXTURE_CUBE_MAP,Tt,pe,te.width,te.height);for(let _t=0;_t<6;_t++){ot=Bt[_t].mipmaps;for(let Lt=0;Lt<ot.length;Lt++){const Ot=ot[Lt];A.format!==zi?$t!==null?ee?Y&&i.compressedTexSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt,0,0,Ot.width,Ot.height,$t,Ot.data):i.compressedTexImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt,pe,Ot.width,Ot.height,0,Ot.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):ee?Y&&i.texSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt,0,0,Ot.width,Ot.height,$t,Ft,Ot.data):i.texImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt,pe,Ot.width,Ot.height,0,$t,Ft,Ot.data)}}}else{if(ot=A.mipmaps,ee&&Oe){ot.length>0&&Tt++;const _t=Zt(Bt[0]);i.texStorage2D(o.TEXTURE_CUBE_MAP,Tt,pe,_t.width,_t.height)}for(let _t=0;_t<6;_t++)if(xt){ee?Y&&i.texSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,0,0,0,Bt[_t].width,Bt[_t].height,$t,Ft,Bt[_t].data):i.texImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,0,pe,Bt[_t].width,Bt[_t].height,0,$t,Ft,Bt[_t].data);for(let Lt=0;Lt<ot.length;Lt++){const xe=ot[Lt].image[_t].image;ee?Y&&i.texSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt+1,0,0,xe.width,xe.height,$t,Ft,xe.data):i.texImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt+1,pe,xe.width,xe.height,0,$t,Ft,xe.data)}}else{ee?Y&&i.texSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,0,0,0,$t,Ft,Bt[_t]):i.texImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,0,pe,$t,Ft,Bt[_t]);for(let Lt=0;Lt<ot.length;Lt++){const Ot=ot[Lt];ee?Y&&i.texSubImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt+1,0,0,$t,Ft,Ot.image[_t]):i.texImage2D(o.TEXTURE_CUBE_MAP_POSITIVE_X+_t,Lt+1,pe,$t,Ft,Ot.image[_t])}}}x(A)&&S(o.TEXTURE_CUBE_MAP),mt.__version=vt.version,A.onUpdate&&A.onUpdate(A)}N.__version=A.version}function X(N,A,tt,pt,vt,mt){const kt=f.convert(tt.format,tt.colorSpace),wt=f.convert(tt.type),It=L(tt.internalFormat,kt,wt,tt.colorSpace);if(!r.get(A).__hasExternalTextures){const xt=Math.max(1,A.width>>mt),Bt=Math.max(1,A.height>>mt);vt===o.TEXTURE_3D||vt===o.TEXTURE_2D_ARRAY?i.texImage3D(vt,mt,It,xt,Bt,A.depth,0,kt,wt,null):i.texImage2D(vt,mt,It,xt,Bt,0,kt,wt,null)}i.bindFramebuffer(o.FRAMEBUFFER,N),ae(A)?d.framebufferTexture2DMultisampleEXT(o.FRAMEBUFFER,pt,vt,r.get(tt).__webglTexture,0,le(A)):(vt===o.TEXTURE_2D||vt>=o.TEXTURE_CUBE_MAP_POSITIVE_X&&vt<=o.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&o.framebufferTexture2D(o.FRAMEBUFFER,pt,vt,r.get(tt).__webglTexture,mt),i.bindFramebuffer(o.FRAMEBUFFER,null)}function dt(N,A,tt){if(o.bindRenderbuffer(o.RENDERBUFFER,N),A.depthBuffer){const pt=A.depthTexture,vt=pt&&pt.isDepthTexture?pt.type:null,mt=U(A.stencilBuffer,vt),kt=A.stencilBuffer?o.DEPTH_STENCIL_ATTACHMENT:o.DEPTH_ATTACHMENT,wt=le(A);ae(A)?d.renderbufferStorageMultisampleEXT(o.RENDERBUFFER,wt,mt,A.width,A.height):tt?o.renderbufferStorageMultisample(o.RENDERBUFFER,wt,mt,A.width,A.height):o.renderbufferStorage(o.RENDERBUFFER,mt,A.width,A.height),o.framebufferRenderbuffer(o.FRAMEBUFFER,kt,o.RENDERBUFFER,N)}else{const pt=A.textures;for(let vt=0;vt<pt.length;vt++){const mt=pt[vt],kt=f.convert(mt.format,mt.colorSpace),wt=f.convert(mt.type),It=L(mt.internalFormat,kt,wt,mt.colorSpace),ue=le(A);tt&&ae(A)===!1?o.renderbufferStorageMultisample(o.RENDERBUFFER,ue,It,A.width,A.height):ae(A)?d.renderbufferStorageMultisampleEXT(o.RENDERBUFFER,ue,It,A.width,A.height):o.renderbufferStorage(o.RENDERBUFFER,It,A.width,A.height)}}o.bindRenderbuffer(o.RENDERBUFFER,null)}function ht(N,A){if(A&&A.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(i.bindFramebuffer(o.FRAMEBUFFER,N),!(A.depthTexture&&A.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");(!r.get(A.depthTexture).__webglTexture||A.depthTexture.image.width!==A.width||A.depthTexture.image.height!==A.height)&&(A.depthTexture.image.width=A.width,A.depthTexture.image.height=A.height,A.depthTexture.needsUpdate=!0),lt(A.depthTexture,0);const pt=r.get(A.depthTexture).__webglTexture,vt=le(A);if(A.depthTexture.format===no)ae(A)?d.framebufferTexture2DMultisampleEXT(o.FRAMEBUFFER,o.DEPTH_ATTACHMENT,o.TEXTURE_2D,pt,0,vt):o.framebufferTexture2D(o.FRAMEBUFFER,o.DEPTH_ATTACHMENT,o.TEXTURE_2D,pt,0);else if(A.depthTexture.format===lo)ae(A)?d.framebufferTexture2DMultisampleEXT(o.FRAMEBUFFER,o.DEPTH_STENCIL_ATTACHMENT,o.TEXTURE_2D,pt,0,vt):o.framebufferTexture2D(o.FRAMEBUFFER,o.DEPTH_STENCIL_ATTACHMENT,o.TEXTURE_2D,pt,0);else throw new Error("Unknown depthTexture format")}function Ct(N){const A=r.get(N),tt=N.isWebGLCubeRenderTarget===!0;if(A.__boundDepthTexture!==N.depthTexture){const pt=N.depthTexture;if(A.__depthDisposeCallback&&A.__depthDisposeCallback(),pt){const vt=()=>{delete A.__boundDepthTexture,delete A.__depthDisposeCallback,pt.removeEventListener("dispose",vt)};pt.addEventListener("dispose",vt),A.__depthDisposeCallback=vt}A.__boundDepthTexture=pt}if(N.depthTexture&&!A.__autoAllocateDepthBuffer){if(tt)throw new Error("target.depthTexture not supported in Cube render targets");ht(A.__webglFramebuffer,N)}else if(tt){A.__webglDepthbuffer=[];for(let pt=0;pt<6;pt++)if(i.bindFramebuffer(o.FRAMEBUFFER,A.__webglFramebuffer[pt]),A.__webglDepthbuffer[pt]===void 0)A.__webglDepthbuffer[pt]=o.createRenderbuffer(),dt(A.__webglDepthbuffer[pt],N,!1);else{const vt=N.stencilBuffer?o.DEPTH_STENCIL_ATTACHMENT:o.DEPTH_ATTACHMENT,mt=A.__webglDepthbuffer[pt];o.bindRenderbuffer(o.RENDERBUFFER,mt),o.framebufferRenderbuffer(o.FRAMEBUFFER,vt,o.RENDERBUFFER,mt)}}else if(i.bindFramebuffer(o.FRAMEBUFFER,A.__webglFramebuffer),A.__webglDepthbuffer===void 0)A.__webglDepthbuffer=o.createRenderbuffer(),dt(A.__webglDepthbuffer,N,!1);else{const pt=N.stencilBuffer?o.DEPTH_STENCIL_ATTACHMENT:o.DEPTH_ATTACHMENT,vt=A.__webglDepthbuffer;o.bindRenderbuffer(o.RENDERBUFFER,vt),o.framebufferRenderbuffer(o.FRAMEBUFFER,pt,o.RENDERBUFFER,vt)}i.bindFramebuffer(o.FRAMEBUFFER,null)}function Rt(N,A,tt){const pt=r.get(N);A!==void 0&&X(pt.__webglFramebuffer,N,N.texture,o.COLOR_ATTACHMENT0,o.TEXTURE_2D,0),tt!==void 0&&Ct(N)}function Ht(N){const A=N.texture,tt=r.get(N),pt=r.get(A);N.addEventListener("dispose",B);const vt=N.textures,mt=N.isWebGLCubeRenderTarget===!0,kt=vt.length>1;if(kt||(pt.__webglTexture===void 0&&(pt.__webglTexture=o.createTexture()),pt.__version=A.version,h.memory.textures++),mt){tt.__webglFramebuffer=[];for(let wt=0;wt<6;wt++)if(A.mipmaps&&A.mipmaps.length>0){tt.__webglFramebuffer[wt]=[];for(let It=0;It<A.mipmaps.length;It++)tt.__webglFramebuffer[wt][It]=o.createFramebuffer()}else tt.__webglFramebuffer[wt]=o.createFramebuffer()}else{if(A.mipmaps&&A.mipmaps.length>0){tt.__webglFramebuffer=[];for(let wt=0;wt<A.mipmaps.length;wt++)tt.__webglFramebuffer[wt]=o.createFramebuffer()}else tt.__webglFramebuffer=o.createFramebuffer();if(kt)for(let wt=0,It=vt.length;wt<It;wt++){const ue=r.get(vt[wt]);ue.__webglTexture===void 0&&(ue.__webglTexture=o.createTexture(),h.memory.textures++)}if(N.samples>0&&ae(N)===!1){tt.__webglMultisampledFramebuffer=o.createFramebuffer(),tt.__webglColorRenderbuffer=[],i.bindFramebuffer(o.FRAMEBUFFER,tt.__webglMultisampledFramebuffer);for(let wt=0;wt<vt.length;wt++){const It=vt[wt];tt.__webglColorRenderbuffer[wt]=o.createRenderbuffer(),o.bindRenderbuffer(o.RENDERBUFFER,tt.__webglColorRenderbuffer[wt]);const ue=f.convert(It.format,It.colorSpace),xt=f.convert(It.type),Bt=L(It.internalFormat,ue,xt,It.colorSpace,N.isXRRenderTarget===!0),te=le(N);o.renderbufferStorageMultisample(o.RENDERBUFFER,te,Bt,N.width,N.height),o.framebufferRenderbuffer(o.FRAMEBUFFER,o.COLOR_ATTACHMENT0+wt,o.RENDERBUFFER,tt.__webglColorRenderbuffer[wt])}o.bindRenderbuffer(o.RENDERBUFFER,null),N.depthBuffer&&(tt.__webglDepthRenderbuffer=o.createRenderbuffer(),dt(tt.__webglDepthRenderbuffer,N,!0)),i.bindFramebuffer(o.FRAMEBUFFER,null)}}if(mt){i.bindTexture(o.TEXTURE_CUBE_MAP,pt.__webglTexture),Pt(o.TEXTURE_CUBE_MAP,A);for(let wt=0;wt<6;wt++)if(A.mipmaps&&A.mipmaps.length>0)for(let It=0;It<A.mipmaps.length;It++)X(tt.__webglFramebuffer[wt][It],N,A,o.COLOR_ATTACHMENT0,o.TEXTURE_CUBE_MAP_POSITIVE_X+wt,It);else X(tt.__webglFramebuffer[wt],N,A,o.COLOR_ATTACHMENT0,o.TEXTURE_CUBE_MAP_POSITIVE_X+wt,0);x(A)&&S(o.TEXTURE_CUBE_MAP),i.unbindTexture()}else if(kt){for(let wt=0,It=vt.length;wt<It;wt++){const ue=vt[wt],xt=r.get(ue);i.bindTexture(o.TEXTURE_2D,xt.__webglTexture),Pt(o.TEXTURE_2D,ue),X(tt.__webglFramebuffer,N,ue,o.COLOR_ATTACHMENT0+wt,o.TEXTURE_2D,0),x(ue)&&S(o.TEXTURE_2D)}i.unbindTexture()}else{let wt=o.TEXTURE_2D;if((N.isWebGL3DRenderTarget||N.isWebGLArrayRenderTarget)&&(wt=N.isWebGL3DRenderTarget?o.TEXTURE_3D:o.TEXTURE_2D_ARRAY),i.bindTexture(wt,pt.__webglTexture),Pt(wt,A),A.mipmaps&&A.mipmaps.length>0)for(let It=0;It<A.mipmaps.length;It++)X(tt.__webglFramebuffer[It],N,A,o.COLOR_ATTACHMENT0,wt,It);else X(tt.__webglFramebuffer,N,A,o.COLOR_ATTACHMENT0,wt,0);x(A)&&S(wt),i.unbindTexture()}N.depthBuffer&&Ct(N)}function Mt(N){const A=N.textures;for(let tt=0,pt=A.length;tt<pt;tt++){const vt=A[tt];if(x(vt)){const mt=N.isWebGLCubeRenderTarget?o.TEXTURE_CUBE_MAP:o.TEXTURE_2D,kt=r.get(vt).__webglTexture;i.bindTexture(mt,kt),S(mt),i.unbindTexture()}}}const bt=[],F=[];function vn(N){if(N.samples>0){if(ae(N)===!1){const A=N.textures,tt=N.width,pt=N.height;let vt=o.COLOR_BUFFER_BIT;const mt=N.stencilBuffer?o.DEPTH_STENCIL_ATTACHMENT:o.DEPTH_ATTACHMENT,kt=r.get(N),wt=A.length>1;if(wt)for(let It=0;It<A.length;It++)i.bindFramebuffer(o.FRAMEBUFFER,kt.__webglMultisampledFramebuffer),o.framebufferRenderbuffer(o.FRAMEBUFFER,o.COLOR_ATTACHMENT0+It,o.RENDERBUFFER,null),i.bindFramebuffer(o.FRAMEBUFFER,kt.__webglFramebuffer),o.framebufferTexture2D(o.DRAW_FRAMEBUFFER,o.COLOR_ATTACHMENT0+It,o.TEXTURE_2D,null,0);i.bindFramebuffer(o.READ_FRAMEBUFFER,kt.__webglMultisampledFramebuffer),i.bindFramebuffer(o.DRAW_FRAMEBUFFER,kt.__webglFramebuffer);for(let It=0;It<A.length;It++){if(N.resolveDepthBuffer&&(N.depthBuffer&&(vt|=o.DEPTH_BUFFER_BIT),N.stencilBuffer&&N.resolveStencilBuffer&&(vt|=o.STENCIL_BUFFER_BIT)),wt){o.framebufferRenderbuffer(o.READ_FRAMEBUFFER,o.COLOR_ATTACHMENT0,o.RENDERBUFFER,kt.__webglColorRenderbuffer[It]);const ue=r.get(A[It]).__webglTexture;o.framebufferTexture2D(o.DRAW_FRAMEBUFFER,o.COLOR_ATTACHMENT0,o.TEXTURE_2D,ue,0)}o.blitFramebuffer(0,0,tt,pt,0,0,tt,pt,vt,o.NEAREST),p===!0&&(bt.length=0,F.length=0,bt.push(o.COLOR_ATTACHMENT0+It),N.depthBuffer&&N.resolveDepthBuffer===!1&&(bt.push(mt),F.push(mt),o.invalidateFramebuffer(o.DRAW_FRAMEBUFFER,F)),o.invalidateFramebuffer(o.READ_FRAMEBUFFER,bt))}if(i.bindFramebuffer(o.READ_FRAMEBUFFER,null),i.bindFramebuffer(o.DRAW_FRAMEBUFFER,null),wt)for(let It=0;It<A.length;It++){i.bindFramebuffer(o.FRAMEBUFFER,kt.__webglMultisampledFramebuffer),o.framebufferRenderbuffer(o.FRAMEBUFFER,o.COLOR_ATTACHMENT0+It,o.RENDERBUFFER,kt.__webglColorRenderbuffer[It]);const ue=r.get(A[It]).__webglTexture;i.bindFramebuffer(o.FRAMEBUFFER,kt.__webglFramebuffer),o.framebufferTexture2D(o.DRAW_FRAMEBUFFER,o.COLOR_ATTACHMENT0+It,o.TEXTURE_2D,ue,0)}i.bindFramebuffer(o.DRAW_FRAMEBUFFER,kt.__webglMultisampledFramebuffer)}else if(N.depthBuffer&&N.resolveDepthBuffer===!1&&p){const A=N.stencilBuffer?o.DEPTH_STENCIL_ATTACHMENT:o.DEPTH_ATTACHMENT;o.invalidateFramebuffer(o.DRAW_FRAMEBUFFER,[A])}}}function le(N){return Math.min(u.maxSamples,N.samples)}function ae(N){const A=r.get(N);return N.samples>0&&e.has("WEBGL_multisampled_render_to_texture")===!0&&A.__useRenderToTexture!==!1}function Xt(N){const A=h.render.frame;v.get(N)!==A&&(v.set(N,A),N.update())}function Kt(N,A){const tt=N.colorSpace,pt=N.format,vt=N.type;return N.isCompressedTexture===!0||N.isVideoTexture===!0||tt!==cs&&tt!==ss&&(De.getTransfer(tt)===Xe?(pt!==zi||vt!==Ea)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",tt)),A}function Zt(N){return typeof HTMLImageElement<"u"&&N instanceof HTMLImageElement?(g.width=N.naturalWidth||N.width,g.height=N.naturalHeight||N.height):typeof VideoFrame<"u"&&N instanceof VideoFrame?(g.width=N.displayWidth,g.height=N.displayHeight):(g.width=N.width,g.height=N.height),g}this.allocateTextureUnit=nt,this.resetTextureUnits=w,this.setTexture2D=lt,this.setTexture2DArray=ft,this.setTexture3D=H,this.setTextureCube=at,this.rebindTextures=Rt,this.setupRenderTarget=Ht,this.updateRenderTargetMipmap=Mt,this.updateMultisampleRenderTarget=vn,this.setupDepthRenderbuffer=Ct,this.setupFrameBufferTexture=X,this.useMultisampledRTT=ae}function zR(o,e){function i(r,u=ss){let f;const h=De.getTransfer(u);if(r===Ea)return o.UNSIGNED_BYTE;if(r===Ip)return o.UNSIGNED_SHORT_4_4_4_4;if(r===Bp)return o.UNSIGNED_SHORT_5_5_5_1;if(r===xS)return o.UNSIGNED_INT_5_9_9_9_REV;if(r===SS)return o.BYTE;if(r===yS)return o.SHORT;if(r===ml)return o.UNSIGNED_SHORT;if(r===zp)return o.INT;if(r===ks)return o.UNSIGNED_INT;if(r===xa)return o.FLOAT;if(r===_l)return o.HALF_FLOAT;if(r===MS)return o.ALPHA;if(r===ES)return o.RGB;if(r===zi)return o.RGBA;if(r===TS)return o.LUMINANCE;if(r===bS)return o.LUMINANCE_ALPHA;if(r===no)return o.DEPTH_COMPONENT;if(r===lo)return o.DEPTH_STENCIL;if(r===AS)return o.RED;if(r===Fp)return o.RED_INTEGER;if(r===RS)return o.RG;if(r===Hp)return o.RG_INTEGER;if(r===Gp)return o.RGBA_INTEGER;if(r===_c||r===gc||r===vc||r===Sc)if(h===Xe)if(f=e.get("WEBGL_compressed_texture_s3tc_srgb"),f!==null){if(r===_c)return f.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(r===gc)return f.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(r===vc)return f.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(r===Sc)return f.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(f=e.get("WEBGL_compressed_texture_s3tc"),f!==null){if(r===_c)return f.COMPRESSED_RGB_S3TC_DXT1_EXT;if(r===gc)return f.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(r===vc)return f.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(r===Sc)return f.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(r===rp||r===op||r===lp||r===up)if(f=e.get("WEBGL_compressed_texture_pvrtc"),f!==null){if(r===rp)return f.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(r===op)return f.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(r===lp)return f.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(r===up)return f.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(r===cp||r===fp||r===hp)if(f=e.get("WEBGL_compressed_texture_etc"),f!==null){if(r===cp||r===fp)return h===Xe?f.COMPRESSED_SRGB8_ETC2:f.COMPRESSED_RGB8_ETC2;if(r===hp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:f.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(r===dp||r===pp||r===mp||r===_p||r===gp||r===vp||r===Sp||r===yp||r===xp||r===Mp||r===Ep||r===Tp||r===bp||r===Ap)if(f=e.get("WEBGL_compressed_texture_astc"),f!==null){if(r===dp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:f.COMPRESSED_RGBA_ASTC_4x4_KHR;if(r===pp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:f.COMPRESSED_RGBA_ASTC_5x4_KHR;if(r===mp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:f.COMPRESSED_RGBA_ASTC_5x5_KHR;if(r===_p)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:f.COMPRESSED_RGBA_ASTC_6x5_KHR;if(r===gp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:f.COMPRESSED_RGBA_ASTC_6x6_KHR;if(r===vp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:f.COMPRESSED_RGBA_ASTC_8x5_KHR;if(r===Sp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:f.COMPRESSED_RGBA_ASTC_8x6_KHR;if(r===yp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:f.COMPRESSED_RGBA_ASTC_8x8_KHR;if(r===xp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:f.COMPRESSED_RGBA_ASTC_10x5_KHR;if(r===Mp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:f.COMPRESSED_RGBA_ASTC_10x6_KHR;if(r===Ep)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:f.COMPRESSED_RGBA_ASTC_10x8_KHR;if(r===Tp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:f.COMPRESSED_RGBA_ASTC_10x10_KHR;if(r===bp)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:f.COMPRESSED_RGBA_ASTC_12x10_KHR;if(r===Ap)return h===Xe?f.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:f.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(r===yc||r===Rp||r===Cp)if(f=e.get("EXT_texture_compression_bptc"),f!==null){if(r===yc)return h===Xe?f.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:f.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(r===Rp)return f.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(r===Cp)return f.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(r===CS||r===wp||r===Dp||r===Up)if(f=e.get("EXT_texture_compression_rgtc"),f!==null){if(r===yc)return f.COMPRESSED_RED_RGTC1_EXT;if(r===wp)return f.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(r===Dp)return f.COMPRESSED_RED_GREEN_RGTC2_EXT;if(r===Up)return f.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return r===oo?o.UNSIGNED_INT_24_8:o[r]!==void 0?o[r]:null}return{convert:i}}class IR extends Si{constructor(e=[]){super(),this.isArrayCamera=!0,this.cameras=e}}class dl extends bn{constructor(){super(),this.isGroup=!0,this.type="Group"}}const BR={type:"move"};class Xd{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new dl,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new dl,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new Q,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new Q),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new dl,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new Q,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new Q),this._grip}dispatchEvent(e){return this._targetRay!==null&&this._targetRay.dispatchEvent(e),this._grip!==null&&this._grip.dispatchEvent(e),this._hand!==null&&this._hand.dispatchEvent(e),this}connect(e){if(e&&e.hand){const i=this._hand;if(i)for(const r of e.hand.values())this._getHandJoint(i,r)}return this.dispatchEvent({type:"connected",data:e}),this}disconnect(e){return this.dispatchEvent({type:"disconnected",data:e}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(e,i,r){let u=null,f=null,h=null;const d=this._targetRay,p=this._grip,g=this._hand;if(e&&i.session.visibilityState!=="visible-blurred"){if(g&&e.hand){h=!0;for(const R of e.hand.values()){const x=i.getJointPose(R,r),S=this._getHandJoint(g,R);x!==null&&(S.matrix.fromArray(x.transform.matrix),S.matrix.decompose(S.position,S.rotation,S.scale),S.matrixWorldNeedsUpdate=!0,S.jointRadius=x.radius),S.visible=x!==null}const v=g.joints["index-finger-tip"],_=g.joints["thumb-tip"],y=v.position.distanceTo(_.position),M=.02,E=.005;g.inputState.pinching&&y>M+E?(g.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:e.handedness,target:this})):!g.inputState.pinching&&y<=M-E&&(g.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:e.handedness,target:this}))}else p!==null&&e.gripSpace&&(f=i.getPose(e.gripSpace,r),f!==null&&(p.matrix.fromArray(f.transform.matrix),p.matrix.decompose(p.position,p.rotation,p.scale),p.matrixWorldNeedsUpdate=!0,f.linearVelocity?(p.hasLinearVelocity=!0,p.linearVelocity.copy(f.linearVelocity)):p.hasLinearVelocity=!1,f.angularVelocity?(p.hasAngularVelocity=!0,p.angularVelocity.copy(f.angularVelocity)):p.hasAngularVelocity=!1));d!==null&&(u=i.getPose(e.targetRaySpace,r),u===null&&f!==null&&(u=f),u!==null&&(d.matrix.fromArray(u.transform.matrix),d.matrix.decompose(d.position,d.rotation,d.scale),d.matrixWorldNeedsUpdate=!0,u.linearVelocity?(d.hasLinearVelocity=!0,d.linearVelocity.copy(u.linearVelocity)):d.hasLinearVelocity=!1,u.angularVelocity?(d.hasAngularVelocity=!0,d.angularVelocity.copy(u.angularVelocity)):d.hasAngularVelocity=!1,this.dispatchEvent(BR)))}return d!==null&&(d.visible=u!==null),p!==null&&(p.visible=f!==null),g!==null&&(g.visible=h!==null),this}_getHandJoint(e,i){if(e.joints[i.jointName]===void 0){const r=new dl;r.matrixAutoUpdate=!1,r.visible=!1,e.joints[i.jointName]=r,e.add(r)}return e.joints[i.jointName]}}const FR=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,HR=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`;class GR{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(e,i,r){if(this.texture===null){const u=new Kn,f=e.properties.get(u);f.__webglTexture=i.texture,(i.depthNear!=r.depthNear||i.depthFar!=r.depthFar)&&(this.depthNear=i.depthNear,this.depthFar=i.depthFar),this.texture=u}}getMesh(e){if(this.texture!==null&&this.mesh===null){const i=e.cameras[0].viewport,r=new us({vertexShader:FR,fragmentShader:HR,uniforms:{depthColor:{value:this.texture},depthWidth:{value:i.z},depthHeight:{value:i.w}}});this.mesh=new jn(new yl(20,20),r)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}}class VR extends Zs{constructor(e,i){super();const r=this;let u=null,f=1,h=null,d="local-floor",p=1,g=null,v=null,_=null,y=null,M=null,E=null;const R=new GR,x=i.getContextAttributes();let S=null,L=null;const U=[],P=[],J=new ce;let B=null;const O=new Si;O.layers.enable(1),O.viewport=new Je;const V=new Si;V.layers.enable(2),V.viewport=new Je;const gt=[O,V],T=new IR;T.layers.enable(1),T.layers.enable(2);let w=null,nt=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(D){let X=U[D];return X===void 0&&(X=new Xd,U[D]=X),X.getTargetRaySpace()},this.getControllerGrip=function(D){let X=U[D];return X===void 0&&(X=new Xd,U[D]=X),X.getGripSpace()},this.getHand=function(D){let X=U[D];return X===void 0&&(X=new Xd,U[D]=X),X.getHandSpace()};function rt(D){const X=P.indexOf(D.inputSource);if(X===-1)return;const dt=U[X];dt!==void 0&&(dt.update(D.inputSource,D.frame,g||h),dt.dispatchEvent({type:D.type,data:D.inputSource}))}function lt(){u.removeEventListener("select",rt),u.removeEventListener("selectstart",rt),u.removeEventListener("selectend",rt),u.removeEventListener("squeeze",rt),u.removeEventListener("squeezestart",rt),u.removeEventListener("squeezeend",rt),u.removeEventListener("end",lt),u.removeEventListener("inputsourceschange",ft);for(let D=0;D<U.length;D++){const X=P[D];X!==null&&(P[D]=null,U[D].disconnect(X))}w=null,nt=null,R.reset(),e.setRenderTarget(S),M=null,y=null,_=null,u=null,L=null,me.stop(),r.isPresenting=!1,e.setPixelRatio(B),e.setSize(J.width,J.height,!1),r.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(D){f=D,r.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(D){d=D,r.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return g||h},this.setReferenceSpace=function(D){g=D},this.getBaseLayer=function(){return y!==null?y:M},this.getBinding=function(){return _},this.getFrame=function(){return E},this.getSession=function(){return u},this.setSession=async function(D){if(u=D,u!==null){if(S=e.getRenderTarget(),u.addEventListener("select",rt),u.addEventListener("selectstart",rt),u.addEventListener("selectend",rt),u.addEventListener("squeeze",rt),u.addEventListener("squeezestart",rt),u.addEventListener("squeezeend",rt),u.addEventListener("end",lt),u.addEventListener("inputsourceschange",ft),x.xrCompatible!==!0&&await i.makeXRCompatible(),B=e.getPixelRatio(),e.getSize(J),u.renderState.layers===void 0){const X={antialias:x.antialias,alpha:!0,depth:x.depth,stencil:x.stencil,framebufferScaleFactor:f};M=new XRWebGLLayer(u,i,X),u.updateRenderState({baseLayer:M}),e.setPixelRatio(1),e.setSize(M.framebufferWidth,M.framebufferHeight,!1),L=new qs(M.framebufferWidth,M.framebufferHeight,{format:zi,type:Ea,colorSpace:e.outputColorSpace,stencilBuffer:x.stencil})}else{let X=null,dt=null,ht=null;x.depth&&(ht=x.stencil?i.DEPTH24_STENCIL8:i.DEPTH_COMPONENT24,X=x.stencil?lo:no,dt=x.stencil?oo:ks);const Ct={colorFormat:i.RGBA8,depthFormat:ht,scaleFactor:f};_=new XRWebGLBinding(u,i),y=_.createProjectionLayer(Ct),u.updateRenderState({layers:[y]}),e.setPixelRatio(1),e.setSize(y.textureWidth,y.textureHeight,!1),L=new qs(y.textureWidth,y.textureHeight,{format:zi,type:Ea,depthTexture:new VS(y.textureWidth,y.textureHeight,dt,void 0,void 0,void 0,void 0,void 0,void 0,X),stencilBuffer:x.stencil,colorSpace:e.outputColorSpace,samples:x.antialias?4:0,resolveDepthBuffer:y.ignoreDepthValues===!1})}L.isXRRenderTarget=!0,this.setFoveation(p),g=null,h=await u.requestReferenceSpace(d),me.setContext(u),me.start(),r.isPresenting=!0,r.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(u!==null)return u.environmentBlendMode},this.getDepthTexture=function(){return R.getDepthTexture()};function ft(D){for(let X=0;X<D.removed.length;X++){const dt=D.removed[X],ht=P.indexOf(dt);ht>=0&&(P[ht]=null,U[ht].disconnect(dt))}for(let X=0;X<D.added.length;X++){const dt=D.added[X];let ht=P.indexOf(dt);if(ht===-1){for(let Rt=0;Rt<U.length;Rt++)if(Rt>=P.length){P.push(dt),ht=Rt;break}else if(P[Rt]===null){P[Rt]=dt,ht=Rt;break}if(ht===-1)break}const Ct=U[ht];Ct&&Ct.connect(dt)}}const H=new Q,at=new Q;function Z(D,X,dt){H.setFromMatrixPosition(X.matrixWorld),at.setFromMatrixPosition(dt.matrixWorld);const ht=H.distanceTo(at),Ct=X.projectionMatrix.elements,Rt=dt.projectionMatrix.elements,Ht=Ct[14]/(Ct[10]-1),Mt=Ct[14]/(Ct[10]+1),bt=(Ct[9]+1)/Ct[5],F=(Ct[9]-1)/Ct[5],vn=(Ct[8]-1)/Ct[0],le=(Rt[8]+1)/Rt[0],ae=Ht*vn,Xt=Ht*le,Kt=ht/(-vn+le),Zt=Kt*-vn;if(X.matrixWorld.decompose(D.position,D.quaternion,D.scale),D.translateX(Zt),D.translateZ(Kt),D.matrixWorld.compose(D.position,D.quaternion,D.scale),D.matrixWorldInverse.copy(D.matrixWorld).invert(),Ct[10]===-1)D.projectionMatrix.copy(X.projectionMatrix),D.projectionMatrixInverse.copy(X.projectionMatrixInverse);else{const N=Ht+Kt,A=Mt+Kt,tt=ae-Zt,pt=Xt+(ht-Zt),vt=bt*Mt/A*N,mt=F*Mt/A*N;D.projectionMatrix.makePerspective(tt,pt,vt,mt,N,A),D.projectionMatrixInverse.copy(D.projectionMatrix).invert()}}function yt(D,X){X===null?D.matrixWorld.copy(D.matrix):D.matrixWorld.multiplyMatrices(X.matrixWorld,D.matrix),D.matrixWorldInverse.copy(D.matrixWorld).invert()}this.updateCamera=function(D){if(u===null)return;let X=D.near,dt=D.far;R.texture!==null&&(R.depthNear>0&&(X=R.depthNear),R.depthFar>0&&(dt=R.depthFar)),T.near=V.near=O.near=X,T.far=V.far=O.far=dt,(w!==T.near||nt!==T.far)&&(u.updateRenderState({depthNear:T.near,depthFar:T.far}),w=T.near,nt=T.far);const ht=D.parent,Ct=T.cameras;yt(T,ht);for(let Rt=0;Rt<Ct.length;Rt++)yt(Ct[Rt],ht);Ct.length===2?Z(T,O,V):T.projectionMatrix.copy(O.projectionMatrix),St(D,T,ht)};function St(D,X,dt){dt===null?D.matrix.copy(X.matrixWorld):(D.matrix.copy(dt.matrixWorld),D.matrix.invert(),D.matrix.multiply(X.matrixWorld)),D.matrix.decompose(D.position,D.quaternion,D.scale),D.updateMatrixWorld(!0),D.projectionMatrix.copy(X.projectionMatrix),D.projectionMatrixInverse.copy(X.projectionMatrixInverse),D.isPerspectiveCamera&&(D.fov=Np*2*Math.atan(1/D.projectionMatrix.elements[5]),D.zoom=1)}this.getCamera=function(){return T},this.getFoveation=function(){if(!(y===null&&M===null))return p},this.setFoveation=function(D){p=D,y!==null&&(y.fixedFoveation=D),M!==null&&M.fixedFoveation!==void 0&&(M.fixedFoveation=D)},this.hasDepthSensing=function(){return R.texture!==null},this.getDepthSensingMesh=function(){return R.getMesh(T)};let Pt=null;function oe(D,X){if(v=X.getViewerPose(g||h),E=X,v!==null){const dt=v.views;M!==null&&(e.setRenderTargetFramebuffer(L,M.framebuffer),e.setRenderTarget(L));let ht=!1;dt.length!==T.cameras.length&&(T.cameras.length=0,ht=!0);for(let Rt=0;Rt<dt.length;Rt++){const Ht=dt[Rt];let Mt=null;if(M!==null)Mt=M.getViewport(Ht);else{const F=_.getViewSubImage(y,Ht);Mt=F.viewport,Rt===0&&(e.setRenderTargetTextures(L,F.colorTexture,y.ignoreDepthValues?void 0:F.depthStencilTexture),e.setRenderTarget(L))}let bt=gt[Rt];bt===void 0&&(bt=new Si,bt.layers.enable(Rt),bt.viewport=new Je,gt[Rt]=bt),bt.matrix.fromArray(Ht.transform.matrix),bt.matrix.decompose(bt.position,bt.quaternion,bt.scale),bt.projectionMatrix.fromArray(Ht.projectionMatrix),bt.projectionMatrixInverse.copy(bt.projectionMatrix).invert(),bt.viewport.set(Mt.x,Mt.y,Mt.width,Mt.height),Rt===0&&(T.matrix.copy(bt.matrix),T.matrix.decompose(T.position,T.quaternion,T.scale)),ht===!0&&T.cameras.push(bt)}const Ct=u.enabledFeatures;if(Ct&&Ct.includes("depth-sensing")){const Rt=_.getDepthInformation(dt[0]);Rt&&Rt.isValid&&Rt.texture&&R.init(e,Rt,u.renderState)}}for(let dt=0;dt<U.length;dt++){const ht=P[dt],Ct=U[dt];ht!==null&&Ct!==void 0&&Ct.update(ht,X,g||h)}Pt&&Pt(D,X),X.detectedPlanes&&r.dispatchEvent({type:"planesdetected",data:X}),E=null}const me=new HS;me.setAnimationLoop(oe),this.setAnimationLoop=function(D){Pt=D},this.dispose=function(){}}}const Fs=new Ta,XR=new Ze;function YR(o,e){function i(x,S){x.matrixAutoUpdate===!0&&x.updateMatrix(),S.value.copy(x.matrix)}function r(x,S){S.color.getRGB(x.fogColor.value,IS(o)),S.isFog?(x.fogNear.value=S.near,x.fogFar.value=S.far):S.isFogExp2&&(x.fogDensity.value=S.density)}function u(x,S,L,U,P){S.isMeshBasicMaterial||S.isMeshLambertMaterial?f(x,S):S.isMeshToonMaterial?(f(x,S),_(x,S)):S.isMeshPhongMaterial?(f(x,S),v(x,S)):S.isMeshStandardMaterial?(f(x,S),y(x,S),S.isMeshPhysicalMaterial&&M(x,S,P)):S.isMeshMatcapMaterial?(f(x,S),E(x,S)):S.isMeshDepthMaterial?f(x,S):S.isMeshDistanceMaterial?(f(x,S),R(x,S)):S.isMeshNormalMaterial?f(x,S):S.isLineBasicMaterial?(h(x,S),S.isLineDashedMaterial&&d(x,S)):S.isPointsMaterial?p(x,S,L,U):S.isSpriteMaterial?g(x,S):S.isShadowMaterial?(x.color.value.copy(S.color),x.opacity.value=S.opacity):S.isShaderMaterial&&(S.uniformsNeedUpdate=!1)}function f(x,S){x.opacity.value=S.opacity,S.color&&x.diffuse.value.copy(S.color),S.emissive&&x.emissive.value.copy(S.emissive).multiplyScalar(S.emissiveIntensity),S.map&&(x.map.value=S.map,i(S.map,x.mapTransform)),S.alphaMap&&(x.alphaMap.value=S.alphaMap,i(S.alphaMap,x.alphaMapTransform)),S.bumpMap&&(x.bumpMap.value=S.bumpMap,i(S.bumpMap,x.bumpMapTransform),x.bumpScale.value=S.bumpScale,S.side===Zn&&(x.bumpScale.value*=-1)),S.normalMap&&(x.normalMap.value=S.normalMap,i(S.normalMap,x.normalMapTransform),x.normalScale.value.copy(S.normalScale),S.side===Zn&&x.normalScale.value.negate()),S.displacementMap&&(x.displacementMap.value=S.displacementMap,i(S.displacementMap,x.displacementMapTransform),x.displacementScale.value=S.displacementScale,x.displacementBias.value=S.displacementBias),S.emissiveMap&&(x.emissiveMap.value=S.emissiveMap,i(S.emissiveMap,x.emissiveMapTransform)),S.specularMap&&(x.specularMap.value=S.specularMap,i(S.specularMap,x.specularMapTransform)),S.alphaTest>0&&(x.alphaTest.value=S.alphaTest);const L=e.get(S),U=L.envMap,P=L.envMapRotation;U&&(x.envMap.value=U,Fs.copy(P),Fs.x*=-1,Fs.y*=-1,Fs.z*=-1,U.isCubeTexture&&U.isRenderTargetTexture===!1&&(Fs.y*=-1,Fs.z*=-1),x.envMapRotation.value.setFromMatrix4(XR.makeRotationFromEuler(Fs)),x.flipEnvMap.value=U.isCubeTexture&&U.isRenderTargetTexture===!1?-1:1,x.reflectivity.value=S.reflectivity,x.ior.value=S.ior,x.refractionRatio.value=S.refractionRatio),S.lightMap&&(x.lightMap.value=S.lightMap,x.lightMapIntensity.value=S.lightMapIntensity,i(S.lightMap,x.lightMapTransform)),S.aoMap&&(x.aoMap.value=S.aoMap,x.aoMapIntensity.value=S.aoMapIntensity,i(S.aoMap,x.aoMapTransform))}function h(x,S){x.diffuse.value.copy(S.color),x.opacity.value=S.opacity,S.map&&(x.map.value=S.map,i(S.map,x.mapTransform))}function d(x,S){x.dashSize.value=S.dashSize,x.totalSize.value=S.dashSize+S.gapSize,x.scale.value=S.scale}function p(x,S,L,U){x.diffuse.value.copy(S.color),x.opacity.value=S.opacity,x.size.value=S.size*L,x.scale.value=U*.5,S.map&&(x.map.value=S.map,i(S.map,x.uvTransform)),S.alphaMap&&(x.alphaMap.value=S.alphaMap,i(S.alphaMap,x.alphaMapTransform)),S.alphaTest>0&&(x.alphaTest.value=S.alphaTest)}function g(x,S){x.diffuse.value.copy(S.color),x.opacity.value=S.opacity,x.rotation.value=S.rotation,S.map&&(x.map.value=S.map,i(S.map,x.mapTransform)),S.alphaMap&&(x.alphaMap.value=S.alphaMap,i(S.alphaMap,x.alphaMapTransform)),S.alphaTest>0&&(x.alphaTest.value=S.alphaTest)}function v(x,S){x.specular.value.copy(S.specular),x.shininess.value=Math.max(S.shininess,1e-4)}function _(x,S){S.gradientMap&&(x.gradientMap.value=S.gradientMap)}function y(x,S){x.metalness.value=S.metalness,S.metalnessMap&&(x.metalnessMap.value=S.metalnessMap,i(S.metalnessMap,x.metalnessMapTransform)),x.roughness.value=S.roughness,S.roughnessMap&&(x.roughnessMap.value=S.roughnessMap,i(S.roughnessMap,x.roughnessMapTransform)),S.envMap&&(x.envMapIntensity.value=S.envMapIntensity)}function M(x,S,L){x.ior.value=S.ior,S.sheen>0&&(x.sheenColor.value.copy(S.sheenColor).multiplyScalar(S.sheen),x.sheenRoughness.value=S.sheenRoughness,S.sheenColorMap&&(x.sheenColorMap.value=S.sheenColorMap,i(S.sheenColorMap,x.sheenColorMapTransform)),S.sheenRoughnessMap&&(x.sheenRoughnessMap.value=S.sheenRoughnessMap,i(S.sheenRoughnessMap,x.sheenRoughnessMapTransform))),S.clearcoat>0&&(x.clearcoat.value=S.clearcoat,x.clearcoatRoughness.value=S.clearcoatRoughness,S.clearcoatMap&&(x.clearcoatMap.value=S.clearcoatMap,i(S.clearcoatMap,x.clearcoatMapTransform)),S.clearcoatRoughnessMap&&(x.clearcoatRoughnessMap.value=S.clearcoatRoughnessMap,i(S.clearcoatRoughnessMap,x.clearcoatRoughnessMapTransform)),S.clearcoatNormalMap&&(x.clearcoatNormalMap.value=S.clearcoatNormalMap,i(S.clearcoatNormalMap,x.clearcoatNormalMapTransform),x.clearcoatNormalScale.value.copy(S.clearcoatNormalScale),S.side===Zn&&x.clearcoatNormalScale.value.negate())),S.dispersion>0&&(x.dispersion.value=S.dispersion),S.iridescence>0&&(x.iridescence.value=S.iridescence,x.iridescenceIOR.value=S.iridescenceIOR,x.iridescenceThicknessMinimum.value=S.iridescenceThicknessRange[0],x.iridescenceThicknessMaximum.value=S.iridescenceThicknessRange[1],S.iridescenceMap&&(x.iridescenceMap.value=S.iridescenceMap,i(S.iridescenceMap,x.iridescenceMapTransform)),S.iridescenceThicknessMap&&(x.iridescenceThicknessMap.value=S.iridescenceThicknessMap,i(S.iridescenceThicknessMap,x.iridescenceThicknessMapTransform))),S.transmission>0&&(x.transmission.value=S.transmission,x.transmissionSamplerMap.value=L.texture,x.transmissionSamplerSize.value.set(L.width,L.height),S.transmissionMap&&(x.transmissionMap.value=S.transmissionMap,i(S.transmissionMap,x.transmissionMapTransform)),x.thickness.value=S.thickness,S.thicknessMap&&(x.thicknessMap.value=S.thicknessMap,i(S.thicknessMap,x.thicknessMapTransform)),x.attenuationDistance.value=S.attenuationDistance,x.attenuationColor.value.copy(S.attenuationColor)),S.anisotropy>0&&(x.anisotropyVector.value.set(S.anisotropy*Math.cos(S.anisotropyRotation),S.anisotropy*Math.sin(S.anisotropyRotation)),S.anisotropyMap&&(x.anisotropyMap.value=S.anisotropyMap,i(S.anisotropyMap,x.anisotropyMapTransform))),x.specularIntensity.value=S.specularIntensity,x.specularColor.value.copy(S.specularColor),S.specularColorMap&&(x.specularColorMap.value=S.specularColorMap,i(S.specularColorMap,x.specularColorMapTransform)),S.specularIntensityMap&&(x.specularIntensityMap.value=S.specularIntensityMap,i(S.specularIntensityMap,x.specularIntensityMapTransform))}function E(x,S){S.matcap&&(x.matcap.value=S.matcap)}function R(x,S){const L=e.get(S).light;x.referencePosition.value.setFromMatrixPosition(L.matrixWorld),x.nearDistance.value=L.shadow.camera.near,x.farDistance.value=L.shadow.camera.far}return{refreshFogUniforms:r,refreshMaterialUniforms:u}}function kR(o,e,i,r){let u={},f={},h=[];const d=o.getParameter(o.MAX_UNIFORM_BUFFER_BINDINGS);function p(L,U){const P=U.program;r.uniformBlockBinding(L,P)}function g(L,U){let P=u[L.id];P===void 0&&(E(L),P=v(L),u[L.id]=P,L.addEventListener("dispose",x));const J=U.program;r.updateUBOMapping(L,J);const B=e.render.frame;f[L.id]!==B&&(y(L),f[L.id]=B)}function v(L){const U=_();L.__bindingPointIndex=U;const P=o.createBuffer(),J=L.__size,B=L.usage;return o.bindBuffer(o.UNIFORM_BUFFER,P),o.bufferData(o.UNIFORM_BUFFER,J,B),o.bindBuffer(o.UNIFORM_BUFFER,null),o.bindBufferBase(o.UNIFORM_BUFFER,U,P),P}function _(){for(let L=0;L<d;L++)if(h.indexOf(L)===-1)return h.push(L),L;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function y(L){const U=u[L.id],P=L.uniforms,J=L.__cache;o.bindBuffer(o.UNIFORM_BUFFER,U);for(let B=0,O=P.length;B<O;B++){const V=Array.isArray(P[B])?P[B]:[P[B]];for(let gt=0,T=V.length;gt<T;gt++){const w=V[gt];if(M(w,B,gt,J)===!0){const nt=w.__offset,rt=Array.isArray(w.value)?w.value:[w.value];let lt=0;for(let ft=0;ft<rt.length;ft++){const H=rt[ft],at=R(H);typeof H=="number"||typeof H=="boolean"?(w.__data[0]=H,o.bufferSubData(o.UNIFORM_BUFFER,nt+lt,w.__data)):H.isMatrix3?(w.__data[0]=H.elements[0],w.__data[1]=H.elements[1],w.__data[2]=H.elements[2],w.__data[3]=0,w.__data[4]=H.elements[3],w.__data[5]=H.elements[4],w.__data[6]=H.elements[5],w.__data[7]=0,w.__data[8]=H.elements[6],w.__data[9]=H.elements[7],w.__data[10]=H.elements[8],w.__data[11]=0):(H.toArray(w.__data,lt),lt+=at.storage/Float32Array.BYTES_PER_ELEMENT)}o.bufferSubData(o.UNIFORM_BUFFER,nt,w.__data)}}}o.bindBuffer(o.UNIFORM_BUFFER,null)}function M(L,U,P,J){const B=L.value,O=U+"_"+P;if(J[O]===void 0)return typeof B=="number"||typeof B=="boolean"?J[O]=B:J[O]=B.clone(),!0;{const V=J[O];if(typeof B=="number"||typeof B=="boolean"){if(V!==B)return J[O]=B,!0}else if(V.equals(B)===!1)return V.copy(B),!0}return!1}function E(L){const U=L.uniforms;let P=0;const J=16;for(let O=0,V=U.length;O<V;O++){const gt=Array.isArray(U[O])?U[O]:[U[O]];for(let T=0,w=gt.length;T<w;T++){const nt=gt[T],rt=Array.isArray(nt.value)?nt.value:[nt.value];for(let lt=0,ft=rt.length;lt<ft;lt++){const H=rt[lt],at=R(H),Z=P%J,yt=Z%at.boundary,St=Z+yt;P+=yt,St!==0&&J-St<at.storage&&(P+=J-St),nt.__data=new Float32Array(at.storage/Float32Array.BYTES_PER_ELEMENT),nt.__offset=P,P+=at.storage}}}const B=P%J;return B>0&&(P+=J-B),L.__size=P,L.__cache={},this}function R(L){const U={boundary:0,storage:0};return typeof L=="number"||typeof L=="boolean"?(U.boundary=4,U.storage=4):L.isVector2?(U.boundary=8,U.storage=8):L.isVector3||L.isColor?(U.boundary=16,U.storage=12):L.isVector4?(U.boundary=16,U.storage=16):L.isMatrix3?(U.boundary=48,U.storage=48):L.isMatrix4?(U.boundary=64,U.storage=64):L.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",L),U}function x(L){const U=L.target;U.removeEventListener("dispose",x);const P=h.indexOf(U.__bindingPointIndex);h.splice(P,1),o.deleteBuffer(u[U.id]),delete u[U.id],delete f[U.id]}function S(){for(const L in u)o.deleteBuffer(u[L]);h=[],u={},f={}}return{bind:p,update:g,dispose:S}}class qR{constructor(e={}){const{canvas:i=LE(),context:r=null,depth:u=!0,stencil:f=!1,alpha:h=!1,antialias:d=!1,premultipliedAlpha:p=!0,preserveDrawingBuffer:g=!1,powerPreference:v="default",failIfMajorPerformanceCaveat:_=!1}=e;this.isWebGLRenderer=!0;let y;if(r!==null){if(typeof WebGLRenderingContext<"u"&&r instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");y=r.getContextAttributes().alpha}else y=h;const M=new Uint32Array(4),E=new Int32Array(4);let R=null,x=null;const S=[],L=[];this.domElement=i,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this._outputColorSpace=ji,this.toneMapping=os,this.toneMappingExposure=1;const U=this;let P=!1,J=0,B=0,O=null,V=-1,gt=null;const T=new Je,w=new Je;let nt=null;const rt=new ye(0);let lt=0,ft=i.width,H=i.height,at=1,Z=null,yt=null;const St=new Je(0,0,ft,H),Pt=new Je(0,0,ft,H);let oe=!1;const me=new Yp;let D=!1,X=!1;const dt=new Ze,ht=new Ze,Ct=new Q,Rt=new Je,Ht={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0};let Mt=!1;function bt(){return O===null?at:1}let F=r;function vn(C,k){return i.getContext(C,k)}try{const C={alpha:!0,depth:u,stencil:f,antialias:d,premultipliedAlpha:p,preserveDrawingBuffer:g,powerPreference:v,failIfMajorPerformanceCaveat:_};if("setAttribute"in i&&i.setAttribute("data-engine",`three.js r${Pp}`),i.addEventListener("webglcontextlost",_t,!1),i.addEventListener("webglcontextrestored",Lt,!1),i.addEventListener("webglcontextcreationerror",Ot,!1),F===null){const k="webgl2";if(F=vn(k,C),F===null)throw vn(k)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}}catch(C){throw console.error("THREE.WebGLRenderer: "+C.message),C}let le,ae,Xt,Kt,Zt,N,A,tt,pt,vt,mt,kt,wt,It,ue,xt,Bt,te,$t,Ft,pe,ee,Oe,Y;function Tt(){le=new Q1(F),le.init(),ee=new zR(F,le),ae=new k1(F,le,e,ee),Xt=new LR(F),ae.reverseDepthBuffer&&Xt.buffers.depth.setReversed(!0),Kt=new tA(F),Zt=new vR,N=new PR(F,le,Xt,Zt,ae,ee,Kt),A=new W1(U),tt=new K1(U),pt=new oT(F),Oe=new X1(F,pt),vt=new J1(F,pt,Kt,Oe),mt=new nA(F,vt,pt,Kt),$t=new eA(F,ae,N),xt=new q1(Zt),kt=new gR(U,A,tt,le,ae,Oe,xt),wt=new YR(U,Zt),It=new yR,ue=new AR(le),te=new V1(U,A,tt,Xt,mt,y,p),Bt=new UR(U,mt,ae),Y=new kR(F,Kt,ae,Xt),Ft=new Y1(F,le,Kt),pe=new $1(F,le,Kt),Kt.programs=kt.programs,U.capabilities=ae,U.extensions=le,U.properties=Zt,U.renderLists=It,U.shadowMap=Bt,U.state=Xt,U.info=Kt}Tt();const ot=new VR(U,F);this.xr=ot,this.getContext=function(){return F},this.getContextAttributes=function(){return F.getContextAttributes()},this.forceContextLoss=function(){const C=le.get("WEBGL_lose_context");C&&C.loseContext()},this.forceContextRestore=function(){const C=le.get("WEBGL_lose_context");C&&C.restoreContext()},this.getPixelRatio=function(){return at},this.setPixelRatio=function(C){C!==void 0&&(at=C,this.setSize(ft,H,!1))},this.getSize=function(C){return C.set(ft,H)},this.setSize=function(C,k,it=!0){if(ot.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}ft=C,H=k,i.width=Math.floor(C*at),i.height=Math.floor(k*at),it===!0&&(i.style.width=C+"px",i.style.height=k+"px"),this.setViewport(0,0,C,k)},this.getDrawingBufferSize=function(C){return C.set(ft*at,H*at).floor()},this.setDrawingBufferSize=function(C,k,it){ft=C,H=k,at=it,i.width=Math.floor(C*it),i.height=Math.floor(k*it),this.setViewport(0,0,C,k)},this.getCurrentViewport=function(C){return C.copy(T)},this.getViewport=function(C){return C.copy(St)},this.setViewport=function(C,k,it,st){C.isVector4?St.set(C.x,C.y,C.z,C.w):St.set(C,k,it,st),Xt.viewport(T.copy(St).multiplyScalar(at).round())},this.getScissor=function(C){return C.copy(Pt)},this.setScissor=function(C,k,it,st){C.isVector4?Pt.set(C.x,C.y,C.z,C.w):Pt.set(C,k,it,st),Xt.scissor(w.copy(Pt).multiplyScalar(at).round())},this.getScissorTest=function(){return oe},this.setScissorTest=function(C){Xt.setScissorTest(oe=C)},this.setOpaqueSort=function(C){Z=C},this.setTransparentSort=function(C){yt=C},this.getClearColor=function(C){return C.copy(te.getClearColor())},this.setClearColor=function(){te.setClearColor.apply(te,arguments)},this.getClearAlpha=function(){return te.getClearAlpha()},this.setClearAlpha=function(){te.setClearAlpha.apply(te,arguments)},this.clear=function(C=!0,k=!0,it=!0){let st=0;if(C){let j=!1;if(O!==null){const Et=O.texture.format;j=Et===Gp||Et===Hp||Et===Fp}if(j){const Et=O.texture.type,Nt=Et===Ea||Et===ks||Et===ml||Et===oo||Et===Ip||Et===Bp,Gt=te.getClearColor(),Yt=te.getClearAlpha(),Qt=Gt.r,jt=Gt.g,Ut=Gt.b;Nt?(M[0]=Qt,M[1]=jt,M[2]=Ut,M[3]=Yt,F.clearBufferuiv(F.COLOR,0,M)):(E[0]=Qt,E[1]=jt,E[2]=Ut,E[3]=Yt,F.clearBufferiv(F.COLOR,0,E))}else st|=F.COLOR_BUFFER_BIT}k&&(st|=F.DEPTH_BUFFER_BIT,F.clearDepth(this.capabilities.reverseDepthBuffer?0:1)),it&&(st|=F.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),F.clear(st)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){i.removeEventListener("webglcontextlost",_t,!1),i.removeEventListener("webglcontextrestored",Lt,!1),i.removeEventListener("webglcontextcreationerror",Ot,!1),It.dispose(),ue.dispose(),Zt.dispose(),A.dispose(),tt.dispose(),mt.dispose(),Oe.dispose(),Y.dispose(),kt.dispose(),ot.dispose(),ot.removeEventListener("sessionstart",Mi),ot.removeEventListener("sessionend",Rn),Ki.stop()};function _t(C){C.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),P=!0}function Lt(){console.log("THREE.WebGLRenderer: Context Restored."),P=!1;const C=Kt.autoReset,k=Bt.enabled,it=Bt.autoUpdate,st=Bt.needsUpdate,j=Bt.type;Tt(),Kt.autoReset=C,Bt.enabled=k,Bt.autoUpdate=it,Bt.needsUpdate=st,Bt.type=j}function Ot(C){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",C.statusMessage)}function xe(C){const k=C.target;k.removeEventListener("dispose",xe),ke(k)}function ke(C){An(C),Zt.remove(C)}function An(C){const k=Zt.get(C).programs;k!==void 0&&(k.forEach(function(it){kt.releaseProgram(it)}),C.isShaderMaterial&&kt.releaseShaderCache(C))}this.renderBufferDirect=function(C,k,it,st,j,Et){k===null&&(k=Ht);const Nt=j.isMesh&&j.matrixWorld.determinant()<0,Gt=Ml(C,k,it,st,j);Xt.setMaterial(st,Nt);let Yt=it.index,Qt=1;if(st.wireframe===!0){if(Yt=vt.getWireframeAttribute(it),Yt===void 0)return;Qt=2}const jt=it.drawRange,Ut=it.attributes.position;let ie=jt.start*Qt,be=(jt.start+jt.count)*Qt;Et!==null&&(ie=Math.max(ie,Et.start*Qt),be=Math.min(be,(Et.start+Et.count)*Qt)),Yt!==null?(ie=Math.max(ie,0),be=Math.min(be,Yt.count)):Ut!=null&&(ie=Math.max(ie,0),be=Math.min(be,Ut.count));const Ve=be-ie;if(Ve<0||Ve===1/0)return;Oe.setup(j,st,Gt,it,Yt);let Nn,Ae=Ft;if(Yt!==null&&(Nn=pt.get(Yt),Ae=pe,Ae.setIndex(Nn)),j.isMesh)st.wireframe===!0?(Xt.setLineWidth(st.wireframeLinewidth*bt()),Ae.setMode(F.LINES)):Ae.setMode(F.TRIANGLES);else if(j.isLine){let qt=st.linewidth;qt===void 0&&(qt=1),Xt.setLineWidth(qt*bt()),j.isLineSegments?Ae.setMode(F.LINES):j.isLineLoop?Ae.setMode(F.LINE_LOOP):Ae.setMode(F.LINE_STRIP)}else j.isPoints?Ae.setMode(F.POINTS):j.isSprite&&Ae.setMode(F.TRIANGLES);if(j.isBatchedMesh)if(j._multiDrawInstances!==null)Ae.renderMultiDrawInstances(j._multiDrawStarts,j._multiDrawCounts,j._multiDrawCount,j._multiDrawInstances);else if(le.get("WEBGL_multi_draw"))Ae.renderMultiDraw(j._multiDrawStarts,j._multiDrawCounts,j._multiDrawCount);else{const qt=j._multiDrawStarts,We=j._multiDrawCounts,Me=j._multiDrawCount,Cn=Yt?pt.get(Yt).bytesPerElement:1,Hn=Zt.get(st).currentProgram.getUniforms();for(let en=0;en<Me;en++)Hn.setValue(F,"_gl_DrawID",en),Ae.render(qt[en]/Cn,We[en])}else if(j.isInstancedMesh)Ae.renderInstances(ie,Ve,j.count);else if(it.isInstancedBufferGeometry){const qt=it._maxInstanceCount!==void 0?it._maxInstanceCount:1/0,We=Math.min(it.instanceCount,qt);Ae.renderInstances(ie,Ve,We)}else Ae.render(ie,Ve)};function Te(C,k,it){C.transparent===!0&&C.side===Li&&C.forceSinglePass===!1?(C.side=Zn,C.needsUpdate=!0,li(C,k,it),C.side=ls,C.needsUpdate=!0,li(C,k,it),C.side=Li):li(C,k,it)}this.compile=function(C,k,it=null){it===null&&(it=C),x=ue.get(it),x.init(k),L.push(x),it.traverseVisible(function(j){j.isLight&&j.layers.test(k.layers)&&(x.pushLight(j),j.castShadow&&x.pushShadow(j))}),C!==it&&C.traverseVisible(function(j){j.isLight&&j.layers.test(k.layers)&&(x.pushLight(j),j.castShadow&&x.pushShadow(j))}),x.setupLights();const st=new Set;return C.traverse(function(j){if(!(j.isMesh||j.isPoints||j.isLine||j.isSprite))return;const Et=j.material;if(Et)if(Array.isArray(Et))for(let Nt=0;Nt<Et.length;Nt++){const Gt=Et[Nt];Te(Gt,it,j),st.add(Gt)}else Te(Et,it,j),st.add(Et)}),L.pop(),x=null,st},this.compileAsync=function(C,k,it=null){const st=this.compile(C,k,it);return new Promise(j=>{function Et(){if(st.forEach(function(Nt){Zt.get(Nt).currentProgram.isReady()&&st.delete(Nt)}),st.size===0){j(C);return}setTimeout(Et,10)}le.get("KHR_parallel_shader_compile")!==null?Et():setTimeout(Et,10)})};let tn=null;function qe(C){tn&&tn(C)}function Mi(){Ki.stop()}function Rn(){Ki.start()}const Ki=new HS;Ki.setAnimationLoop(qe),typeof self<"u"&&Ki.setContext(self),this.setAnimationLoop=function(C){tn=C,ot.setAnimationLoop(C),C===null?Ki.stop():Ki.start()},ot.addEventListener("sessionstart",Mi),ot.addEventListener("sessionend",Rn),this.render=function(C,k){if(k!==void 0&&k.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(P===!0)return;if(C.matrixWorldAutoUpdate===!0&&C.updateMatrixWorld(),k.parent===null&&k.matrixWorldAutoUpdate===!0&&k.updateMatrixWorld(),ot.enabled===!0&&ot.isPresenting===!0&&(ot.cameraAutoUpdate===!0&&ot.updateCamera(k),k=ot.getCamera()),C.isScene===!0&&C.onBeforeRender(U,C,k,O),x=ue.get(C,L.length),x.init(k),L.push(x),ht.multiplyMatrices(k.projectionMatrix,k.matrixWorldInverse),me.setFromProjectionMatrix(ht),X=this.localClippingEnabled,D=xt.init(this.clippingPlanes,X),R=It.get(C,S.length),R.init(),S.push(R),ot.enabled===!0&&ot.isPresenting===!0){const Et=U.xr.getDepthSensingMesh();Et!==null&&ho(Et,k,-1/0,U.sortObjects)}ho(C,k,0,U.sortObjects),R.finish(),U.sortObjects===!0&&R.sort(Z,yt),Mt=ot.enabled===!1||ot.isPresenting===!1||ot.hasDepthSensing()===!1,Mt&&te.addToRenderList(R,C),this.info.render.frame++,D===!0&&xt.beginShadows();const it=x.state.shadowsArray;Bt.render(it,C,k),D===!0&&xt.endShadows(),this.info.autoReset===!0&&this.info.reset();const st=R.opaque,j=R.transmissive;if(x.setupLights(),k.isArrayCamera){const Et=k.cameras;if(j.length>0)for(let Nt=0,Gt=Et.length;Nt<Gt;Nt++){const Yt=Et[Nt];fs(st,j,C,Yt)}Mt&&te.render(C);for(let Nt=0,Gt=Et.length;Nt<Gt;Nt++){const Yt=Et[Nt];xl(R,C,Yt,Yt.viewport)}}else j.length>0&&fs(st,j,C,k),Mt&&te.render(C),xl(R,C,k);O!==null&&(N.updateMultisampleRenderTarget(O),N.updateRenderTargetMipmap(O)),C.isScene===!0&&C.onAfterRender(U,C,k),Oe.resetDefaultState(),V=-1,gt=null,L.pop(),L.length>0?(x=L[L.length-1],D===!0&&xt.setGlobalState(U.clippingPlanes,x.state.camera)):x=null,S.pop(),S.length>0?R=S[S.length-1]:R=null};function ho(C,k,it,st){if(C.visible===!1)return;if(C.layers.test(k.layers)){if(C.isGroup)it=C.renderOrder;else if(C.isLOD)C.autoUpdate===!0&&C.update(k);else if(C.isLight)x.pushLight(C),C.castShadow&&x.pushShadow(C);else if(C.isSprite){if(!C.frustumCulled||me.intersectsSprite(C)){st&&Rt.setFromMatrixPosition(C.matrixWorld).applyMatrix4(ht);const Nt=mt.update(C),Gt=C.material;Gt.visible&&R.push(C,Nt,Gt,it,Rt.z,null)}}else if((C.isMesh||C.isLine||C.isPoints)&&(!C.frustumCulled||me.intersectsObject(C))){const Nt=mt.update(C),Gt=C.material;if(st&&(C.boundingSphere!==void 0?(C.boundingSphere===null&&C.computeBoundingSphere(),Rt.copy(C.boundingSphere.center)):(Nt.boundingSphere===null&&Nt.computeBoundingSphere(),Rt.copy(Nt.boundingSphere.center)),Rt.applyMatrix4(C.matrixWorld).applyMatrix4(ht)),Array.isArray(Gt)){const Yt=Nt.groups;for(let Qt=0,jt=Yt.length;Qt<jt;Qt++){const Ut=Yt[Qt],ie=Gt[Ut.materialIndex];ie&&ie.visible&&R.push(C,Nt,ie,it,Rt.z,Ut)}}else Gt.visible&&R.push(C,Nt,Gt,it,Rt.z,null)}}const Et=C.children;for(let Nt=0,Gt=Et.length;Nt<Gt;Nt++)ho(Et[Nt],k,it,st)}function xl(C,k,it,st){const j=C.opaque,Et=C.transmissive,Nt=C.transparent;x.setupLightsView(it),D===!0&&xt.setGlobalState(U.clippingPlanes,it),st&&Xt.viewport(T.copy(st)),j.length>0&&Qi(j,k,it),Et.length>0&&Qi(Et,k,it),Nt.length>0&&Qi(Nt,k,it),Xt.buffers.depth.setTest(!0),Xt.buffers.depth.setMask(!0),Xt.buffers.color.setMask(!0),Xt.setPolygonOffset(!1)}function fs(C,k,it,st){if((it.isScene===!0?it.overrideMaterial:null)!==null)return;x.state.transmissionRenderTarget[st.id]===void 0&&(x.state.transmissionRenderTarget[st.id]=new qs(1,1,{generateMipmaps:!0,type:le.has("EXT_color_buffer_half_float")||le.has("EXT_color_buffer_float")?_l:Ea,minFilter:Ys,samples:4,stencilBuffer:f,resolveDepthBuffer:!1,resolveStencilBuffer:!1,colorSpace:De.workingColorSpace}));const Et=x.state.transmissionRenderTarget[st.id],Nt=st.viewport||T;Et.setSize(Nt.z,Nt.w);const Gt=U.getRenderTarget();U.setRenderTarget(Et),U.getClearColor(rt),lt=U.getClearAlpha(),lt<1&&U.setClearColor(16777215,.5),U.clear(),Mt&&te.render(it);const Yt=U.toneMapping;U.toneMapping=os;const Qt=st.viewport;if(st.viewport!==void 0&&(st.viewport=void 0),x.setupLightsView(st),D===!0&&xt.setGlobalState(U.clippingPlanes,st),Qi(C,it,st),N.updateMultisampleRenderTarget(Et),N.updateRenderTargetMipmap(Et),le.has("WEBGL_multisampled_render_to_texture")===!1){let jt=!1;for(let Ut=0,ie=k.length;Ut<ie;Ut++){const be=k[Ut],Ve=be.object,Nn=be.geometry,Ae=be.material,qt=be.group;if(Ae.side===Li&&Ve.layers.test(st.layers)){const We=Ae.side;Ae.side=Zn,Ae.needsUpdate=!0,hs(Ve,it,st,Nn,Ae,qt),Ae.side=We,Ae.needsUpdate=!0,jt=!0}}jt===!0&&(N.updateMultisampleRenderTarget(Et),N.updateRenderTargetMipmap(Et))}U.setRenderTarget(Gt),U.setClearColor(rt,lt),Qt!==void 0&&(st.viewport=Qt),U.toneMapping=Yt}function Qi(C,k,it){const st=k.isScene===!0?k.overrideMaterial:null;for(let j=0,Et=C.length;j<Et;j++){const Nt=C[j],Gt=Nt.object,Yt=Nt.geometry,Qt=st===null?Nt.material:st,jt=Nt.group;Gt.layers.test(it.layers)&&hs(Gt,k,it,Yt,Qt,jt)}}function hs(C,k,it,st,j,Et){C.onBeforeRender(U,k,it,st,j,Et),C.modelViewMatrix.multiplyMatrices(it.matrixWorldInverse,C.matrixWorld),C.normalMatrix.getNormalMatrix(C.modelViewMatrix),j.onBeforeRender(U,k,it,st,C,Et),j.transparent===!0&&j.side===Li&&j.forceSinglePass===!1?(j.side=Zn,j.needsUpdate=!0,U.renderBufferDirect(it,k,st,j,C,Et),j.side=ls,j.needsUpdate=!0,U.renderBufferDirect(it,k,st,j,C,Et),j.side=Li):U.renderBufferDirect(it,k,st,j,C,Et),C.onAfterRender(U,k,it,st,j,Et)}function li(C,k,it){k.isScene!==!0&&(k=Ht);const st=Zt.get(C),j=x.state.lights,Et=x.state.shadowsArray,Nt=j.state.version,Gt=kt.getParameters(C,j.state,Et,k,it),Yt=kt.getProgramCacheKey(Gt);let Qt=st.programs;st.environment=C.isMeshStandardMaterial?k.environment:null,st.fog=k.fog,st.envMap=(C.isMeshStandardMaterial?tt:A).get(C.envMap||st.environment),st.envMapRotation=st.environment!==null&&C.envMap===null?k.environmentRotation:C.envMapRotation,Qt===void 0&&(C.addEventListener("dispose",xe),Qt=new Map,st.programs=Qt);let jt=Qt.get(Yt);if(jt!==void 0){if(st.currentProgram===jt&&st.lightsStateVersion===Nt)return ba(C,Gt),jt}else Gt.uniforms=kt.getUniforms(C),C.onBeforeCompile(Gt,U),jt=kt.acquireProgram(Gt,Yt),Qt.set(Yt,jt),st.uniforms=Gt.uniforms;const Ut=st.uniforms;return(!C.isShaderMaterial&&!C.isRawShaderMaterial||C.clipping===!0)&&(Ut.clippingPlanes=xt.uniform),ba(C,Gt),st.needsLights=El(C),st.lightsStateVersion=Nt,st.needsLights&&(Ut.ambientLightColor.value=j.state.ambient,Ut.lightProbe.value=j.state.probe,Ut.directionalLights.value=j.state.directional,Ut.directionalLightShadows.value=j.state.directionalShadow,Ut.spotLights.value=j.state.spot,Ut.spotLightShadows.value=j.state.spotShadow,Ut.rectAreaLights.value=j.state.rectArea,Ut.ltc_1.value=j.state.rectAreaLTC1,Ut.ltc_2.value=j.state.rectAreaLTC2,Ut.pointLights.value=j.state.point,Ut.pointLightShadows.value=j.state.pointShadow,Ut.hemisphereLights.value=j.state.hemi,Ut.directionalShadowMap.value=j.state.directionalShadowMap,Ut.directionalShadowMatrix.value=j.state.directionalShadowMatrix,Ut.spotShadowMap.value=j.state.spotShadowMap,Ut.spotLightMatrix.value=j.state.spotLightMatrix,Ut.spotLightMap.value=j.state.spotLightMap,Ut.pointShadowMap.value=j.state.pointShadowMap,Ut.pointShadowMatrix.value=j.state.pointShadowMatrix),st.currentProgram=jt,st.uniformsList=null,jt}function ds(C){if(C.uniformsList===null){const k=C.currentProgram.getUniforms();C.uniformsList=Ec.seqWithValue(k.seq,C.uniforms)}return C.uniformsList}function ba(C,k){const it=Zt.get(C);it.outputColorSpace=k.outputColorSpace,it.batching=k.batching,it.batchingColor=k.batchingColor,it.instancing=k.instancing,it.instancingColor=k.instancingColor,it.instancingMorph=k.instancingMorph,it.skinning=k.skinning,it.morphTargets=k.morphTargets,it.morphNormals=k.morphNormals,it.morphColors=k.morphColors,it.morphTargetsCount=k.morphTargetsCount,it.numClippingPlanes=k.numClippingPlanes,it.numIntersection=k.numClipIntersection,it.vertexAlphas=k.vertexAlphas,it.vertexTangents=k.vertexTangents,it.toneMapping=k.toneMapping}function Ml(C,k,it,st,j){k.isScene!==!0&&(k=Ht),N.resetTextureUnits();const Et=k.fog,Nt=st.isMeshStandardMaterial?k.environment:null,Gt=O===null?U.outputColorSpace:O.isXRRenderTarget===!0?O.texture.colorSpace:cs,Yt=(st.isMeshStandardMaterial?tt:A).get(st.envMap||Nt),Qt=st.vertexColors===!0&&!!it.attributes.color&&it.attributes.color.itemSize===4,jt=!!it.attributes.tangent&&(!!st.normalMap||st.anisotropy>0),Ut=!!it.morphAttributes.position,ie=!!it.morphAttributes.normal,be=!!it.morphAttributes.color;let Ve=os;st.toneMapped&&(O===null||O.isXRRenderTarget===!0)&&(Ve=U.toneMapping);const Nn=it.morphAttributes.position||it.morphAttributes.normal||it.morphAttributes.color,Ae=Nn!==void 0?Nn.length:0,qt=Zt.get(st),We=x.state.lights;if(D===!0&&(X===!0||C!==gt)){const Ln=C===gt&&st.id===V;xt.setState(st,C,Ln)}let Me=!1;st.version===qt.__version?(qt.needsLights&&qt.lightsStateVersion!==We.state.version||qt.outputColorSpace!==Gt||j.isBatchedMesh&&qt.batching===!1||!j.isBatchedMesh&&qt.batching===!0||j.isBatchedMesh&&qt.batchingColor===!0&&j.colorTexture===null||j.isBatchedMesh&&qt.batchingColor===!1&&j.colorTexture!==null||j.isInstancedMesh&&qt.instancing===!1||!j.isInstancedMesh&&qt.instancing===!0||j.isSkinnedMesh&&qt.skinning===!1||!j.isSkinnedMesh&&qt.skinning===!0||j.isInstancedMesh&&qt.instancingColor===!0&&j.instanceColor===null||j.isInstancedMesh&&qt.instancingColor===!1&&j.instanceColor!==null||j.isInstancedMesh&&qt.instancingMorph===!0&&j.morphTexture===null||j.isInstancedMesh&&qt.instancingMorph===!1&&j.morphTexture!==null||qt.envMap!==Yt||st.fog===!0&&qt.fog!==Et||qt.numClippingPlanes!==void 0&&(qt.numClippingPlanes!==xt.numPlanes||qt.numIntersection!==xt.numIntersection)||qt.vertexAlphas!==Qt||qt.vertexTangents!==jt||qt.morphTargets!==Ut||qt.morphNormals!==ie||qt.morphColors!==be||qt.toneMapping!==Ve||qt.morphTargetsCount!==Ae)&&(Me=!0):(Me=!0,qt.__version=st.version);let Cn=qt.currentProgram;Me===!0&&(Cn=li(st,k,j));let Hn=!1,en=!1,Ji=!1;const Pe=Cn.getUniforms(),Be=qt.uniforms;if(Xt.useProgram(Cn.program)&&(Hn=!0,en=!0,Ji=!0),st.id!==V&&(V=st.id,en=!0),Hn||gt!==C){ae.reverseDepthBuffer?(dt.copy(C.projectionMatrix),PE(dt),zE(dt),Pe.setValue(F,"projectionMatrix",dt)):Pe.setValue(F,"projectionMatrix",C.projectionMatrix),Pe.setValue(F,"viewMatrix",C.matrixWorldInverse);const Ln=Pe.map.cameraPosition;Ln!==void 0&&Ln.setValue(F,Ct.setFromMatrixPosition(C.matrixWorld)),ae.logarithmicDepthBuffer&&Pe.setValue(F,"logDepthBufFC",2/(Math.log(C.far+1)/Math.LN2)),(st.isMeshPhongMaterial||st.isMeshToonMaterial||st.isMeshLambertMaterial||st.isMeshBasicMaterial||st.isMeshStandardMaterial||st.isShaderMaterial)&&Pe.setValue(F,"isOrthographic",C.isOrthographicCamera===!0),gt!==C&&(gt=C,en=!0,Ji=!0)}if(j.isSkinnedMesh){Pe.setOptional(F,j,"bindMatrix"),Pe.setOptional(F,j,"bindMatrixInverse");const Ln=j.skeleton;Ln&&(Ln.boneTexture===null&&Ln.computeBoneTexture(),Pe.setValue(F,"boneTexture",Ln.boneTexture,N))}j.isBatchedMesh&&(Pe.setOptional(F,j,"batchingTexture"),Pe.setValue(F,"batchingTexture",j._matricesTexture,N),Pe.setOptional(F,j,"batchingIdTexture"),Pe.setValue(F,"batchingIdTexture",j._indirectTexture,N),Pe.setOptional(F,j,"batchingColorTexture"),j._colorsTexture!==null&&Pe.setValue(F,"batchingColorTexture",j._colorsTexture,N));const Ks=it.morphAttributes;if((Ks.position!==void 0||Ks.normal!==void 0||Ks.color!==void 0)&&$t.update(j,it,Cn),(en||qt.receiveShadow!==j.receiveShadow)&&(qt.receiveShadow=j.receiveShadow,Pe.setValue(F,"receiveShadow",j.receiveShadow)),st.isMeshGouraudMaterial&&st.envMap!==null&&(Be.envMap.value=Yt,Be.flipEnvMap.value=Yt.isCubeTexture&&Yt.isRenderTargetTexture===!1?-1:1),st.isMeshStandardMaterial&&st.envMap===null&&k.environment!==null&&(Be.envMapIntensity.value=k.environmentIntensity),en&&(Pe.setValue(F,"toneMappingExposure",U.toneMappingExposure),qt.needsLights&&zc(Be,Ji),Et&&st.fog===!0&&wt.refreshFogUniforms(Be,Et),wt.refreshMaterialUniforms(Be,st,at,H,x.state.transmissionRenderTarget[C.id]),Ec.upload(F,ds(qt),Be,N)),st.isShaderMaterial&&st.uniformsNeedUpdate===!0&&(Ec.upload(F,ds(qt),Be,N),st.uniformsNeedUpdate=!1),st.isSpriteMaterial&&Pe.setValue(F,"center",j.center),Pe.setValue(F,"modelViewMatrix",j.modelViewMatrix),Pe.setValue(F,"normalMatrix",j.normalMatrix),Pe.setValue(F,"modelMatrix",j.matrixWorld),st.isShaderMaterial||st.isRawShaderMaterial){const Ln=st.uniformsGroups;for(let Qs=0,$i=Ln.length;Qs<$i;Qs++){const ta=Ln[Qs];Y.update(ta,Cn),Y.bind(ta,Cn)}}return Cn}function zc(C,k){C.ambientLightColor.needsUpdate=k,C.lightProbe.needsUpdate=k,C.directionalLights.needsUpdate=k,C.directionalLightShadows.needsUpdate=k,C.pointLights.needsUpdate=k,C.pointLightShadows.needsUpdate=k,C.spotLights.needsUpdate=k,C.spotLightShadows.needsUpdate=k,C.rectAreaLights.needsUpdate=k,C.hemisphereLights.needsUpdate=k}function El(C){return C.isMeshLambertMaterial||C.isMeshToonMaterial||C.isMeshPhongMaterial||C.isMeshStandardMaterial||C.isShadowMaterial||C.isShaderMaterial&&C.lights===!0}this.getActiveCubeFace=function(){return J},this.getActiveMipmapLevel=function(){return B},this.getRenderTarget=function(){return O},this.setRenderTargetTextures=function(C,k,it){Zt.get(C.texture).__webglTexture=k,Zt.get(C.depthTexture).__webglTexture=it;const st=Zt.get(C);st.__hasExternalTextures=!0,st.__autoAllocateDepthBuffer=it===void 0,st.__autoAllocateDepthBuffer||le.has("WEBGL_multisampled_render_to_texture")===!0&&(console.warn("THREE.WebGLRenderer: Render-to-texture extension was disabled because an external texture was provided"),st.__useRenderToTexture=!1)},this.setRenderTargetFramebuffer=function(C,k){const it=Zt.get(C);it.__webglFramebuffer=k,it.__useDefaultFramebuffer=k===void 0},this.setRenderTarget=function(C,k=0,it=0){O=C,J=k,B=it;let st=!0,j=null,Et=!1,Nt=!1;if(C){const Yt=Zt.get(C);if(Yt.__useDefaultFramebuffer!==void 0)Xt.bindFramebuffer(F.FRAMEBUFFER,null),st=!1;else if(Yt.__webglFramebuffer===void 0)N.setupRenderTarget(C);else if(Yt.__hasExternalTextures)N.rebindTextures(C,Zt.get(C.texture).__webglTexture,Zt.get(C.depthTexture).__webglTexture);else if(C.depthBuffer){const Ut=C.depthTexture;if(Yt.__boundDepthTexture!==Ut){if(Ut!==null&&Zt.has(Ut)&&(C.width!==Ut.image.width||C.height!==Ut.image.height))throw new Error("WebGLRenderTarget: Attached DepthTexture is initialized to the incorrect size.");N.setupDepthRenderbuffer(C)}}const Qt=C.texture;(Qt.isData3DTexture||Qt.isDataArrayTexture||Qt.isCompressedArrayTexture)&&(Nt=!0);const jt=Zt.get(C).__webglFramebuffer;C.isWebGLCubeRenderTarget?(Array.isArray(jt[k])?j=jt[k][it]:j=jt[k],Et=!0):C.samples>0&&N.useMultisampledRTT(C)===!1?j=Zt.get(C).__webglMultisampledFramebuffer:Array.isArray(jt)?j=jt[it]:j=jt,T.copy(C.viewport),w.copy(C.scissor),nt=C.scissorTest}else T.copy(St).multiplyScalar(at).floor(),w.copy(Pt).multiplyScalar(at).floor(),nt=oe;if(Xt.bindFramebuffer(F.FRAMEBUFFER,j)&&st&&Xt.drawBuffers(C,j),Xt.viewport(T),Xt.scissor(w),Xt.setScissorTest(nt),Et){const Yt=Zt.get(C.texture);F.framebufferTexture2D(F.FRAMEBUFFER,F.COLOR_ATTACHMENT0,F.TEXTURE_CUBE_MAP_POSITIVE_X+k,Yt.__webglTexture,it)}else if(Nt){const Yt=Zt.get(C.texture),Qt=k||0;F.framebufferTextureLayer(F.FRAMEBUFFER,F.COLOR_ATTACHMENT0,Yt.__webglTexture,it||0,Qt)}V=-1},this.readRenderTargetPixels=function(C,k,it,st,j,Et,Nt){if(!(C&&C.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let Gt=Zt.get(C).__webglFramebuffer;if(C.isWebGLCubeRenderTarget&&Nt!==void 0&&(Gt=Gt[Nt]),Gt){Xt.bindFramebuffer(F.FRAMEBUFFER,Gt);try{const Yt=C.texture,Qt=Yt.format,jt=Yt.type;if(!ae.textureFormatReadable(Qt)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(!ae.textureTypeReadable(jt)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}k>=0&&k<=C.width-st&&it>=0&&it<=C.height-j&&F.readPixels(k,it,st,j,ee.convert(Qt),ee.convert(jt),Et)}finally{const Yt=O!==null?Zt.get(O).__webglFramebuffer:null;Xt.bindFramebuffer(F.FRAMEBUFFER,Yt)}}},this.readRenderTargetPixelsAsync=async function(C,k,it,st,j,Et,Nt){if(!(C&&C.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let Gt=Zt.get(C).__webglFramebuffer;if(C.isWebGLCubeRenderTarget&&Nt!==void 0&&(Gt=Gt[Nt]),Gt){const Yt=C.texture,Qt=Yt.format,jt=Yt.type;if(!ae.textureFormatReadable(Qt))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(!ae.textureTypeReadable(jt))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");if(k>=0&&k<=C.width-st&&it>=0&&it<=C.height-j){Xt.bindFramebuffer(F.FRAMEBUFFER,Gt);const Ut=F.createBuffer();F.bindBuffer(F.PIXEL_PACK_BUFFER,Ut),F.bufferData(F.PIXEL_PACK_BUFFER,Et.byteLength,F.STREAM_READ),F.readPixels(k,it,st,j,ee.convert(Qt),ee.convert(jt),0);const ie=O!==null?Zt.get(O).__webglFramebuffer:null;Xt.bindFramebuffer(F.FRAMEBUFFER,ie);const be=F.fenceSync(F.SYNC_GPU_COMMANDS_COMPLETE,0);return F.flush(),await OE(F,be,4),F.bindBuffer(F.PIXEL_PACK_BUFFER,Ut),F.getBufferSubData(F.PIXEL_PACK_BUFFER,0,Et),F.deleteBuffer(Ut),F.deleteSync(be),Et}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")}},this.copyFramebufferToTexture=function(C,k=null,it=0){C.isTexture!==!0&&(Mc("WebGLRenderer: copyFramebufferToTexture function signature has changed."),k=arguments[0]||null,C=arguments[1]);const st=Math.pow(2,-it),j=Math.floor(C.image.width*st),Et=Math.floor(C.image.height*st),Nt=k!==null?k.x:0,Gt=k!==null?k.y:0;N.setTexture2D(C,0),F.copyTexSubImage2D(F.TEXTURE_2D,it,0,0,Nt,Gt,j,Et),Xt.unbindTexture()},this.copyTextureToTexture=function(C,k,it=null,st=null,j=0){C.isTexture!==!0&&(Mc("WebGLRenderer: copyTextureToTexture function signature has changed."),st=arguments[0]||null,C=arguments[1],k=arguments[2],j=arguments[3]||0,it=null);let Et,Nt,Gt,Yt,Qt,jt;it!==null?(Et=it.max.x-it.min.x,Nt=it.max.y-it.min.y,Gt=it.min.x,Yt=it.min.y):(Et=C.image.width,Nt=C.image.height,Gt=0,Yt=0),st!==null?(Qt=st.x,jt=st.y):(Qt=0,jt=0);const Ut=ee.convert(k.format),ie=ee.convert(k.type);N.setTexture2D(k,0),F.pixelStorei(F.UNPACK_FLIP_Y_WEBGL,k.flipY),F.pixelStorei(F.UNPACK_PREMULTIPLY_ALPHA_WEBGL,k.premultiplyAlpha),F.pixelStorei(F.UNPACK_ALIGNMENT,k.unpackAlignment);const be=F.getParameter(F.UNPACK_ROW_LENGTH),Ve=F.getParameter(F.UNPACK_IMAGE_HEIGHT),Nn=F.getParameter(F.UNPACK_SKIP_PIXELS),Ae=F.getParameter(F.UNPACK_SKIP_ROWS),qt=F.getParameter(F.UNPACK_SKIP_IMAGES),We=C.isCompressedTexture?C.mipmaps[j]:C.image;F.pixelStorei(F.UNPACK_ROW_LENGTH,We.width),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,We.height),F.pixelStorei(F.UNPACK_SKIP_PIXELS,Gt),F.pixelStorei(F.UNPACK_SKIP_ROWS,Yt),C.isDataTexture?F.texSubImage2D(F.TEXTURE_2D,j,Qt,jt,Et,Nt,Ut,ie,We.data):C.isCompressedTexture?F.compressedTexSubImage2D(F.TEXTURE_2D,j,Qt,jt,We.width,We.height,Ut,We.data):F.texSubImage2D(F.TEXTURE_2D,j,Qt,jt,Et,Nt,Ut,ie,We),F.pixelStorei(F.UNPACK_ROW_LENGTH,be),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,Ve),F.pixelStorei(F.UNPACK_SKIP_PIXELS,Nn),F.pixelStorei(F.UNPACK_SKIP_ROWS,Ae),F.pixelStorei(F.UNPACK_SKIP_IMAGES,qt),j===0&&k.generateMipmaps&&F.generateMipmap(F.TEXTURE_2D),Xt.unbindTexture()},this.copyTextureToTexture3D=function(C,k,it=null,st=null,j=0){C.isTexture!==!0&&(Mc("WebGLRenderer: copyTextureToTexture3D function signature has changed."),it=arguments[0]||null,st=arguments[1]||null,C=arguments[2],k=arguments[3],j=arguments[4]||0);let Et,Nt,Gt,Yt,Qt,jt,Ut,ie,be;const Ve=C.isCompressedTexture?C.mipmaps[j]:C.image;it!==null?(Et=it.max.x-it.min.x,Nt=it.max.y-it.min.y,Gt=it.max.z-it.min.z,Yt=it.min.x,Qt=it.min.y,jt=it.min.z):(Et=Ve.width,Nt=Ve.height,Gt=Ve.depth,Yt=0,Qt=0,jt=0),st!==null?(Ut=st.x,ie=st.y,be=st.z):(Ut=0,ie=0,be=0);const Nn=ee.convert(k.format),Ae=ee.convert(k.type);let qt;if(k.isData3DTexture)N.setTexture3D(k,0),qt=F.TEXTURE_3D;else if(k.isDataArrayTexture||k.isCompressedArrayTexture)N.setTexture2DArray(k,0),qt=F.TEXTURE_2D_ARRAY;else{console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: only supports THREE.DataTexture3D and THREE.DataTexture2DArray.");return}F.pixelStorei(F.UNPACK_FLIP_Y_WEBGL,k.flipY),F.pixelStorei(F.UNPACK_PREMULTIPLY_ALPHA_WEBGL,k.premultiplyAlpha),F.pixelStorei(F.UNPACK_ALIGNMENT,k.unpackAlignment);const We=F.getParameter(F.UNPACK_ROW_LENGTH),Me=F.getParameter(F.UNPACK_IMAGE_HEIGHT),Cn=F.getParameter(F.UNPACK_SKIP_PIXELS),Hn=F.getParameter(F.UNPACK_SKIP_ROWS),en=F.getParameter(F.UNPACK_SKIP_IMAGES);F.pixelStorei(F.UNPACK_ROW_LENGTH,Ve.width),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,Ve.height),F.pixelStorei(F.UNPACK_SKIP_PIXELS,Yt),F.pixelStorei(F.UNPACK_SKIP_ROWS,Qt),F.pixelStorei(F.UNPACK_SKIP_IMAGES,jt),C.isDataTexture||C.isData3DTexture?F.texSubImage3D(qt,j,Ut,ie,be,Et,Nt,Gt,Nn,Ae,Ve.data):k.isCompressedArrayTexture?F.compressedTexSubImage3D(qt,j,Ut,ie,be,Et,Nt,Gt,Nn,Ve.data):F.texSubImage3D(qt,j,Ut,ie,be,Et,Nt,Gt,Nn,Ae,Ve),F.pixelStorei(F.UNPACK_ROW_LENGTH,We),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,Me),F.pixelStorei(F.UNPACK_SKIP_PIXELS,Cn),F.pixelStorei(F.UNPACK_SKIP_ROWS,Hn),F.pixelStorei(F.UNPACK_SKIP_IMAGES,en),j===0&&k.generateMipmaps&&F.generateMipmap(qt),Xt.unbindTexture()},this.initRenderTarget=function(C){Zt.get(C).__webglFramebuffer===void 0&&N.setupRenderTarget(C)},this.initTexture=function(C){C.isCubeTexture?N.setTextureCube(C,0):C.isData3DTexture?N.setTexture3D(C,0):C.isDataArrayTexture||C.isCompressedArrayTexture?N.setTexture2DArray(C,0):N.setTexture2D(C,0),Xt.unbindTexture()},this.resetState=function(){J=0,B=0,O=null,Xt.reset(),Oe.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Ma}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(e){this._outputColorSpace=e;const i=this.getContext();i.drawingBufferColorSpace=e===Vp?"display-p3":"srgb",i.unpackColorSpace=De.workingColorSpace===Nc?"display-p3":"srgb"}}class WR extends bn{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new Ta,this.environmentIntensity=1,this.environmentRotation=new Ta,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(e,i){return super.copy(e,i),e.background!==null&&(this.background=e.background.clone()),e.environment!==null&&(this.environment=e.environment.clone()),e.fog!==null&&(this.fog=e.fog.clone()),this.backgroundBlurriness=e.backgroundBlurriness,this.backgroundIntensity=e.backgroundIntensity,this.backgroundRotation.copy(e.backgroundRotation),this.environmentIntensity=e.environmentIntensity,this.environmentRotation.copy(e.environmentRotation),e.overrideMaterial!==null&&(this.overrideMaterial=e.overrideMaterial.clone()),this.matrixAutoUpdate=e.matrixAutoUpdate,this}toJSON(e){const i=super.toJSON(e);return this.fog!==null&&(i.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(i.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(i.object.backgroundIntensity=this.backgroundIntensity),i.object.backgroundRotation=this.backgroundRotation.toArray(),this.environmentIntensity!==1&&(i.object.environmentIntensity=this.environmentIntensity),i.object.environmentRotation=this.environmentRotation.toArray(),i}}class Pc extends Sl{constructor(e){super(),this.isLineBasicMaterial=!0,this.type="LineBasicMaterial",this.color=new ye(16777215),this.map=null,this.linewidth=1,this.linecap="round",this.linejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.linewidth=e.linewidth,this.linecap=e.linecap,this.linejoin=e.linejoin,this.fog=e.fog,this}}const wc=new Q,Dc=new Q,oS=new Ze,cl=new Xp,fc=new Lc,Yd=new Q,lS=new Q;class WS extends bn{constructor(e=new Qn,i=new Pc){super(),this.isLine=!0,this.type="Line",this.geometry=e,this.material=i,this.updateMorphTargets()}copy(e,i){return super.copy(e,i),this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}computeLineDistances(){const e=this.geometry;if(e.index===null){const i=e.attributes.position,r=[0];for(let u=1,f=i.count;u<f;u++)wc.fromBufferAttribute(i,u-1),Dc.fromBufferAttribute(i,u),r[u]=r[u-1],r[u]+=wc.distanceTo(Dc);e.setAttribute("lineDistance",new gn(r,1))}else console.warn("THREE.Line.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}raycast(e,i){const r=this.geometry,u=this.matrixWorld,f=e.params.Line.threshold,h=r.drawRange;if(r.boundingSphere===null&&r.computeBoundingSphere(),fc.copy(r.boundingSphere),fc.applyMatrix4(u),fc.radius+=f,e.ray.intersectsSphere(fc)===!1)return;oS.copy(u).invert(),cl.copy(e.ray).applyMatrix4(oS);const d=f/((this.scale.x+this.scale.y+this.scale.z)/3),p=d*d,g=this.isLineSegments?2:1,v=r.index,y=r.attributes.position;if(v!==null){const M=Math.max(0,h.start),E=Math.min(v.count,h.start+h.count);for(let R=M,x=E-1;R<x;R+=g){const S=v.getX(R),L=v.getX(R+1),U=hc(this,e,cl,p,S,L);U&&i.push(U)}if(this.isLineLoop){const R=v.getX(E-1),x=v.getX(M),S=hc(this,e,cl,p,R,x);S&&i.push(S)}}else{const M=Math.max(0,h.start),E=Math.min(y.count,h.start+h.count);for(let R=M,x=E-1;R<x;R+=g){const S=hc(this,e,cl,p,R,R+1);S&&i.push(S)}if(this.isLineLoop){const R=hc(this,e,cl,p,E-1,M);R&&i.push(R)}}}updateMorphTargets(){const i=this.geometry.morphAttributes,r=Object.keys(i);if(r.length>0){const u=i[r[0]];if(u!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let f=0,h=u.length;f<h;f++){const d=u[f].name||String(f);this.morphTargetInfluences.push(0),this.morphTargetDictionary[d]=f}}}}}function hc(o,e,i,r,u,f){const h=o.geometry.attributes.position;if(wc.fromBufferAttribute(h,u),Dc.fromBufferAttribute(h,f),i.distanceSqToSegment(wc,Dc,Yd,lS)>r)return;Yd.applyMatrix4(o.matrixWorld);const p=e.ray.origin.distanceTo(Yd);if(!(p<e.near||p>e.far))return{distance:p,point:lS.clone().applyMatrix4(o.matrixWorld),index:u,face:null,faceIndex:null,barycoord:null,object:o}}const uS=new Q,cS=new Q;class jS extends WS{constructor(e,i){super(e,i),this.isLineSegments=!0,this.type="LineSegments"}computeLineDistances(){const e=this.geometry;if(e.index===null){const i=e.attributes.position,r=[];for(let u=0,f=i.count;u<f;u+=2)uS.fromBufferAttribute(i,u),cS.fromBufferAttribute(i,u+1),r[u]=u===0?0:r[u-1],r[u+1]=r[u]+uS.distanceTo(cS);e.setAttribute("lineDistance",new gn(r,1))}else console.warn("THREE.LineSegments.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}}class qp extends Qn{constructor(e=1,i=1,r=1,u=32,f=1,h=!1,d=0,p=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:e,radiusBottom:i,height:r,radialSegments:u,heightSegments:f,openEnded:h,thetaStart:d,thetaLength:p};const g=this;u=Math.floor(u),f=Math.floor(f);const v=[],_=[],y=[],M=[];let E=0;const R=[],x=r/2;let S=0;L(),h===!1&&(e>0&&U(!0),i>0&&U(!1)),this.setIndex(v),this.setAttribute("position",new gn(_,3)),this.setAttribute("normal",new gn(y,3)),this.setAttribute("uv",new gn(M,2));function L(){const P=new Q,J=new Q;let B=0;const O=(i-e)/r;for(let V=0;V<=f;V++){const gt=[],T=V/f,w=T*(i-e)+e;for(let nt=0;nt<=u;nt++){const rt=nt/u,lt=rt*p+d,ft=Math.sin(lt),H=Math.cos(lt);J.x=w*ft,J.y=-T*r+x,J.z=w*H,_.push(J.x,J.y,J.z),P.set(ft,O,H).normalize(),y.push(P.x,P.y,P.z),M.push(rt,1-T),gt.push(E++)}R.push(gt)}for(let V=0;V<u;V++)for(let gt=0;gt<f;gt++){const T=R[gt][V],w=R[gt+1][V],nt=R[gt+1][V+1],rt=R[gt][V+1];e>0&&(v.push(T,w,rt),B+=3),i>0&&(v.push(w,nt,rt),B+=3)}g.addGroup(S,B,0),S+=B}function U(P){const J=E,B=new ce,O=new Q;let V=0;const gt=P===!0?e:i,T=P===!0?1:-1;for(let nt=1;nt<=u;nt++)_.push(0,x*T,0),y.push(0,T,0),M.push(.5,.5),E++;const w=E;for(let nt=0;nt<=u;nt++){const lt=nt/u*p+d,ft=Math.cos(lt),H=Math.sin(lt);O.x=gt*H,O.y=x*T,O.z=gt*ft,_.push(O.x,O.y,O.z),y.push(0,T,0),B.x=ft*.5+.5,B.y=H*.5*T+.5,M.push(B.x,B.y),E++}for(let nt=0;nt<u;nt++){const rt=J+nt,lt=w+nt;P===!0?v.push(lt,lt+1,rt):v.push(lt+1,lt,rt),V+=3}g.addGroup(S,V,P===!0?1:2),S+=V}}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new qp(e.radiusTop,e.radiusBottom,e.height,e.radialSegments,e.heightSegments,e.openEnded,e.thetaStart,e.thetaLength)}}class Wp extends qp{constructor(e=1,i=1,r=32,u=1,f=!1,h=0,d=Math.PI*2){super(0,e,i,r,u,f,h,d),this.type="ConeGeometry",this.parameters={radius:e,height:i,radialSegments:r,heightSegments:u,openEnded:f,thetaStart:h,thetaLength:d}}static fromJSON(e){return new Wp(e.radius,e.height,e.radialSegments,e.heightSegments,e.openEnded,e.thetaStart,e.thetaLength)}}class jp extends Qn{constructor(e=1,i=32,r=16,u=0,f=Math.PI*2,h=0,d=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:e,widthSegments:i,heightSegments:r,phiStart:u,phiLength:f,thetaStart:h,thetaLength:d},i=Math.max(3,Math.floor(i)),r=Math.max(2,Math.floor(r));const p=Math.min(h+d,Math.PI);let g=0;const v=[],_=new Q,y=new Q,M=[],E=[],R=[],x=[];for(let S=0;S<=r;S++){const L=[],U=S/r;let P=0;S===0&&h===0?P=.5/i:S===r&&p===Math.PI&&(P=-.5/i);for(let J=0;J<=i;J++){const B=J/i;_.x=-e*Math.cos(u+B*f)*Math.sin(h+U*d),_.y=e*Math.cos(h+U*d),_.z=e*Math.sin(u+B*f)*Math.sin(h+U*d),E.push(_.x,_.y,_.z),y.copy(_).normalize(),R.push(y.x,y.y,y.z),x.push(B+P,1-U),L.push(g++)}v.push(L)}for(let S=0;S<r;S++)for(let L=0;L<i;L++){const U=v[S][L+1],P=v[S][L],J=v[S+1][L],B=v[S+1][L+1];(S!==0||h>0)&&M.push(U,P,B),(S!==r-1||p<Math.PI)&&M.push(P,J,B)}this.setIndex(M),this.setAttribute("position",new gn(E,3)),this.setAttribute("normal",new gn(R,3)),this.setAttribute("uv",new gn(x,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new jp(e.radius,e.widthSegments,e.heightSegments,e.phiStart,e.phiLength,e.thetaStart,e.thetaLength)}}class ZS extends bn{constructor(e,i=1){super(),this.isLight=!0,this.type="Light",this.color=new ye(e),this.intensity=i}dispose(){}copy(e,i){return super.copy(e,i),this.color.copy(e.color),this.intensity=e.intensity,this}toJSON(e){const i=super.toJSON(e);return i.object.color=this.color.getHex(),i.object.intensity=this.intensity,this.groundColor!==void 0&&(i.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(i.object.distance=this.distance),this.angle!==void 0&&(i.object.angle=this.angle),this.decay!==void 0&&(i.object.decay=this.decay),this.penumbra!==void 0&&(i.object.penumbra=this.penumbra),this.shadow!==void 0&&(i.object.shadow=this.shadow.toJSON()),this.target!==void 0&&(i.object.target=this.target.uuid),i}}const kd=new Ze,fS=new Q,hS=new Q;class jR{constructor(e){this.camera=e,this.intensity=1,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new ce(512,512),this.map=null,this.mapPass=null,this.matrix=new Ze,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new Yp,this._frameExtents=new ce(1,1),this._viewportCount=1,this._viewports=[new Je(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(e){const i=this.camera,r=this.matrix;fS.setFromMatrixPosition(e.matrixWorld),i.position.copy(fS),hS.setFromMatrixPosition(e.target.matrixWorld),i.lookAt(hS),i.updateMatrixWorld(),kd.multiplyMatrices(i.projectionMatrix,i.matrixWorldInverse),this._frustum.setFromProjectionMatrix(kd),r.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),r.multiply(kd)}getViewport(e){return this._viewports[e]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(e){return this.camera=e.camera.clone(),this.intensity=e.intensity,this.bias=e.bias,this.radius=e.radius,this.mapSize.copy(e.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){const e={};return this.intensity!==1&&(e.intensity=this.intensity),this.bias!==0&&(e.bias=this.bias),this.normalBias!==0&&(e.normalBias=this.normalBias),this.radius!==1&&(e.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(e.mapSize=this.mapSize.toArray()),e.camera=this.camera.toJSON(!1).object,delete e.camera.matrix,e}}class ZR extends jR{constructor(){super(new GS(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}}class KR extends ZS{constructor(e,i){super(e,i),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(bn.DEFAULT_UP),this.updateMatrix(),this.target=new bn,this.shadow=new ZR}dispose(){this.shadow.dispose()}copy(e){return super.copy(e),this.target=e.target.clone(),this.shadow=e.shadow.clone(),this}}class QR extends ZS{constructor(e,i){super(e,i),this.isAmbientLight=!0,this.type="AmbientLight"}}class dS{constructor(e=1,i=0,r=0){return this.radius=e,this.phi=i,this.theta=r,this}set(e,i,r){return this.radius=e,this.phi=i,this.theta=r,this}copy(e){return this.radius=e.radius,this.phi=e.phi,this.theta=e.theta,this}makeSafe(){return this.phi=Math.max(1e-6,Math.min(Math.PI-1e-6,this.phi)),this}setFromVector3(e){return this.setFromCartesianCoords(e.x,e.y,e.z)}setFromCartesianCoords(e,i,r){return this.radius=Math.sqrt(e*e+i*i+r*r),this.radius===0?(this.theta=0,this.phi=0):(this.theta=Math.atan2(e,r),this.phi=Math.acos(Fn(i/this.radius,-1,1))),this}clone(){return new this.constructor().copy(this)}}class JR extends jS{constructor(e=10,i=10,r=4473924,u=8947848){r=new ye(r),u=new ye(u);const f=i/2,h=e/i,d=e/2,p=[],g=[];for(let y=0,M=0,E=-d;y<=i;y++,E+=h){p.push(-d,0,E,d,0,E),p.push(E,0,-d,E,0,d);const R=y===f?r:u;R.toArray(g,M),M+=3,R.toArray(g,M),M+=3,R.toArray(g,M),M+=3,R.toArray(g,M),M+=3}const v=new Qn;v.setAttribute("position",new gn(p,3)),v.setAttribute("color",new gn(g,3));const _=new Pc({vertexColors:!0,toneMapped:!1});super(v,_),this.type="GridHelper"}dispose(){this.geometry.dispose(),this.material.dispose()}}class $R extends Zs{constructor(e,i=null){super(),this.object=e,this.domElement=i,this.enabled=!0,this.state=-1,this.keys={},this.mouseButtons={LEFT:null,MIDDLE:null,RIGHT:null},this.touches={ONE:null,TWO:null}}connect(){}disconnect(){}dispose(){}update(){}}typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:Pp}}));typeof window<"u"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__=Pp);const pS={type:"change"},Zp={type:"start"},KS={type:"end"},dc=new Xp,mS=new as,tC=Math.cos(70*NE.DEG2RAD),un=new Q,Wn=2*Math.PI,Ie={NONE:-1,ROTATE:0,DOLLY:1,PAN:2,TOUCH_ROTATE:3,TOUCH_PAN:4,TOUCH_DOLLY_PAN:5,TOUCH_DOLLY_ROTATE:6},qd=1e-6;class eC extends $R{constructor(e,i=null){super(e,i),this.state=Ie.NONE,this.enabled=!0,this.target=new Q,this.cursor=new Q,this.minDistance=0,this.maxDistance=1/0,this.minZoom=0,this.maxZoom=1/0,this.minTargetRadius=0,this.maxTargetRadius=1/0,this.minPolarAngle=0,this.maxPolarAngle=Math.PI,this.minAzimuthAngle=-1/0,this.maxAzimuthAngle=1/0,this.enableDamping=!1,this.dampingFactor=.05,this.enableZoom=!0,this.zoomSpeed=1,this.enableRotate=!0,this.rotateSpeed=1,this.enablePan=!0,this.panSpeed=1,this.screenSpacePanning=!0,this.keyPanSpeed=7,this.zoomToCursor=!1,this.autoRotate=!1,this.autoRotateSpeed=2,this.keys={LEFT:"ArrowLeft",UP:"ArrowUp",RIGHT:"ArrowRight",BOTTOM:"ArrowDown"},this.mouseButtons={LEFT:to.ROTATE,MIDDLE:to.DOLLY,RIGHT:to.PAN},this.touches={ONE:Jr.ROTATE,TWO:Jr.DOLLY_PAN},this.target0=this.target.clone(),this.position0=this.object.position.clone(),this.zoom0=this.object.zoom,this._domElementKeyEvents=null,this._lastPosition=new Q,this._lastQuaternion=new Ws,this._lastTargetPosition=new Q,this._quat=new Ws().setFromUnitVectors(e.up,new Q(0,1,0)),this._quatInverse=this._quat.clone().invert(),this._spherical=new dS,this._sphericalDelta=new dS,this._scale=1,this._panOffset=new Q,this._rotateStart=new ce,this._rotateEnd=new ce,this._rotateDelta=new ce,this._panStart=new ce,this._panEnd=new ce,this._panDelta=new ce,this._dollyStart=new ce,this._dollyEnd=new ce,this._dollyDelta=new ce,this._dollyDirection=new Q,this._mouse=new ce,this._performCursorZoom=!1,this._pointers=[],this._pointerPositions={},this._controlActive=!1,this._onPointerMove=iC.bind(this),this._onPointerDown=nC.bind(this),this._onPointerUp=aC.bind(this),this._onContextMenu=fC.bind(this),this._onMouseWheel=oC.bind(this),this._onKeyDown=lC.bind(this),this._onTouchStart=uC.bind(this),this._onTouchMove=cC.bind(this),this._onMouseDown=sC.bind(this),this._onMouseMove=rC.bind(this),this._interceptControlDown=hC.bind(this),this._interceptControlUp=dC.bind(this),this.domElement!==null&&this.connect(),this.update()}connect(){this.domElement.addEventListener("pointerdown",this._onPointerDown),this.domElement.addEventListener("pointercancel",this._onPointerUp),this.domElement.addEventListener("contextmenu",this._onContextMenu),this.domElement.addEventListener("wheel",this._onMouseWheel,{passive:!1}),this.domElement.getRootNode().addEventListener("keydown",this._interceptControlDown,{passive:!0,capture:!0}),this.domElement.style.touchAction="none"}disconnect(){this.domElement.removeEventListener("pointerdown",this._onPointerDown),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.domElement.removeEventListener("pointercancel",this._onPointerUp),this.domElement.removeEventListener("wheel",this._onMouseWheel),this.domElement.removeEventListener("contextmenu",this._onContextMenu),this.stopListenToKeyEvents(),this.domElement.getRootNode().removeEventListener("keydown",this._interceptControlDown,{capture:!0}),this.domElement.style.touchAction="auto"}dispose(){this.disconnect()}getPolarAngle(){return this._spherical.phi}getAzimuthalAngle(){return this._spherical.theta}getDistance(){return this.object.position.distanceTo(this.target)}listenToKeyEvents(e){e.addEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=e}stopListenToKeyEvents(){this._domElementKeyEvents!==null&&(this._domElementKeyEvents.removeEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=null)}saveState(){this.target0.copy(this.target),this.position0.copy(this.object.position),this.zoom0=this.object.zoom}reset(){this.target.copy(this.target0),this.object.position.copy(this.position0),this.object.zoom=this.zoom0,this.object.updateProjectionMatrix(),this.dispatchEvent(pS),this.update(),this.state=Ie.NONE}update(e=null){const i=this.object.position;un.copy(i).sub(this.target),un.applyQuaternion(this._quat),this._spherical.setFromVector3(un),this.autoRotate&&this.state===Ie.NONE&&this._rotateLeft(this._getAutoRotationAngle(e)),this.enableDamping?(this._spherical.theta+=this._sphericalDelta.theta*this.dampingFactor,this._spherical.phi+=this._sphericalDelta.phi*this.dampingFactor):(this._spherical.theta+=this._sphericalDelta.theta,this._spherical.phi+=this._sphericalDelta.phi);let r=this.minAzimuthAngle,u=this.maxAzimuthAngle;isFinite(r)&&isFinite(u)&&(r<-Math.PI?r+=Wn:r>Math.PI&&(r-=Wn),u<-Math.PI?u+=Wn:u>Math.PI&&(u-=Wn),r<=u?this._spherical.theta=Math.max(r,Math.min(u,this._spherical.theta)):this._spherical.theta=this._spherical.theta>(r+u)/2?Math.max(r,this._spherical.theta):Math.min(u,this._spherical.theta)),this._spherical.phi=Math.max(this.minPolarAngle,Math.min(this.maxPolarAngle,this._spherical.phi)),this._spherical.makeSafe(),this.enableDamping===!0?this.target.addScaledVector(this._panOffset,this.dampingFactor):this.target.add(this._panOffset),this.target.sub(this.cursor),this.target.clampLength(this.minTargetRadius,this.maxTargetRadius),this.target.add(this.cursor);let f=!1;if(this.zoomToCursor&&this._performCursorZoom||this.object.isOrthographicCamera)this._spherical.radius=this._clampDistance(this._spherical.radius);else{const h=this._spherical.radius;this._spherical.radius=this._clampDistance(this._spherical.radius*this._scale),f=h!=this._spherical.radius}if(un.setFromSpherical(this._spherical),un.applyQuaternion(this._quatInverse),i.copy(this.target).add(un),this.object.lookAt(this.target),this.enableDamping===!0?(this._sphericalDelta.theta*=1-this.dampingFactor,this._sphericalDelta.phi*=1-this.dampingFactor,this._panOffset.multiplyScalar(1-this.dampingFactor)):(this._sphericalDelta.set(0,0,0),this._panOffset.set(0,0,0)),this.zoomToCursor&&this._performCursorZoom){let h=null;if(this.object.isPerspectiveCamera){const d=un.length();h=this._clampDistance(d*this._scale);const p=d-h;this.object.position.addScaledVector(this._dollyDirection,p),this.object.updateMatrixWorld(),f=!!p}else if(this.object.isOrthographicCamera){const d=new Q(this._mouse.x,this._mouse.y,0);d.unproject(this.object);const p=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),this.object.updateProjectionMatrix(),f=p!==this.object.zoom;const g=new Q(this._mouse.x,this._mouse.y,0);g.unproject(this.object),this.object.position.sub(g).add(d),this.object.updateMatrixWorld(),h=un.length()}else console.warn("WARNING: OrbitControls.js encountered an unknown camera type - zoom to cursor disabled."),this.zoomToCursor=!1;h!==null&&(this.screenSpacePanning?this.target.set(0,0,-1).transformDirection(this.object.matrix).multiplyScalar(h).add(this.object.position):(dc.origin.copy(this.object.position),dc.direction.set(0,0,-1).transformDirection(this.object.matrix),Math.abs(this.object.up.dot(dc.direction))<tC?this.object.lookAt(this.target):(mS.setFromNormalAndCoplanarPoint(this.object.up,this.target),dc.intersectPlane(mS,this.target))))}else if(this.object.isOrthographicCamera){const h=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),h!==this.object.zoom&&(this.object.updateProjectionMatrix(),f=!0)}return this._scale=1,this._performCursorZoom=!1,f||this._lastPosition.distanceToSquared(this.object.position)>qd||8*(1-this._lastQuaternion.dot(this.object.quaternion))>qd||this._lastTargetPosition.distanceToSquared(this.target)>qd?(this.dispatchEvent(pS),this._lastPosition.copy(this.object.position),this._lastQuaternion.copy(this.object.quaternion),this._lastTargetPosition.copy(this.target),!0):!1}_getAutoRotationAngle(e){return e!==null?Wn/60*this.autoRotateSpeed*e:Wn/60/60*this.autoRotateSpeed}_getZoomScale(e){const i=Math.abs(e*.01);return Math.pow(.95,this.zoomSpeed*i)}_rotateLeft(e){this._sphericalDelta.theta-=e}_rotateUp(e){this._sphericalDelta.phi-=e}_panLeft(e,i){un.setFromMatrixColumn(i,0),un.multiplyScalar(-e),this._panOffset.add(un)}_panUp(e,i){this.screenSpacePanning===!0?un.setFromMatrixColumn(i,1):(un.setFromMatrixColumn(i,0),un.crossVectors(this.object.up,un)),un.multiplyScalar(e),this._panOffset.add(un)}_pan(e,i){const r=this.domElement;if(this.object.isPerspectiveCamera){const u=this.object.position;un.copy(u).sub(this.target);let f=un.length();f*=Math.tan(this.object.fov/2*Math.PI/180),this._panLeft(2*e*f/r.clientHeight,this.object.matrix),this._panUp(2*i*f/r.clientHeight,this.object.matrix)}else this.object.isOrthographicCamera?(this._panLeft(e*(this.object.right-this.object.left)/this.object.zoom/r.clientWidth,this.object.matrix),this._panUp(i*(this.object.top-this.object.bottom)/this.object.zoom/r.clientHeight,this.object.matrix)):(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - pan disabled."),this.enablePan=!1)}_dollyOut(e){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale/=e:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_dollyIn(e){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale*=e:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_updateZoomParameters(e,i){if(!this.zoomToCursor)return;this._performCursorZoom=!0;const r=this.domElement.getBoundingClientRect(),u=e-r.left,f=i-r.top,h=r.width,d=r.height;this._mouse.x=u/h*2-1,this._mouse.y=-(f/d)*2+1,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()}_clampDistance(e){return Math.max(this.minDistance,Math.min(this.maxDistance,e))}_handleMouseDownRotate(e){this._rotateStart.set(e.clientX,e.clientY)}_handleMouseDownDolly(e){this._updateZoomParameters(e.clientX,e.clientX),this._dollyStart.set(e.clientX,e.clientY)}_handleMouseDownPan(e){this._panStart.set(e.clientX,e.clientY)}_handleMouseMoveRotate(e){this._rotateEnd.set(e.clientX,e.clientY),this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const i=this.domElement;this._rotateLeft(Wn*this._rotateDelta.x/i.clientHeight),this._rotateUp(Wn*this._rotateDelta.y/i.clientHeight),this._rotateStart.copy(this._rotateEnd),this.update()}_handleMouseMoveDolly(e){this._dollyEnd.set(e.clientX,e.clientY),this._dollyDelta.subVectors(this._dollyEnd,this._dollyStart),this._dollyDelta.y>0?this._dollyOut(this._getZoomScale(this._dollyDelta.y)):this._dollyDelta.y<0&&this._dollyIn(this._getZoomScale(this._dollyDelta.y)),this._dollyStart.copy(this._dollyEnd),this.update()}_handleMouseMovePan(e){this._panEnd.set(e.clientX,e.clientY),this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd),this.update()}_handleMouseWheel(e){this._updateZoomParameters(e.clientX,e.clientY),e.deltaY<0?this._dollyIn(this._getZoomScale(e.deltaY)):e.deltaY>0&&this._dollyOut(this._getZoomScale(e.deltaY)),this.update()}_handleKeyDown(e){let i=!1;switch(e.code){case this.keys.UP:e.ctrlKey||e.metaKey||e.shiftKey?this._rotateUp(Wn*this.rotateSpeed/this.domElement.clientHeight):this._pan(0,this.keyPanSpeed),i=!0;break;case this.keys.BOTTOM:e.ctrlKey||e.metaKey||e.shiftKey?this._rotateUp(-Wn*this.rotateSpeed/this.domElement.clientHeight):this._pan(0,-this.keyPanSpeed),i=!0;break;case this.keys.LEFT:e.ctrlKey||e.metaKey||e.shiftKey?this._rotateLeft(Wn*this.rotateSpeed/this.domElement.clientHeight):this._pan(this.keyPanSpeed,0),i=!0;break;case this.keys.RIGHT:e.ctrlKey||e.metaKey||e.shiftKey?this._rotateLeft(-Wn*this.rotateSpeed/this.domElement.clientHeight):this._pan(-this.keyPanSpeed,0),i=!0;break}i&&(e.preventDefault(),this.update())}_handleTouchStartRotate(e){if(this._pointers.length===1)this._rotateStart.set(e.pageX,e.pageY);else{const i=this._getSecondPointerPosition(e),r=.5*(e.pageX+i.x),u=.5*(e.pageY+i.y);this._rotateStart.set(r,u)}}_handleTouchStartPan(e){if(this._pointers.length===1)this._panStart.set(e.pageX,e.pageY);else{const i=this._getSecondPointerPosition(e),r=.5*(e.pageX+i.x),u=.5*(e.pageY+i.y);this._panStart.set(r,u)}}_handleTouchStartDolly(e){const i=this._getSecondPointerPosition(e),r=e.pageX-i.x,u=e.pageY-i.y,f=Math.sqrt(r*r+u*u);this._dollyStart.set(0,f)}_handleTouchStartDollyPan(e){this.enableZoom&&this._handleTouchStartDolly(e),this.enablePan&&this._handleTouchStartPan(e)}_handleTouchStartDollyRotate(e){this.enableZoom&&this._handleTouchStartDolly(e),this.enableRotate&&this._handleTouchStartRotate(e)}_handleTouchMoveRotate(e){if(this._pointers.length==1)this._rotateEnd.set(e.pageX,e.pageY);else{const r=this._getSecondPointerPosition(e),u=.5*(e.pageX+r.x),f=.5*(e.pageY+r.y);this._rotateEnd.set(u,f)}this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const i=this.domElement;this._rotateLeft(Wn*this._rotateDelta.x/i.clientHeight),this._rotateUp(Wn*this._rotateDelta.y/i.clientHeight),this._rotateStart.copy(this._rotateEnd)}_handleTouchMovePan(e){if(this._pointers.length===1)this._panEnd.set(e.pageX,e.pageY);else{const i=this._getSecondPointerPosition(e),r=.5*(e.pageX+i.x),u=.5*(e.pageY+i.y);this._panEnd.set(r,u)}this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd)}_handleTouchMoveDolly(e){const i=this._getSecondPointerPosition(e),r=e.pageX-i.x,u=e.pageY-i.y,f=Math.sqrt(r*r+u*u);this._dollyEnd.set(0,f),this._dollyDelta.set(0,Math.pow(this._dollyEnd.y/this._dollyStart.y,this.zoomSpeed)),this._dollyOut(this._dollyDelta.y),this._dollyStart.copy(this._dollyEnd);const h=(e.pageX+i.x)*.5,d=(e.pageY+i.y)*.5;this._updateZoomParameters(h,d)}_handleTouchMoveDollyPan(e){this.enableZoom&&this._handleTouchMoveDolly(e),this.enablePan&&this._handleTouchMovePan(e)}_handleTouchMoveDollyRotate(e){this.enableZoom&&this._handleTouchMoveDolly(e),this.enableRotate&&this._handleTouchMoveRotate(e)}_addPointer(e){this._pointers.push(e.pointerId)}_removePointer(e){delete this._pointerPositions[e.pointerId];for(let i=0;i<this._pointers.length;i++)if(this._pointers[i]==e.pointerId){this._pointers.splice(i,1);return}}_isTrackingPointer(e){for(let i=0;i<this._pointers.length;i++)if(this._pointers[i]==e.pointerId)return!0;return!1}_trackPointer(e){let i=this._pointerPositions[e.pointerId];i===void 0&&(i=new ce,this._pointerPositions[e.pointerId]=i),i.set(e.pageX,e.pageY)}_getSecondPointerPosition(e){const i=e.pointerId===this._pointers[0]?this._pointers[1]:this._pointers[0];return this._pointerPositions[i]}_customWheelEvent(e){const i=e.deltaMode,r={clientX:e.clientX,clientY:e.clientY,deltaY:e.deltaY};switch(i){case 1:r.deltaY*=16;break;case 2:r.deltaY*=100;break}return e.ctrlKey&&!this._controlActive&&(r.deltaY*=10),r}}function nC(o){this.enabled!==!1&&(this._pointers.length===0&&(this.domElement.setPointerCapture(o.pointerId),this.domElement.addEventListener("pointermove",this._onPointerMove),this.domElement.addEventListener("pointerup",this._onPointerUp)),!this._isTrackingPointer(o)&&(this._addPointer(o),o.pointerType==="touch"?this._onTouchStart(o):this._onMouseDown(o)))}function iC(o){this.enabled!==!1&&(o.pointerType==="touch"?this._onTouchMove(o):this._onMouseMove(o))}function aC(o){switch(this._removePointer(o),this._pointers.length){case 0:this.domElement.releasePointerCapture(o.pointerId),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.dispatchEvent(KS),this.state=Ie.NONE;break;case 1:const e=this._pointers[0],i=this._pointerPositions[e];this._onTouchStart({pointerId:e,pageX:i.x,pageY:i.y});break}}function sC(o){let e;switch(o.button){case 0:e=this.mouseButtons.LEFT;break;case 1:e=this.mouseButtons.MIDDLE;break;case 2:e=this.mouseButtons.RIGHT;break;default:e=-1}switch(e){case to.DOLLY:if(this.enableZoom===!1)return;this._handleMouseDownDolly(o),this.state=Ie.DOLLY;break;case to.ROTATE:if(o.ctrlKey||o.metaKey||o.shiftKey){if(this.enablePan===!1)return;this._handleMouseDownPan(o),this.state=Ie.PAN}else{if(this.enableRotate===!1)return;this._handleMouseDownRotate(o),this.state=Ie.ROTATE}break;case to.PAN:if(o.ctrlKey||o.metaKey||o.shiftKey){if(this.enableRotate===!1)return;this._handleMouseDownRotate(o),this.state=Ie.ROTATE}else{if(this.enablePan===!1)return;this._handleMouseDownPan(o),this.state=Ie.PAN}break;default:this.state=Ie.NONE}this.state!==Ie.NONE&&this.dispatchEvent(Zp)}function rC(o){switch(this.state){case Ie.ROTATE:if(this.enableRotate===!1)return;this._handleMouseMoveRotate(o);break;case Ie.DOLLY:if(this.enableZoom===!1)return;this._handleMouseMoveDolly(o);break;case Ie.PAN:if(this.enablePan===!1)return;this._handleMouseMovePan(o);break}}function oC(o){this.enabled===!1||this.enableZoom===!1||this.state!==Ie.NONE||(o.preventDefault(),this.dispatchEvent(Zp),this._handleMouseWheel(this._customWheelEvent(o)),this.dispatchEvent(KS))}function lC(o){this.enabled===!1||this.enablePan===!1||this._handleKeyDown(o)}function uC(o){switch(this._trackPointer(o),this._pointers.length){case 1:switch(this.touches.ONE){case Jr.ROTATE:if(this.enableRotate===!1)return;this._handleTouchStartRotate(o),this.state=Ie.TOUCH_ROTATE;break;case Jr.PAN:if(this.enablePan===!1)return;this._handleTouchStartPan(o),this.state=Ie.TOUCH_PAN;break;default:this.state=Ie.NONE}break;case 2:switch(this.touches.TWO){case Jr.DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchStartDollyPan(o),this.state=Ie.TOUCH_DOLLY_PAN;break;case Jr.DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchStartDollyRotate(o),this.state=Ie.TOUCH_DOLLY_ROTATE;break;default:this.state=Ie.NONE}break;default:this.state=Ie.NONE}this.state!==Ie.NONE&&this.dispatchEvent(Zp)}function cC(o){switch(this._trackPointer(o),this.state){case Ie.TOUCH_ROTATE:if(this.enableRotate===!1)return;this._handleTouchMoveRotate(o),this.update();break;case Ie.TOUCH_PAN:if(this.enablePan===!1)return;this._handleTouchMovePan(o),this.update();break;case Ie.TOUCH_DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchMoveDollyPan(o),this.update();break;case Ie.TOUCH_DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchMoveDollyRotate(o),this.update();break;default:this.state=Ie.NONE}}function fC(o){this.enabled!==!1&&o.preventDefault()}function hC(o){o.key==="Control"&&(this._controlActive=!0,this.domElement.getRootNode().addEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function dC(o){o.key==="Control"&&(this._controlActive=!1,this.domElement.getRootNode().removeEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function fl(o,e){return[o[0]+e[0],o[1]+e[1]]}function Qr(o,e){return[o[0]*e[0]-o[1]*e[1],o[0]*e[1]+o[1]*e[0]]}function pC(o){return Math.hypot(o[0],o[1])}function pc(o,e){const i=Math.hypot(o[0],o[1]);if(i===0)return[0,0];const r=Math.atan2(o[1],o[0]),u=Math.log(i),f=e[0]*u-e[1]*r,h=e[1]*u+e[0]*r,d=Math.exp(f);return[d*Math.cos(h),d*Math.sin(h)]}const mc=[1];function mC(o){for(let e=mc.length;e<=o;e++)mc[e]=mc[e-1]*e;return mc[o]}const _C=[1,-.5,1/6,0,-1/30,0,1/42,0,-1/30,0,5/66,0,-691/2730,0,7/6,0,-3617/510];function pl(o){let r=[0,0];for(let v=1;v<40;v++)r=fl(r,pc([v,0],[-o[0],-o[1]]));const u=[40,0],f=(o[0]-1)*(o[0]-1)+o[1]*o[1];if(f===0)return[1/0,0];const h=[(o[0]-1)/f,-o[1]/f];let d=Qr(h,pc(u,[1-o[0],-o[1]]));d=fl(d,Qr([.5,0],pc(u,[-o[0],-o[1]])));let p=[1,0],g=[0,0];for(let v=1;v<=8;v++){p=Qr(p,[o[0]+2*v-2,o[1]]),p=Qr(p,[o[0]+2*v-1,o[1]]);const _=_C[2*v]/mC(2*v);g=fl(g,Qr([_,0],Qr(p,pc(u,[1-o[0]-2*v,-o[1]]))))}return fl(r,fl(d,g))}function gC(){const o=pl([2,0]),e=pl([4,0]),i=pl([.5,0]),r=pl([.5,14.134725142]);return{z2:o[0],z2err:Math.abs(o[0]-Math.PI*Math.PI/6),z4:e[0],z4err:Math.abs(e[0]-Math.pow(Math.PI,4)/90),zh:i[0],zherr:Math.abs(i[0]+1.4603545088095868),zcrit:pC(r)}}const vC=[14.134725142,21.022039639,25.01085758,30.424876126,32.935061588,37.586178159,40.918719012,43.327073281,48.005150881,49.773832478,52.970321478,56.446247697,59.347044003,60.831778525,65.112544048];function SC(o){const e=o.clientWidth||800,i=o.clientHeight||600,r=new WR;r.background=new ye(856608);const u=new Si(50,e/i,.1,500);u.position.set(26,20,30);const f=new qR({antialias:!0});f.setSize(e,i),o.appendChild(f.domElement);const h=new eC(u,f.domElement);h.enableDamping=!0;const d=new QR(16777215,.55);r.add(d);const p=new KR(16777215,1.1);p.position.set(30,40,25),r.add(p);let g=0;const v=()=>{g=requestAnimationFrame(v),h.update(),f.render(r,u)};v();const _=new Set([d,p]),y=()=>{const E=o.clientWidth,R=o.clientHeight;E>0&&R>0&&(u.aspect=E/R,u.updateProjectionMatrix(),f.setSize(E,R))};window.addEventListener("resize",y);const M=E=>{E.traverse?.(R=>{R.geometry?.dispose?.(),Array.isArray(R.material)?R.material.forEach(x=>x.dispose?.()):R.material?.dispose?.()})};return{scene:r,camera:u,renderer:f,controls:h,clear(){for(let E=r.children.length-1;E>=0;E--){const R=r.children[E];_.has(R)||(r.remove(R),M(R))}},dispose(){cancelAnimationFrame(g),window.removeEventListener("resize",y),this.clear(),h.dispose(),f.dispose(),f.domElement.parentNode?.removeChild(f.domElement)}}}function yC(o,e=18,i=.5,r=4,u=96){o.clear();let f=u;const h=()=>(f=(f*1103515245+12345)%2147483648)/2147483648,d=[];for(let M=0;M<r;M++)d.push([1+h()*(e-1),1+h()*(e-1)]);const p=new dl,g=new Pc({color:2899558}),v=[];for(let M=0;M<e;M++)for(let E=0;E<e;E++)v.push(new Q(M,0,E),new Q(M+1,0,E)),v.push(new Q(M,0,E),new Q(M,0,E+1));p.add(new jS(new Qn().setFromPoints(v),g));const _=new co(.22,1,.22);for(let M=0;M<e;M++)for(let E=0;E<e;E++){const R=2*Math.PI*i*(E+1)%(2*Math.PI),x=R/(2*Math.PI),S=new js({color:new ye().setHSL(x,.75,.55)}),L=.4+.9*Math.abs(Math.sin(R)),U=new jn(_,S);U.position.set(E,L/2,M),U.scale.y=L,p.add(U)}const y=new Wp(.5,1.6,20);for(const[M,E]of d){const R=new jn(y,new js({color:16733491}));R.position.set(E,1.4,M),p.add(R)}return o.scene.add(p),o.camera.position.set(e*1.3,e,e*1.5),o.controls.target.set(e/2,0,e/2),{vortices:d}}function xC(o,e=6,i=1.9){o.clear();const r=72,u=new yl(2*e,2*e,r,r);u.rotateX(-Math.PI/2);const f=u.attributes.position,h=[];for(let g=0;g<f.count;g++){const v=f.getX(g),_=f.getZ(g),y=Math.hypot(v,_),M=i*y*(y<=e?1:0);f.setY(g,M);const E=Math.min(1,Math.abs(M)/(i*e)),R=new ye().setHSL(M>=0?.58:0,.8,.35+.35*E);h.push(R.r,R.g,R.b)}u.setAttribute("color",new gn(h,3)),u.computeVertexNormals();const d=new jn(u,new js({vertexColors:!0,side:Li,wireframe:!1,transparent:!0,opacity:.92}));o.scene.add(d);const p=new JR(2*e,12,2241365,1713216);p.position.y=-.01,o.scene.add(p),o.camera.position.set(9,7,11),o.controls.target.set(0,0,0)}function MC(o,e=40,i=81,r=240){o.clear();let u=0;const f=i*r,h=new Qn,d=new Float32Array(f*3),p=new Float32Array(f*3),g=[],v=[],_=[],y=[];for(let S=0;S<i;S++)for(let L=0;L<r;L++){const U=S/(i-1)*1.2,P=L/(r-1)*e,J=pl([U,P]),B=Math.hypot(J[0],J[1]);u=Math.max(u,B),v.push(U),_.push(P),y.push(B)}for(let S=0;S<v.length;S++){d[3*S]=v[S]-.6,d[3*S+1]=Math.min(y[S],6),d[3*S+2]=_[S]-e/2;const L=Math.min(.85,y[S]/3),U=new ye().setHSL(.62-.62*L,.85,.28+.4*L);p[3*S]=U.r,p[3*S+1]=U.g,p[3*S+2]=U.b}for(let S=0;S<i-1;S++)for(let L=0;L<r-1;L++){const U=S*r+L,P=U+1,J=U+r,B=J+1;g.push(U,J,P,P,J,B)}h.setAttribute("position",new xi(d,3)),h.setAttribute("color",new xi(p,3)),h.setIndex(g),h.computeVertexNormals();const M=new jn(h,new js({vertexColors:!0,side:Li}));o.scene.add(M);const E=new Pc({color:16766282}),R=[new Q(-.1,0,-e/2),new Q(-.1,0,e/2)];o.scene.add(new WS(new Qn().setFromPoints(R),E));const x=new jp(.22,16,16);for(const S of vC){if(S>e)break;const L=new jn(x,new js({color:16724821}));L.position.set(-.1,.05,S-e/2),o.scene.add(L)}return o.camera.position.set(4.5,7,22),o.controls.target.set(-.1,1.2,0),{eMax:u}}function EC(){try{const o=document.createElement("canvas");return!!(window.WebGLRenderingContext&&(o.getContext("webgl2")||o.getContext("webgl")))}catch{return!1}}function TC(){const o=wi.useRef(null),e=wi.useRef(null),[i,r]=wi.useState("hofstadter"),[u,f]=wi.useState(.5),[h,d]=wi.useState(4),[p,g]=wi.useState(""),[v,_]=wi.useState(null),[y,M]=wi.useState("");return wi.useEffect(()=>{_(gC())},[]),wi.useEffect(()=>{if(o.current){if(!EC()){M("WebGL is not available in this browser/environment. The 3D laboratory needs hardware (or software) WebGL — try Chrome, Firefox or Safari with hardware acceleration enabled.");return}try{e.current=SC(o.current)}catch(E){M(`Failed to initialize the WebGL renderer — ${E.message}`);return}return()=>{e.current&&e.current.dispose(),e.current=null}}},[]),wi.useEffect(()=>{const E=e.current;if(!(!E||y))if(i==="hofstadter"){const{vortices:R}=yC(E,18,u,h);g(`Lattice 18×18, α = ${u}, ${R.length} vortices (red cones, q=+1). Site bars are colored by the Landau phase 2πα·j — the GUE mechanism of the suite is the vortex phase field (:monumental gauge).`)}else i==="dirac"?(xC(E,6,1.9),g("Dirac cone E(k) = v_F·|k| at α = 1/2 (vortex q=+1): the chiral tower of suite tests 19/30, v_F(2π) = 1.9.")):(MC(E,40,61,200),g(`|ζ(σ+it)| for σ ∈ [0, 1.2], t ∈ [0, 40] — the critical strip (3D-34). Yellow line: Re s = 1/2; red spheres: embedded zeros γ₁..γ₁₅. JS ζ-evaluator self-check: |ζ(2)−π²/6| = ${v?v.z2err.toExponential(2):"…"}.`))},[i,u,h,v]),cn.jsxs("div",{className:"app",children:[cn.jsxs("header",{children:[cn.jsx("h1",{children:"AB-Cloud — 3D Laboratory"}),cn.jsx("p",{className:"muted",children:"Hofstadter lattice with vortices · Dirac cone · ζ critical strip — WebGL/Three.js, real-time. Suite 3D-1…3D-34 (Julia) visualized."}),cn.jsxs("nav",{children:[cn.jsx("button",{className:i==="hofstadter"?"btn active":"btn",onClick:()=>r("hofstadter"),children:"Hofstadter lattice"}),cn.jsx("button",{className:i==="dirac"?"btn active":"btn",onClick:()=>r("dirac"),children:"Dirac cone"}),cn.jsx("button",{className:i==="zeta"?"btn active":"btn",onClick:()=>r("zeta"),children:"ζ critical strip"})]}),i==="hofstadter"&&cn.jsxs("div",{className:"controls",children:[cn.jsxs("label",{children:["α = ",u.toFixed(2),cn.jsx("input",{type:"range",min:"0",max:"1",step:"0.05",value:u,onChange:E=>f(+E.target.value)})]}),cn.jsxs("label",{children:["vortices = ",h,cn.jsx("input",{type:"range",min:"0",max:"12",value:h,onChange:E=>d(+E.target.value)})]})]})]}),cn.jsx("div",{ref:o,className:"canvas-host"}),y&&cn.jsx("p",{className:"gl-error",children:y}),!y&&cn.jsx("p",{className:"info",children:p}),cn.jsxs("footer",{className:"muted",children:["Source: ",cn.jsx("code",{children:"apps/ab-cloud-lab3d/"})," (React 19 + Vite + Three.js). ζ evaluator: self-anchored Euler–Maclaurin (port of 3D-34); check anchors ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(1/2)≈−1.4603545."]})]})}VM.createRoot(document.getElementById("root")).render(cn.jsx(TC,{}));
